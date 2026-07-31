# discovery.py

from connection import connect_to_switch


def discover_neighbors():
    """
    Collect CDP and LLDP neighbor information
    from the Cisco switch.
    """

    connection = connect_to_switch()

    if connection is None:
        print("Unable to connect to the switch.")
        return None

    try:
        print("\nCollecting CDP neighbor information...")

        cdp_output = connection.send_command(
            "show cdp neighbors detail"
        )

        print("\nCollecting LLDP neighbor information...")

        lldp_output = connection.send_command(
            "show lldp neighbors detail"
        )

        return {
            "cdp": cdp_output,
            "lldp": lldp_output
        }

    except Exception as error:
        print(f"Discovery error: {error}")
        return None

    finally:
        connection.disconnect()
        print("\nDisconnected from switch.")


if __name__ == "__main__":

    neighbors = discover_neighbors()

    if neighbors:

        print("\n========== CDP NEIGHBORS ==========")
        print(neighbors["cdp"])

        print("\n========== LLDP NEIGHBORS ==========")
        print(neighbors["lldp"])