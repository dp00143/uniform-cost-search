from dataStruct import Node, Graph
from pprint import pprint


def buildGraph(f_name):
    g = Graph()
    with open(f_name) as f:
        number_of_nodes = int(f.readline().strip())
        for node in range(0, number_of_nodes):
            node_id = f.readline().strip()
            n = Node(node_id)
            g.nodes[node_id] = n

        number_of_edges = int(f.readline().strip())
        for edge in range(0, number_of_edges):
            node1, node2, distance = f.readline().strip().split(" ")
            # As the graph is bidirectional, we need to add this connection to both nodes
            g.nodes[node1].addNeighbour(node2, distance)
            g.nodes[node2].addNeighbour(node1, distance)
    return g


if __name__ == '__main__':
    graph = buildGraph()
    pprint(graph.nodes)
