# compare.py


def connection_key(connection):
    """
    Convert a connection dictionary into a tuple
    so that it can be compared easily.
    """

    return (
        connection["local_device"],
        connection["remote_device"],
        connection["local_port"],
        connection["remote_port"]
    )


def compare_topologies(baseline, current):
    """
    Compare baseline topology with current topology.

    Detect:
    1. New connections
    2. Removed connections
    """

    baseline_connections = {
        connection_key(item) for item in baseline
    }

    current_connections = {
        connection_key(item) for item in current
    }

    # Connections present now but not in baseline
    added = current_connections - baseline_connections

    # Connections present in baseline but missing now
    removed = baseline_connections - current_connections

    return {
        "added": list(added),
        "removed": list(removed)
    }


def display_changes(changes):

    print("\n===== TOPOLOGY CHANGE REPORT =====")

    if not changes["added"] and not changes["removed"]:
        print("No topology changes detected.")
        return

    for connection in changes["added"]:

        local_device, remote_device, local_port, remote_port = connection

        print(
            f"[NEW CONNECTION] "
            f"{local_device} ({local_port}) "
            f"<--> {remote_device} ({remote_port})"
        )

    for connection in changes["removed"]:

        local_device, remote_device, local_port, remote_port = connection

        print(
            f"[REMOVED CONNECTION] "
            f"{local_device} ({local_port}) "
            f"<--> {remote_device} ({remote_port})"
        )


# Test
if __name__ == "__main__":

    baseline = [
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
        }
    ]

    # Imagine someone removed Switch-2
    # and connected an unknown switch.
    current = [
        {
            "local_device": "Core-Switch",
            "remote_device": "Switch-1",
            "local_port": "Gi0/1",
            "remote_port": "Gi0/1"
        },
        {
            "local_device": "Core-Switch",
            "remote_device": "Unknown-Switch",
            "local_port": "Gi0/2",
            "remote_port": "Gi0/1"
        }
    ]

    changes = compare_topologies(baseline, current)

    display_changes(changes)