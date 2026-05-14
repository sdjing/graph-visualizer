import networkx as nx
from collections import deque


def build_graph(edges, weighted=False):
    G = nx.Graph()
    for edge in edges:
        if weighted and len(edge) == 3:
            G.add_edge(edge[0], edge[1], weight=edge[2])
        else:
            G.add_edge(edge[0], edge[1], weight=1)
    return G


def bfs(G, start, end):
    visited = []
    queue = deque([[start]])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node in visited:
            continue
        visited.append(node)

        if node == end:
            return path, visited

        for neighbor in G.neighbors(node):
            queue.append(path + [neighbor])

    return [], visited


def dfs(G, start, end):
    visited = []
    stack = [[start]]

    while stack:
        path = stack.pop()
        node = path[-1]

        if node in visited:
            continue
        visited.append(node)

        if node == end:
            return path, visited

        for neighbor in G.neighbors(node):
            stack.append(path + [neighbor])

    return [], visited


def dijkstra(G, start, end):
    try:
        path = nx.dijkstra_path(G, start, end, weight="weight")
        visited = list(nx.single_source_dijkstra_path(G, start).keys())
        return path, visited
    except nx.NetworkXNoPath:
        return [], []