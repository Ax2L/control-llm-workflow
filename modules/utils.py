# Date: 12.09.2024
# Author: Vsewolod Schmidt
# Description: Utility functions for logging and loading conversations.

import os
import time
import json
from taipy.gui import notify
import subprocess

log_file = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs.txt")

def log(message):
    """
    Log a message with a timestamp to both a file and the terminal.
    
    Args:
        message (str): The message to log.
    """
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    log_message = f"{timestamp} - {message}"
    with open(log_file, "a") as f:
        f.write(log_message + "\n")
    print(log_message)  # Log to terminal as well

def show_answer(state, task_id):
    """
    Show the answer for a given task ID from the state.
    
    Args:
        state (object): The state object containing answers.
        task_id (str): The ID of the task.
    
    Returns:
        str: The answer for the task or "n/a" if not found.
    """
    log(f"Showing answer for Task ID: {task_id}")  # Log start
    if state is None or state.answers is None:
        log(f"No answer found for Task ID: {task_id}")
        return "n/a"
    answer = state.answers.get(task_id, "n/a")
    log(f"Answer for Task ID: {task_id} is {answer}")
    return answer

def load_conversation(task_id):
    """
    Load the conversation for a given task ID from a JSON file.
    
    Args:
        task_id (str): The ID of the task.
    
    Returns:
        dict: The conversation data or None if the file does not exist.
    """
    log(f"Loading conversation for Task ID: {task_id}")  # Log start
    file_path = f"data/{task_id}.json"
    if not os.path.exists(file_path):
        log(f"Conversation file for Task ID {task_id} does not exist.")
        return None

    with open(file_path, "r") as file:
        conversation = json.load(file)
    log(f"Conversation for Task ID {task_id} loaded successfully.")
    return conversation

def ask_llm_action(state, task_id, summary, description):
    """
    Trigger the LLM action for a given task ID.
    
    Args:
        state (object): The state object.
        task_id (str): The ID of the task.
        summary (str): The summary of the task.
        description (str): The description of the task.
    """
    log(f"Asking LLM action for Task ID: {task_id}")  # Log start
    answer = ask_llm_solution(task_id, summary, description)
    state.answers[task_id] = answer
    notify(state, f"Answer for Task {task_id} received!", "success")
    log(f"LLM action for Task ID: {task_id} completed successfully.")  # Log end

def ask_llm_solution(task_id, summary, description):
    """
    Ask the LLM for a solution for a given task ID.
    
    Args:
        task_id (str): The ID of the task.
        summary (str): The summary of the task.
        description (str): The description of the task.
    
    Returns:
        str: The answer from the LLM.
    """
    log(f"Asking LLM for solution for Task ID: {task_id}")  # Log start
    context = f"Summary: {summary}\nDescription: {description}"
    answer = ask_llm(context)
    tasks = load_existing_tasks("data/tasks.json")
    for task in tasks:
        if task["ID"] == task_id:
            task["Answers"] = f"data/{task_id}.json"
            task["Status"] = "discussed"
            break
    with open("data/tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)
    log(f"LLM solution for Task ID: {task_id} received and saved.")
    return answer

def load_config():
    """
    Load configuration settings from the config.json file.

    Returns:
        dict: Configuration settings.
    """
    log("Loading configuration...")  # Log start
    with open("config/config.json") as f:
        config = json.load(f)
    log("Configuration loaded successfully.")
    return config

def generate_mermaid_diagram(config_path="config/config.json"):
    """
    Generate a Mermaid diagram from the configuration settings.

    Args:
        config_path (str): Path to the configuration file.
    
    Returns:
        str: The Mermaid diagram as a string.
    """
    log("Generating Mermaid diagram...")  # Log start
    with open(config_path, "r") as f:
        config = json.load(f)

    system_prompts = config.get("system_prompts", {})
    mermaid_diagram = "graph LR\n"

    for llm_key, llm_data in system_prompts.items():
        title = llm_data.get("title", llm_key)
        input_data = llm_data.get("input", [])
        output_data = llm_data.get("output", "")

        mermaid_diagram += f'{llm_key}["{title}"]\n'
        for input_item in input_data:
            mermaid_diagram += f"{input_item} --> {llm_key}\n"
        mermaid_diagram += f"{llm_key} --> {output_data}\n"

    # Save the mermaid diagram to a file
    mermaid_file_path = "assets/images/jira_assistant_llm_workflow.mmd"
    with open(mermaid_file_path, "w") as f:
        f.write(mermaid_diagram)

    # Use mermaid-cli (mmdc) to convert the mermaid diagram to SVG
    svg_file_path = "assets/images/jira_assistant_llm_workflow.svg"
    subprocess.run(["mmdc", "-i", mermaid_file_path, "-o", svg_file_path, "-t", "dark", "-b", "transparent"])

    log("Mermaid diagram generated and converted to SVG successfully.")
    return mermaid_diagram

def add_task_action(state, task_id, summary, description):
    """
    Add a new task to the state.

    Args:
        state (object): The state object.
        task_id (str): The ID of the task.
        summary (str): The summary of the task.
        description (str): The description of the task.
    """
    log(f"Adding new task: {task_id}")  # Log start
    new_task = {"ID": task_id, "Summary": summary, "Description": description}
    state.tasks = state.tasks.append(new_task, ignore_index=True)
    notify(state, "success", f"Task {task_id} added successfully!")
    log(f"Task {task_id} added successfully.")  # Log end

def get_task_details(task_id):
    """
    Get the details of a task by its ID.

    Args:
        task_id (str): The ID of the task.

    Returns:
        dict: The task details or None if not found.
    """
    log(f"Fetching details for Task ID: {task_id}")  # Log start
    tasks = load_existing_tasks("data/tasks.json")
    for task in tasks:
        if task["ID"] == task_id:
            log(f"Details for Task ID: {task_id} fetched successfully.")
            return task
    log(f"No details found for Task ID: {task_id}")
    return None

def clean_string(input_variables):
    """
    Clean a string by removing certain characters.

    Args:
        input_variables (str): The input string.

    Returns:
        str: The cleaned string.
    """
    log("Cleaning string...")  # Log start
    cleaned_input_variables = (
        str(input_variables).replace("[", "")
        .replace("]", "")
        .replace("{", "")
        .replace("}", "")
        .replace("'", "")
    )
    log("String cleaned successfully.")  # Log end
    return cleaned_input_variables

def ensure_conversation_folder(conversation_id):
    """
    Ensure that a folder for the given Conversation-ID exists and store each result inside it.
    Maintain a JSON file as a history list for the Conversation ID.

    Args:
        conversation_id (str): The ID of the conversation.
    """
    log(f"Ensuring folder exists for Conversation ID: {conversation_id}")  # Log start
    folder_path = os.path.join("data/conversations", conversation_id)
    os.makedirs(folder_path, exist_ok=True)

    history_file = os.path.join(folder_path, "history.json")
    if not os.path.exists(history_file):
        with open(history_file, "w") as f:
            json.dump([], f)  # Initialize with an empty list

    log(f"Folder and history file for Conversation ID: {conversation_id} ensured.")  # Log end

def add_to_conversation_history(conversation_id, result):
    """
    Add a result to the conversation history for the given Conversation-ID.

    Args:
        conversation_id (str): The ID of the conversation.
        result (dict): The result to add to the history.
    """
    log(f"Adding result to history for Conversation ID: {conversation_id}")  # Log start
    ensure_conversation_folder(conversation_id)
    history_file = os.path.join("data/conversations", conversation_id, "history.json")

    with open(history_file, "r") as f:
        history = json.load(f)

    history.append(result)

    with open(history_file, "w") as f:
        json.dump(history, f, indent=4)

    log(f"Result added to history for Conversation ID: {conversation_id} successfully.")  # Log end
