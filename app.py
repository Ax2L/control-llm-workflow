# WebUI Taipy App for Scenario workflows management
import taipy.core as tp
from taipy import Config
import os
import argparse  # Import argparse for command-line arguments
from modules.utils import log  # Import the log function

config_path = "workflows/config.toml"

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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Taipy Scenario")
    parser.add_argument("-s", "--scenario", type=str, default="llm_ollama_instruction", help="Scenario name to run")
    parser.add_argument("-c", "--config", type=str, default="workflows/config.toml", help="Config file path")
    args = parser.parse_args()
    main(args.scenario, args.config)

