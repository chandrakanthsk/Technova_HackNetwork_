# baseline.py

import json
import os
from config import BASELINE_FILE


def save_baseline(neighbors):
    """
    Save the expected network topology to baseline.json.
    """

    try:
        with open(BASELINE_FILE, "w") as file:
            json.dump(neighbors, file, indent=4)

        print(f"Baseline saved successfully to {BASELINE_FILE}")

    except Exception as error:
        print(f"Error saving baseline: {error}")


def load_baseline():
    """
    Load the saved baseline topology.
    """

    if not os.path.exists(BASELINE_FILE):
        print("Baseline file does not exist.")
        return None

    try:
        with open(BASELINE_FILE, "r") as file:
            baseline = json.load(file)

        return baseline

    except Exception as error:
        print(f"Error loading baseline: {error}")
        return None


def baseline_exists():
    """
    Check whether a baseline already exists.
    """

    if not os.path.exists(BASELINE_FILE):
        return False

    return os.path.getsize(BASELINE_FILE) > 0


# Test
if __name__ == "__main__":

    sample_topology = [
        {
            "local_device": "Core-Switch",
            "remote_device": "Switch-1",
            "local_port": "Gi0/1",
            "remote_port": "Gi0/1"
        },
        {
            "local_device": "Core-Switch",
            "remote_device": "Switch-2",
            "local_port": "Gi0/2",
            "remote_port": "Gi0/1"
        },
        {
            "local_device": "Switch-1",
            "remote_device": "Server-1",
            "local_port": "Gi0/2",
            "remote_port": "Eth0"
        }
    ]

    save_baseline(sample_topology)

    print("\nSaved Baseline:")

    baseline = load_baseline()

    print(baseline)