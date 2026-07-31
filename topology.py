# topology.py

import networkx as nx


def build_topology(neighbors):
    """
    Build a network topology graph
    from discovered neighbor information.
    """

    graph = nx.Graph()

    for neighbor in neighbors:

        local_device = neighbor["local_device"]
        remote_device = neighbor["remote_device"]
        local_port = neighbor["local_port"]
        remote_port = neighbor["remote_port"]

        # Add devices
        graph.add_node(local_device)
        graph.add_node(remote_device)

        # Add connection
        graph.add_edge(
            local_device,
            remote_device,
            local_port=local_port,
            remote_port=remote_port
        )

    return graph


def display_topology(graph):

    print("\n===== CURRENT NETWORK TOPOLOGY =====")

    for device1, device2, data in graph.edges(data=True):

        print(
            f"{device1} ({data['local_port']}) "
            f"<----> "
            f"{device2} ({data['remote_port']})"
        )


# Test using sample network data
if __name__ == "__main__":

    sample_neighbors = [
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

    topology = build_topology(sample_neighbors)

    display_topology(topology)