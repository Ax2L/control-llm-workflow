# Function File for Scenario workflows
from modules.utils import add_to_conversation_history, log
import requests
import sseclient
import json


def check_prompts(input_data):
    log("Checking prompts...")  # Log start
    # Check prompts from Jira
    prompts = input_data
    log(f"Prompts: {prompts}")
    print(f"Here are the prompts: {prompts}")
    # save_new_tasks("data/tasks.json", tasks)
    log("Prompts checked successfully.")  # Log end
    return prompts


# LLM request to Ollama
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser


def send_instruction_to_ollama(prompt, model_name, conversation_id):
    log(f"Preparing to send instruction to Ollama model {model_name}...")  # Log start
    try:
        log(f"Sending instruction to Ollama model {model_name}...")
        llm = Ollama(model=model_name, temperature=0.0)
        output_parser = StrOutputParser()
        result = llm.invoke(prompt)
        parsed_result = output_parser.parse(result)
        log(f"Received response from Ollama model {model_name}.")
        add_to_conversation_history(conversation_id, parsed_result)
        return parsed_result
    except Exception as e:
        log(f"Error sending instruction to Ollama: {e}")
        raise e
    finally:
        log(f"Finished sending instruction to Ollama model {model_name}.")  # Log end


def send_instruction_to_oobabooga(
    prompt,
    conversation_id,
    max_tokens=200,
    temperature=1,
    top_p=0.9,
    seed=None,
    stream=False,
):
    """
    Generate text using the oobabooga/text-generation-webui API.

    Args:
        prompt (str): The input prompt for text generation.
        max_tokens (int): The maximum number of tokens to generate.
        temperature (float): Sampling temperature.
        top_p (float): Nucleus sampling probability.
        seed (int, optional): Random seed for reproducibility.
        stream (bool): Whether to use streaming for the response.

    Returns:
        str: The generated text.
    """
    url = "http://192.168.1.99:5000/v1/completions"
    headers = {"Content-Type": "application/json"}
    data = {
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "top_p": top_p,
        "stream": stream,
    }
    if seed is not None:
        data["seed"] = seed

    response = requests.post(url, headers=headers, json=data, verify=False)
    if stream:
        client = sseclient.SSEClient(response)
        generated_text = ""
        for event in client.events():
            payload = json.loads(event.data)
            generated_text += payload["choices"][0]["text"]
        add_to_conversation_history(conversation_id, generated_text)
        return generated_text
    else:
        add_to_conversation_history(conversation_id, response.json()["choices"][0]["text"])
        return response.json()["choices"][0]["text"]


# ... existing code ...
