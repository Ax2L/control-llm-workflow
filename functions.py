# Function File for Scenario workflows


from modules.utils import log  # Import the log function

def check_prompts(input_data):
    log("Checking prompts...")  # Log start
    # Check prompts from Jira
    prompts = input_data
    log(f"Prompts: {prompts}")
    print(f"Here are the prompts: {prompts}")
    #save_new_tasks("data/tasks.json", tasks)
    log("Prompts checked successfully.")  # Log end
    return prompts






# LLM request to Ollama
from langchain_community.llms import Ollama
from langchain_core.output_parsers import StrOutputParser
from modules.utils import log

def send_instruction_to_ollama(instruction, model_name):
    log(f"Preparing to send instruction to Ollama model {model_name}...")  # Log start
    try:
        log(f"Sending instruction to Ollama model {model_name}...")
        llm = Ollama(model=model_name, temperature=0.0)
        output_parser = StrOutputParser()
        result = llm.invoke(instruction)
        parsed_result = output_parser.parse(result)
        log(f"Received response from Ollama model {model_name}.")
        return parsed_result
    except Exception as e:
        log(f"Error sending instruction to Ollama: {e}")
        raise e
    finally:
        log(f"Finished sending instruction to Ollama model {model_name}.")  # Log end






