# risk.py


def classify_device(device_name):
    """
    Classify risk based on the type/name of device.
    """

    name = device_name.lower()

    # HIGH RISK
    if "unknown" in name:
        return "HIGH"

    if "switch" in name:
        return "HIGH"

    if "server" in name:
        return "HIGH"

    # MEDIUM RISK
    if "router" in name:
        return "MEDIUM"

    if "firewall" in name:
        return "MEDIUM"

    # LOW RISK
    if "laptop" in name:
        return "LOW"

    if "pc" in name:
        return "LOW"

    if "printer" in name:
        return "LOW"

    # If device type is not recognized
    return "MEDIUM"


def classify_changes(changes):
    """
    Classify topology changes by risk level.
    """

    results = []

    # Check newly added connections
    for connection in changes["added"]:

        local_device, remote_device, local_port, remote_port = connection

        risk = classify_device(remote_device)

        results.append({
            "change_type": "NEW CONNECTION",
            "local_device": local_device,
            "remote_device": remote_device,
            "local_port": local_port,
            "remote_port": remote_port,
            "risk": risk
        })

    # Check removed connections
    for connection in changes["removed"]:

        local_device, remote_device, local_port, remote_port = connection

        risk = classify_device(remote_device)

        results.append({
            "change_type": "REMOVED CONNECTION",
            "local_device": local_device,
            "remote_device": remote_device,
            "local_port": local_port,
            "remote_port": remote_port,
            "risk": risk
        })

    return results


def display_risk_report(results):
    """
    Display risk classification results.
    """

    print("\n===== RISK CLASSIFICATION REPORT =====")

    if not results:
        print("No changes detected.")
        return

    for event in results:

        print("\n-----------------------------")

        print(f"Change : {event['change_type']}")
        print(f"Device : {event['remote_device']}")
        print(
            f"Link   : {event['local_device']} "
            f"{event['local_port']} <--> "
            f"{event['remote_device']} "
            f"{event['remote_port']}"
        )

        print(f"Risk   : {event['risk']}")


# Test
if __name__ == "__main__":

    sample_changes = {

        "added": [
            (
                "Core-Switch",
                "Unknown-Switch",
                "Gi0/2",
                "Gi0/1"
            ),

            (
                "Access-Switch",
                "Laptop-10",
                "Gi0/10",
                "Eth0"
            )
        ],

        "removed": [
            (
                "Core-Switch",
                "Server-1",
                "Gi0/5",
                "Eth0"
            )
        ]
    }

    results = classify_changes(sample_changes)

    display_risk_report(results)