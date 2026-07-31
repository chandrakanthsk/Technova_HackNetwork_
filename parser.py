# parser.py

import re


def parse_cdp_neighbors(output, local_device="Local-Switch"):
    """
    Convert Cisco 'show cdp neighbors' output
    into structured topology data.
    """

    neighbors = []

    lines = output.splitlines()

    for line in lines:

        # Ignore empty lines
        if not line.strip():
            continue

        # Ignore headings
        if "Device ID" in line:
            continue

        if "Capability Codes" in line:
            continue

        # Split using multiple spaces
        parts = re.split(r"\s{2,}", line.strip())

        # Typical CDP row contains multiple columns
        if len(parts) >= 5:

            try:
                remote_device = parts[0]

                local_port = parts[1]

                remote_port = parts[-1]

                neighbors.append({
                    "local_device": local_device,
                    "remote_device": remote_device,
                    "local_port": local_port,
                    "remote_port": remote_port
                })

            except Exception:
                continue

    return neighbors


# -------------------------
# TEST
# -------------------------

if __name__ == "__main__":

    sample_output = """
Device ID        Local Intrfce     Holdtme    Capability  Platform  Port ID

Switch-1         Gig 0/1           122        S I         2960      Gig 0/1
Switch-2         Gig 0/2           131        S I         2960      Gig 0/1
Router-1         Gig 0/3           145        R S I       ISR4321   Gig 0/0
"""

    result = parse_cdp_neighbors(
        sample_output,
        "Core-Switch"
    )

    print("\n===== PARSED CDP DATA =====")

    for neighbor in result:
        print(neighbor)