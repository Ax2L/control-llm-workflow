import taipy.core as tp
from taipy import Config


print("hello")

if __name__ == "__main__":
    # Load the configuration
    Config.load("config.toml")  # Ensure this path is correct
    tp.Core().run()
    
    # Create and run the scenario
    scenario_cfg = Config.scenarios["llm_request_instruction"]  # Ensure "llm_chain" is defined in config.toml
    scenario = tp.create_scenario(scenario_cfg)
    tp.submit(scenario)
