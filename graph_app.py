import streamlit as st
from graph import build_graph, bfs, dfs, dijkstra
from visualizer import draw_graph

st.set_page_config(page_title="Graph Pathfinder", layout="centered")
st.title("Graph Pathfinder")
st.caption("Build a graph and visualize BFS, DFS, or Dijkstra's algorithm.")

with st.sidebar:
    st.header("Graph Builder")
    st.markdown("Enter edges one per line as `A B` or `A B 5` for weighted.")
    edge_input = st.text_area("Edges", value="A B\nA C\nB D\nC D\nD E\nB E")
    weighted = st.checkbox("Weighted graph")
    algorithm = st.selectbox("Algorithm", ["BFS", "DFS", "Dijkstra"])
    start_node = st.text_input("Start node", value="A")
    end_node = st.text_input("End node", value="E")
    run = st.button("Find Path", type="primary")

def parse_edges(raw, weighted):
    edges = []
    for line in raw.strip().split("\n"):
        parts = line.strip().split()
        if len(parts) == 2:
            edges.append((parts[0], parts[1]))
        elif len(parts) == 3 and weighted:
            edges.append((parts[0], parts[1], int(parts[2])))
    return edges

if run:
    edges = parse_edges(edge_input, weighted)

    if not edges:
        st.error("No valid edges found. Check your input.")
        st.stop()

    G = build_graph(edges, weighted)

    if start_node not in G.nodes():
        st.error(f"Start node '{start_node}' not in graph.")
        st.stop()

    if end_node not in G.nodes():
        st.error(f"End node '{end_node}' not in graph.")
        st.stop()

    if algorithm == "BFS":
        path, visited = bfs(G, start_node, end_node)
    elif algorithm == "DFS":
        path, visited = dfs(G, start_node, end_node)
    else:
        path, visited = dijkstra(G, start_node, end_node)

    fig = draw_graph(G, path, visited)
    st.pyplot(fig)

    if path:
        st.success(f"Path found: {' → '.join(path)}")
        col1, col2 = st.columns(2)
        col1.metric("Path Length", len(path) - 1)
        col2.metric("Nodes Visited", len(visited))
        st.markdown(f"**Traversal order:** {' → '.join(visited)}")
    else:
        st.warning("No path found between the selected nodes.")
else:
    G = build_graph(parse_edges("A B\nA C\nB D\nC D\nD E\nB E", False))
    fig = draw_graph(G)
    st.pyplot(fig)
    st.info("Set your start and end nodes in the sidebar and click Find Path.")