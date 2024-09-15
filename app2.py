import taipy as tp
from taipy.gui import notify, Gui, State
from taipy import Config
from modules.utils import log

state = State
Config.load("config.toml")

def main(scenario_name, config_path):
    log("Starting the application...")  # Log start
    # Load the configuration
    if not os.path.exists(config_path):
        log(f"Configuration file '{config_path}' not found.")
        print(f"Configuration file '{config_path}' not found.")
    else:
        try:
            log(f"Loading configuration from '{config_path}'...")
            Config.load(config_path)
            log("Configuration loaded successfully.")
            tp.Core().run()
            log("Core running.")
            
            # Create and run the scenario
            scenario_cfg = Config.scenarios.get(scenario_name)  # Changed llm_testt_benchmark to scenario_name
            if scenario_cfg is None:
                log(f"Scenario '{scenario_name}' not found in configuration.")
                print(f"Scenario '{scenario_name}' not found in configuration.")
            else:
                log(f"Creating and submitting scenario '{scenario_name}'...")
                scenario = tp.create_scenario(scenario_cfg)
                tp.submit(scenario)
                log(f"Scenario '{scenario_name}' submitted successfully.")
        except Exception as e:
            log(f"An error occurred: {e}")
            print(f"An error occurred: {e}")
    log("Application finished.")  # Log end



def on_init(state: State):
    log("Initializing application state.")  # Log start
    state.date = None
    state.selected_nodes = []
    state.selected_jobs = []
    state.selected_scenario = None  # Initialize scenario as None
    state.scenario = None
    log("Application state initialized.")  # Log end

def load_dynamic_scenario(state: State):
    log(f"Loading dynamic scenario for selected_scenario: {state.selected_scenario}")  # Log start
    scenario_cfg = Config.scenarios.get(state.selected_scenario)
    if scenario_cfg:
        state.scenario = tp.create_scenario(scenario_cfg)
        state.variables = scenario_cfg.variables
        state.jobs = scenario_cfg.jobs
        state.graph_data = scenario_cfg.graph_data
        log(f"Dynamic scenario loaded: {state.scenario}")  # Log end
    else:
        log(f"No scenario configuration found for: {state.selected_scenario}")

def on_data_node_change(state: State, var_name, var_value):
    log(f"on_data_node_change triggered with var_name={var_name}, var_value={var_value}")  # Log start
    state.selected_nodes = var_value
    notify(state, f"Selected data nodes updated: {state.selected_nodes}", "success")
    log(f"Data nodes updated: {state.selected_nodes}")  # Log end

def on_scenario_change(state: State, var_name, var_value):
    log(f"on_scenario_change triggered with var_name={var_name}, var_value={var_value}")  # Log start
    state.selected_scenario = var_value
    load_dynamic_scenario(state)
    notify(state, f"Scenario updated: {state.selected_scenario}", "success")
    log(f"Scenario updated: {state.selected_scenario}")  # Log end

root_md = """
<|navbar|>
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
<|layout|columns=300px 1|
<|part|
<|{scenario}|scenario_selector|on_change=on_scenario_change|>
|>
<|{scenario}|scenario|>
|>
<|Graph|expandable|
<|{scenario}|scenario_dag|show_toolbar=False|>
|>
<|layout|columns=300px 1|
<|part|
<|{scenario}|data_node_selector|on_change=on_data_node_change|>
|>
<|part|
<|{selected_nodes}|data_node|show_config=True|>
|>
|>
"""

Config.export("config_export.toml")

if __name__ == "__main__":
    try:
        log("Starting application...")  # Log start
        if selected_scenario:
            pass
    except Exception as e:
        selected_nodes = []
        selected_jobs = []
        date = None
        scenario = None
        selected_scenario = None
    pages = {"/": root_md, "Scenarios": scenario_configure_md, "Jobs": job_selector_md}
    tp.Core().run()
    gui = Gui(pages=pages)
    gui.run(
        on_init=on_init,
        port=5001,
        title="Scenario Dashboard",
        dark_mode=True,
        # use_reloader=True,
        # allow_unsafe_werkzeug=True,
        # async_mode="threading",
        # debug=True,
    )
    log("Application started successfully.")  # Log end

