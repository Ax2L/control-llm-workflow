# Function File for Scenario workflows
from modules.utils import add_to_conversation_history, log
import requests
import sseclient
import json
import os




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



def send_instruction_to_oobabooga(prompt, conversation_id=None):
    log(f"Preparing to send instruction to oobabooga...")
    max_tokens = 200
    temperature = 1
    top_p = 0.9
    stream = False
    url = "http://192.168.10.99:5000/v1/completions"
    headers = {"Content-Type": "application/json"}
    data = {
        "prompt": prompt,
        "max_tokens": max_tokens,
        "temperature": temperature,
        "top_p": top_p,
        "stream": stream,
    }

    try:
        log(f"Sending request to oobabooga API...")
        response = requests.post(url, headers=headers, json=data, verify=False)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        log(f"Received response from oobabooga API. Status code: {response.status_code}")
        log(f"Response content: {response.text[:500]}...")  # Log the first 500 characters of the response
        
        try:
            result_json = response.json()
            result_text = result_json["choices"][0]["text"]
        except json.JSONDecodeError:
            log("Failed to parse JSON response. Using raw text instead.")
            result_text = response.text
        
        if conversation_id:
            add_to_conversation_history(conversation_id, result_text)
        
        return result_text
    except requests.exceptions.RequestException as e:
        log(f"Error sending instruction to oobabooga: {e}")
        if hasattr(e, 'response'):
            log(f"Response status code: {e.response.status_code}")
            log(f"Response content: {e.response.text[:500]}...")  # Log the first 500 characters of the error response
        raise
    finally:
        log(f"Finished sending instruction to oobabooga.")



def load_test_questions(path_or_data):
    log(f"Loading test questions...")  # Log start
    try:
        if isinstance(path_or_data, dict):
            # If it's already a dictionary, return it directly
            log("Test questions loaded from provided data.")
            return path_or_data
        elif isinstance(path_or_data, str) and os.path.exists(path_or_data):
            # If it's a file path, load the JSON file
            with open(path_or_data, 'r') as file:
                data = json.load(file)
            log(f"Test questions loaded successfully from {path_or_data}.")
            return data
        else:
            raise ValueError("Invalid input: expected a dictionary or a valid file path.")
    except Exception as e:
        log(f"Error loading test questions: {e}")
        raise e

def send_to_llm(question):
    
    # Placeholder function to simulate LLM response
    return f"Response to: {question}"


def llm_result_analysis(analysis_json_list, model_name):
    log("Starting LLM result analysis...")
    questions = analysis_json_list.get('jokes_prompts', [])
    responses = []
    for question in questions:
        prompt = question.get('prompt', '')
        try:
            response = send_instruction_to_oobabooga(prompt, model_name)
        except Exception as e:
            log(f"Error processing question '{prompt}': {e}")
            response = f"Error: {str(e)}"
        responses.append({
            "question": prompt,
            "response": response
        })
    log("LLM result analysis completed.")
    return json.dumps(responses)

