import matplotlib.pyplot as plt
import networkx as nx


def draw_graph(G, path=[], visited=[]):
    fig, ax = plt.subplots(figsize=(8, 5))
    pos = nx.spring_layout(G, seed=42)

    node_colors = []
    for node in G.nodes():
        if path and node == path[0]:
            node_colors.append("#2ecc71")   # start — green
        elif path and node == path[-1]:
            node_colors.append("#e74c3c")   # end — red
        elif node in path:
            node_colors.append("#f39c12")   # on path — orange
        elif node in visited:
            node_colors.append("#95a5a6")   # visited — gray
        else:
            node_colors.append("#3498db")   # unvisited — blue

    path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
    other_edges = [e for e in G.edges() if e not in path_edges and (e[1], e[0]) not in path_edges]

    nx.draw_networkx_nodes(G, pos, node_color=node_colors, node_size=600, ax=ax)
    nx.draw_networkx_labels(G, pos, ax=ax, font_color="white", font_weight="bold")
    nx.draw_networkx_edges(G, pos, edgelist=other_edges, ax=ax, edge_color="#bdc3c7", width=1.5)
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, ax=ax, edge_color="#f39c12", width=3)

    edge_labels = nx.get_edge_attributes(G, "weight")
    if any(v != 1 for v in edge_labels.values()):
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, ax=ax)

    ax.axis("off")
    plt.tight_layout()
    return fig