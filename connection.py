# connection.py

from netmiko import ConnectHandler
from netmiko.exceptions import NetmikoTimeoutException
from netmiko.exceptions import NetmikoAuthenticationException

from config import DEVICE


def connect_to_switch():
    """
    Connect to the Cisco switch using SSH.
    """

    try:
        print(f"Connecting to switch {DEVICE['host']}...")

        connection = ConnectHandler(**DEVICE)

        print("Connected to switch successfully!")

        return connection

    except NetmikoAuthenticationException:
        print("Authentication failed!")
        print("Check the username and password.")
        return None

    except NetmikoTimeoutException:
        print("Connection timed out!")
        print("Check the switch IP address and network connection.")
        return None

    except Exception as error:
        print(f"Unexpected error: {error}")
        return None


# Test the connection
if __name__ == "__main__":

    connection = connect_to_switch()

    if connection:

        # Run a simple Cisco command
        output = connection.send_command("show version")

        print("\n----- SWITCH OUTPUT -----")
        print(output)

        # Close SSH connection
        connection.disconnect()

        print("\nDisconnected from switch.")