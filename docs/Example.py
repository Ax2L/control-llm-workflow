import os
import json
import time
import subprocess
import pandas as pd
from taipy.gui import Gui, Markdown, notify, navigate
from dotenv import load_dotenv

import threading

# Import custom modules
from modules.utils import log, load_config, clean_string, generate_mermaid_diagram
from ask_llm import main as ask_llm
from modules.collect_tasks import get_jira_tasks, load_existing_tasks, save_new_tasks

# Load the config
config = load_config()


# Initialize the GUI
def run_ask_llm_script():
    while True:
        log("Running ask_llm.py script...")
        subprocess.run(["python", "ask_llm.py"])
        log("ask_llm.py script execution completed. Sleeping for 5 minutes...")
        time.sleep(300)


# Function to collect tasks from Jira and append missing tasks
def collect_tasks():
    log("Collecting tasks from Jira...")
    tasks = get_jira_tasks()
    save_new_tasks("data/tasks.json", tasks)
    tasks_df = pd.DataFrame(load_existing_tasks("data/tasks.json"))
    tasks_df = tasks_df[
        ["ID", "Topic", "Context", "Status"]
    ]  # Ensure only these columns are present
    log("Tasks collected and saved successfully.")
    return tasks_df


# Function to get a list of all Task-ID numbers from tasks.json
def get_task_ids():
    log("Fetching task IDs...")
    tasks = load_existing_tasks("data/tasks.json")
    task_ids = [task["ID"] for task in tasks]
    log("Task IDs fetched successfully.")
    return task_ids


# Define the actions for the buttons
def collect_tasks_action(state):
    log("Collecting tasks action triggered.")
    state.tasks = collect_tasks()
    notify(state, "success", "Tasks collected successfully!")


def update_config(state, key, value):
    log(f"Updating config: {key} to {value}")
    config[key] = value
    with open("config/config.json", "w") as f:
        json.dump(config, f, indent=4)
    notify(state, f"Config {key} updated to {value}!", "success")


def load_conversation(state):
    file_path = f"data/{state.task_id}.json"
    if not os.path.exists(file_path):
        log(f"Conversation file for Task ID {state.task_id} does not exist.")
        conversation_md = "<|No conversation available for this task.|>"
        state.conversation_partial.update_content(state, conversation_md)
        return conversation_md

    with open(file_path, "r") as file:
        conversation = json.load(file)
    log(f"Conversation for Task ID {state.task_id} loaded successfully.")

    # Load config
    config = load_config()

    # Create the structured view
    conversation_md = ""
    count_steps = 4
    for step in reversed(conversation.get("Conversation", [])):
        count_steps -= 1
        prompt_count = f"LLM{str(count_steps)}"
        expanded_boolean = False
        prompt_title = config["system_prompts"][prompt_count]["title"]
        input_variables = clean_string(config["system_prompts"][prompt_count]["input"])
        prompt_prompt = clean_string(config["system_prompts"][prompt_count]["prompt"])
        prompt_output = clean_string(config["system_prompts"][prompt_count]["output"])
        if count_steps == 3:
            expanded_boolean = False
        # for detail in details:
        conversation_md += f"""
<|Step {count_steps}: {prompt_title}|expandable|class_name=conversation-step-{count_steps}|expanded={expanded_boolean}|
<|part|class_name=conversation-step-response-{count_steps}|
<|{step['result']}
|>
<|layout|columns=100px auto 100px|class_name=conversation-step-layout-{count_steps}|
<|part|class_name=conversation-step-input-{count_steps}|
<|Input|text|mode=markdown|>
<|{input_variables}|text|mode=markdown|label="Input variables"|>
|>
<|part|class_name=conversation-step-prompt-{count_steps} m-auto|
<|Prompt|text|mode=markdown|>
<|{prompt_prompt}|text|mode=markdown|label="LLM Prompt"|>
|>
<|part|class_name=conversation-step-output-{count_steps}|
<|Output|text|mode=markdown|>
<|{prompt_output}|text|mode=markdown|label="Output Variable"|>
|>
|>
|>
|>
"""
    conversation_md += "\n"
    state.conversation_partial.update_content(state, conversation_md)
    return conversation_md

# Function to refresh the conversation partial
def refresh_conversation(state):
    conversation_md = load_conversation(state)
    state.conversation_partial.update_content(state, conversation_md)

page_titel = f"{config['project_title']}"
tasks_md = Markdown(
    """
<|layout|columns=200px 1|class_name=p-0 m-0|
<|part|class_name=sidebar scrollable|
<|{task_id}|selector|lov={tasks_list}|type=Jira-Task|filter|class_name=scrollable nolabel|height=600px|on_change=refresh_conversation|>
<|Fetch latest Tasks|button|class_name=headernavibar_fetch_tasks align_items_center justify_content_center m-auto|on_action=collect_tasks_action|hover_text="Update the list of available tasks"|>
<|{page_titel}|text|mode=markdown|class_name=headerlogo|>
|>

<|part|class_name=main-content|label="Right Side"|

<|layout|columns=150px auto 150px|
<|part|class_name=card card-bg headernavibar_cards|label="ID"|hover_text="ID of the task"|
<|{get_taskdata('ID', task_id)}|text|label="ID"|>
|>
<|part|class_name=card card-bg headernavibar_cards|label="Topic"|hover_text="Topic of the task"|
<|{get_taskdata('Topic', task_id)}|text|label="Topic"|>
|>
<|part|class_name=card card-bg headernavibar_cards|label="Status"|hover_text="Status of the task"|
<|{get_taskdata('Status', task_id)}|text|label="Status"|>
|>
|>
<|Jira Task Context|expandable|class_name=headernavibar_context|expanded=true|
<|{get_taskdata('Context', task_id)}|text|mode=markdown|label="Context"|class_name=headernavibar_context_inside|>
|>
<|part|partial={conversation_partial}|>
<|LLM Workflow|expandable|class_name=headernavibar_workflow|expanded=false|
<|assets/images/jira_assistant_llm_workflow.svg|image|label=Mermaid Diagram|width=100%|class_name=align_items_center m-auto|>
|>
|>
|>
"""
)


def get_taskdata(parameter, task_id):
    log(f"Fetching task data for parameter: {parameter}, Task ID: {task_id}")
    tasks = load_existing_tasks("data/tasks.json")
    for task in tasks:
        if task["ID"] == task_id:
            log(
                f"Task data for parameter: {parameter}, Task ID: {task_id} fetched successfully."
            )
            if parameter == "Conversation":
                try:
                    conversation_data = load_conversation(task_id)
                    return conversation_data
                except (FileNotFoundError, json.JSONDecodeError) as e:
                    log(f"Error loading conversation data for Task ID: {task_id} - {e}")
                    return "n/a"
            return task.get(parameter, "n/a")
    log(f"No task data found for parameter: {parameter}, Task ID: {task_id}")
    return "n/a"


# Initialize variables
task_id = None
topic = None
context = None
status = None
answer = None
answers = None

# Collect tasks and get task IDs
tasks = collect_tasks()
tasks_list = get_task_ids()

# Ensure root_page is defined before this line
root_page = ""  # Define root_page appropriately
pages = {"/": root_page, "Tasks": tasks_md}


def initialize_jira_task(state):
    log("Initializing JiraTask...")
    tasks = load_existing_tasks("data/tasks.json")
    if tasks:
        first_task = tasks[0]
        state.task_id = first_task["ID"]
        state.topic = first_task["Topic"]
        state.context = first_task["Context"]
        state.status = first_task["Status"]
        state.answer = first_task.get("Answers", "")
    log("JiraTask initialized successfully.")


# Initialize the application state
def on_init(state):
    state.task_id = "1234"
    state.topic = "Test"
    state.context = "Test"
    state.status = ""
    state.answer = ""
    initialize_jira_task(state)
    state.tasks = collect_tasks()  # Ensure tasks are loaded into state
    state.answers = {}  # Initialize answers dictionary
    refresh_conversation(state)



load_dotenv()

threading.Thread(target=run_ask_llm_script, daemon=True).start()
gui = Gui(css_file="assets/styles.css", pages=pages)
conversation_partial = gui.add_partial("")
gui.run(
    on_init=on_init,
    port=5001,  # Change the port number here
    title="JIRA Assistant",
    dark_mode=True,
    use_reloader=True,
)

