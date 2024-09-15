import taipy as tp
from taipy.gui import notify, Gui, State
from taipy import Config
import pandas as pd
import datetime as dt
import os
from modules.utils import log

Config.load('config.toml')  # Updated to use config.toml

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
    log(f"on_data_node_change triggered with var_name={var_name}, var_value={var_value}")
    state.selected_nodes = var_value
    notify(state, f"Selected data nodes updated: {state.selected_nodes}", "success")

html = """
<|layout|columns=150px auto|
<|{scenario}|scenario_selector|>
<|part|
<|layout|columns=450px auto|
<|{scenario}|scenario|>
<|part|
<|{scenario}|scenario_dag|>
|>
|>
|>
|>
<|{selected_jobs}|job_selector|>
<|layout|columns=1 1|
<|{scenario}|data_node_selector|on_change=on_data_node_change|>
<|{selected_nodes}|data_node|>
|>
"""

gui = Gui(page=html)
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

