import taipy as tp
from taipy.gui import notify, Gui, State
from taipy import Config
import pandas as pd
import datetime as dt
import os
from modules.utils import log

# Removed load_toml_files function

def load_scenarios(state: State):
    log("Loading scenarios.")
    tp.Core().stop()
    Config.load('config.toml')  # Updated to use config.toml
    scenarios = list(Config.scenarios.keys())
    log(f"Loaded scenarios: {scenarios}")
    return scenarios

def on_toml_change(state: State, var_name, var_value):
    log(f"on_toml_change triggered with var_name={var_name}, var_value={var_value}")
    try:
        tp.Core().stop()
        Config.load('config.toml')  # Updated to use config.toml
        state.scenarios = list(Config.scenarios.keys())
        state.selected_scenario = state.scenarios[0] if state.scenarios else None
        state.variables = []
        state.jobs = []
        state.graph_data = {}
        notify(state, f"Loaded scenarios from config.toml", "success")
        if state.selected_scenario:
            on_scenario_change(state, 'selected_scenario', state.selected_scenario)
    except Exception as e:
        log(f"Error loading scenarios: {str(e)}")
        notify(state, f"Error loading scenarios: {str(e)}", "error")

def on_scenario_change(state: State, var_name, var_value):
    log(f"on_scenario_change triggered with var_name={var_name}, var_value={var_value}")
    try:
        state.selected_scenario = var_value
        scenario_cfg = Config.scenarios[state.selected_scenario]
        if scenario_cfg:
            state.tasks = scenario_cfg.tasks
            log(f"state.variables: {str(state.variables)}")
            state.variables = collect_variables_from_tasks(state.tasks)
            state.dynamic_controls = generate_dynamic_controls(state.variables)
            notify(state, f"Scenario '{state.selected_scenario}' loaded successfully!", "success")
        else:
            log(f"No scenario configuration found for {state.selected_scenario}")
            notify(state, f"No scenario configuration found for {state.selected_scenario}", "error")
    except Exception as e:
        log(f"Error changing scenario: {str(e)}")
        notify(state, f"Error changing scenario: {str(e)}", "error")

def generate_dynamic_controls(variables):
    pass
    log("Generating dynamic controls.")
    controls = []
    for var in variables:
        if isinstance(var, bool):
            controls.append(f'<|{var}|toggle|label={var}|>')
        elif isinstance(var, list):
            controls.append(f'<|{var}|list|label={var}|>')
        elif isinstance(var, (int, float)):
            controls.append(f'<|{var}|input|type=number|label={var}|>')
        else:
            controls.append(f'<|{var}|input|label={var}|>')
    return "\n".join(controls)

def collect_variables_from_tasks(tasks):
    pass
    log(f"Collecting variables from tasks: {tasks}")
    variables = []
    for task_name in tasks:
        log(f"Processing task: {task_name}")
        task_cfg = Config.tasks.get(task_name)
        if task_cfg:
            log(f"Found task configuration for: {task_name}")
            input_data_nodes = task_cfg.inputs
            if not input_data_nodes:
                log(f"No input data nodes for task {task_name}, skipping.")
                continue
            log(f"Input data nodes for task {task_name}: {input_data_nodes}")
            for data_node_name in input_data_nodes:
                log(f"Processing data node: {data_node_name}")
                data_node_cfg = Config.data_nodes.get(data_node_name)
                if data_node_cfg:
                    log(f"Found data node configuration for: {data_node_name}")
                    variables.append(data_node_cfg.get('name', data_node_name))
                    log(f"Added variable: {data_node_cfg.get('name', data_node_name)}")
                else:
                    log(f"No configuration found for data node: {data_node_name}")
        else:
            log(f"No task configuration found for: {task_name}")
    log(f"Collected variables: {variables}")
    return variables

def execute_scenario(state: State):
    log(f"Executing scenario: {state.selected_scenario}")
    try:
        if state.selected_scenario:
            scenario_cfg = Config.scenarios.get(state.selected_scenario)
            scenario = tp.create_scenario(scenario_cfg)
            tp.submit(scenario)
            notify(state, f"Scenario '{state.selected_scenario}' executed successfully!", "success")
    except Exception as e:
        log(f"Error executing scenario: {str(e)}")
        notify(state, f"Error executing scenario: {str(e)}", "error")

Config.load('config.toml')  # Updated to use config.toml

def save(state: State):
    log("Saving scenario data.")
    state.scenario.historical_temperature.write(data)
    state.scenario.date_to_forecast.write(state.date)
    state.refresh('scenario')
    notify(state, "Saved! Ready to submit", "success")

def load_dynamic_scenario(state: State):
    log(f"Loading dynamic scenario: {state.selected_scenario}")
    scenario_cfg = Config.scenarios.get(state.selected_scenario)
    if scenario_cfg:
        state.scenario = tp.create_scenario(scenario_cfg)
        state.variables = scenario_cfg.get('variables', [])
        state.jobs = scenario_cfg.get('jobs', [])
        state.graph_data = scenario_cfg.get('graph_data', {})


def on_data_node_change(state: State, var_name, var_value):
    log(f"on_data_node_change triggered with var_name={var_name}, var_value={var_value}")  # Log start
    state.selected_nodes = var_value
    notify(state, f"Selected data nodes updated: {state.selected_nodes}", "success")
    log(f"Data nodes updated: {state.selected_nodes}")  # Log end


root_md = """
"""

job_selector_md = """
<|layout|columns=1|
<|{selected_jobs}|job_selector|>
|>
"""

data_node_view_md = """
<|layout|columns=300px 1|
<|part|
<|{scenario}|data_node_selector|on_change=on_data_node_change|>
|>
<|part|
<|{selected_nodes}|data_node|show_config=True|>
|>
|>
"""

scenario_configure_md = """
<|Jobs|expandable|expanded=False|
<|{selected_jobs}|job_selector|>
|>

<|part|class_name=card card-bg data_scenario_view|
<|### Scenarios|text|mode=markdown|>
<|layout|columns=300px 1|
<|part|
<|{scenario}|scenario_selector|on_change=on_scenario_change|>
|>
<|{scenario}|scenario|>
|>
|>


<|part|class_name=card card-bg data_node_view|
<|## Data Nodes|text|mode=markdown|>
<|layout|columns=300px 1|
<|part|
<|{scenario}|data_node_selector|height="150vh"|show_pins=False|on_change=on_data_node_change|>
|>
<|part|
<|{selected_nodes}|data_node|show_config=True|>
|>
|>
|>

<|Scenario Graph|expandable|class_name=graph_container|
<|{scenario}|scenario_dag|show_toolbar=False|>
|>
"""




try:
    if graph_data:
        pass
except:
    selected_toml = None
    selected_scenario = None
    scenario = None
    scenarios = None
    variables = []
    jobs = []
    graph_data = {}
    date = None
    tasks = []
    dynamic_controls = None
    selected_nodes = []
    
def on_init(state: State):
    log("Initializing application state.")
    state.selected_toml = 'config.toml'  # Set to config.toml
    state.scenarios = load_scenarios(state)
    state.variables = []
    state.tasks = []
    state.jobs = []
    state.graph_data = {}
    state.date = None
    state.scenario = None
    state.dynamic_controls = ""
    state.selected_nodes = []
    if state.selected_scenario:
        on_scenario_change(state, 'selected_scenario', state.selected_scenario)

pages = {"/": root_md, "Scenarios": scenario_configure_md, "Jobs": job_selector_md}
gui = Gui(css_file="modules/styles.css", pages=pages)
gui.run(
    on_init=on_init,
    port=5001,
    title="Scenario Dashboard",
    dark_mode=True,
    use_reloader=True,
    allow_unsafe_werkzeug=True,
    async_mode='threading',
    debug=True,
)