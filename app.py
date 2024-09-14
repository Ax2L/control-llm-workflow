# WebUI Taipy App for Scenario workflows management
import taipy.core as tp
from taipy import Config
import os
from modules.utils import log  # Import the log function

config_path = "config.toml"

if __name__ == "__main__":
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
            scenario_cfg = Config.scenarios.get("llm_ollama_instruction")
            if scenario_cfg is None:
                log("Scenario 'llm_ollama_instruction' not found in configuration.")
                print("Scenario 'llm_ollama_instruction' not found in configuration.")
            else:
                log("Creating and submitting scenario 'llm_ollama_instruction'...")
                scenario = tp.create_scenario(scenario_cfg)
                tp.submit(scenario)
                log("Scenario 'llm_ollama_instruction' submitted successfully.")
        except Exception as e:
            log(f"An error occurred: {e}")
            print(f"An error occurred: {e}")
    log("Application finished.")  # Log end

