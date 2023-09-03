# Importing required modules
from itertools import product
from typing import List, Dict
import random
import pandas as pd

# Defining the function
def generate_configurations(
    default_values: Dict, varying_values: Dict
) -> List[Dict]:
    """
    Generate a list of configuration dictionaries based on default values and varying values.

    Parameters:
        default_values: Dictionary containing the default values for the configuration keys.
        varying_values: Dictionary containing lists of varying values for specific configuration keys.

    Returns:
        A list of configuration dictionaries.
    """

    # Extract keys and values for varying parameters
    varying_keys = list(varying_values.keys())
    varying_values_lists = [varying_values[key] for key in varying_keys]

    configs = []

    # Generate all combinations of varying values
    for values_combo in product(*varying_values_lists):
        new_config = default_values.copy()
        for key, value in zip(varying_keys, values_combo):
            new_config[key] = value
        configs.append(new_config.copy())

    return configs

# Wrapping the code inside if __name__ == "__main__":
if __name__ == "__main__":
    # Default values
    default_values = {
        "temp": 300.0,
        "press": 1.0,
        "press_ratio": None,
        "time_step": 1.0,
        "intel": "auto",
        "opt": "auto",
        "omp": 30,
        "mpi": 30,
        "gpu": 0,
        "packing_steps": [20000, 1000000, 1000000],
        "packing_time_step": [0.1, 1.0, 1.0],
    }

    # Varying values
    varying_values = {
        "num_atoms": [300, 500, 700, 1000],
        "chain_num": [5, 7, 10],
        "ini_dens": [0.05, 0.1, 0.2, 0.3, 0.6],
        "max_temp": [400, 500, 600, 700],
        "max_press": [1000, 3000, 5000, 10000, 30000, 50000],
        "step_list": [0, 0.05, 0.1, 0.2, 0.3],
        "eq_step": [1, 3, 5, 7, 10],
    }

    # Example usage:
    configurations = generate_configurations(
         default_values, varying_values
    )

    # Show the first 5 configurations for illustration
    sampled_configs = random.sample(configurations, 100)
    print(pd.DataFrame(sampled_configs).head(5))
    #pd.DataFrame(sampled_configs).iloc[5].to_dict()
