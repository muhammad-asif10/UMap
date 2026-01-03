import matplotlib.pyplot as plt
import networkx as nx

def draw_graph_path(graph, path):
    G = nx.Graph()

    for node, neighbors in graph.adjacency_list.items():
        for neighbor, weight in neighbors:
            G.add_edge(node, neighbor, weight=weight)

    pos = nx.spring_layout(G, seed=42)

    nx.draw(G, pos, with_labels=True, node_size=1500)
    path_edges = list(zip(path, path[1:]))

    nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3)
    plt.show()
