import taipy as tp
from taipy.gui import notify, Gui, State, navigate
from taipy import Config
import pandas as pd
import datetime as dt
import os
from modules.utils import log

Config.load("config.toml")  # Updated to use config.toml

try:
    if selected_nodes:
        pass
except:
    date = None
    scenario = None
    selected_nodes = []
    selected_jobs = []


def on_init(state: State):
    log("Initializing application state.")
    state.date = None
    state.selected_nodes = []  # Initialize selected_nodes


def on_data_node_change(state: State, var_name, var_value):
    log(
        f"on_data_node_change triggered with var_name={var_name}, var_value={var_value}"
    )
    state.selected_nodes = var_value
    notify(state, f"Selected data nodes updated: {state.selected_nodes}", "success")


root_md = """
<|navbar|>
"""

job_selector_md = """
<|layout|columns=1|fullheight|
<|{selected_jobs}|job_selector|>
|>
"""

data_node_view_md = """
<|layout|columns=300px 1|class_name=context_container|
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
<|part|class_name=scenario_selector_container|
<|{scenario}|scenario_selector|align_item_bottom|>
|>
<|{scenario}|scenario|>
<|{scenario}|scenario_dag|show_toolbar=False|class_name=graph_container|>
|>
"""

def on_menu(state, action, info):
    page = info["args"][0]
    navigate(state, to=page)


pages = {"/": root_md, "Scenarios": scenario_configure_md, "Data": data_node_view_md, "Jobs": job_selector_md}


gui = Gui(css_file="modules/styles.css", pages=pages)
gui.run(
    on_init=on_init,
    port=5001,
    title="Scenario Dashboard",
    dark_mode=True,
    use_reloader=True,
    allow_unsafe_werkzeug=True,
    async_mode="threading",
    debug=True,
)
