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
    if state is None or state.answers is None:
        return "n/a"
    return state.answers.get(task_id, "n/a")

def load_conversation(task_id):
    """
    Load the conversation for a given task ID from a JSON file.
    
    Args:
        task_id (str): The ID of the task.
    
    Returns:
        dict: The conversation data or None if the file does not exist.
    """
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
    log(f"Asking LLM action triggered for Task ID: {task_id}")
    answer = ask_llm_solution(task_id, summary, description)
    state.answers[task_id] = answer
    notify(state, f"Answer for Task {task_id} received!", "success")

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
    log(f"Asking LLM for solution for Task ID: {task_id}")
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
    log("Loading configuration...")
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
    log("Generating Mermaid diagram...")
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
    log(f"Adding new task: {task_id}")
    new_task = {"ID": task_id, "Summary": summary, "Description": description}
    state.tasks = state.tasks.append(new_task, ignore_index=True)
    notify(state, "success", f"Task {task_id} added successfully!")

def get_task_details(task_id):
    """
    Get the details of a task by its ID.

    Args:
        task_id (str): The ID of the task.

    Returns:
        dict: The task details or None if not found.
    """
    log(f"Fetching details for Task ID: {task_id}")
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
    cleaned_input_variables = (
        str(input_variables).replace("[", "")
        .replace("]", "")
        .replace("{", "")
        .replace("}", "")
        .replace("'", "")
    )
    return cleaned_input_variables
