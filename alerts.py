# alerts.py

from datetime import datetime


def create_alert(event):
    """
    Create an alert message from a topology change event.
    """

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    message = (
        f"\n===== NETWORK TOPOLOGY ALERT =====\n"
        f"Time        : {timestamp}\n"
        f"Risk Level  : {event['risk']}\n"
        f"Change Type : {event['change_type']}\n"
        f"Device      : {event['remote_device']}\n"
        f"Connection  : {event['local_device']} "
        f"({event['local_port']}) <--> "
        f"{event['remote_device']} "
        f"({event['remote_port']})\n"
    )

    return message


def send_alert(event):
    """
    Send an alert based on risk level.
    """

    message = create_alert(event)

    if event["risk"] == "HIGH":
        print("\n!!! HIGH RISK ALERT !!!")
        print(message)

    elif event["risk"] == "MEDIUM":
        print("\n!! MEDIUM RISK ALERT !!")
        print(message)

    else:
        print("\nLOW RISK EVENT")
        print(message)


# Test
if __name__ == "__main__":

    sample_event = {
        "change_type": "NEW CONNECTION",
        "local_device": "Core-Switch",
        "remote_device": "Unknown-Switch",
        "local_port": "Gi0/2",
        "remote_port": "Gi0/1",
        "risk": "HIGH"
    }

    send_alert(sample_event)