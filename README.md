# Graph Pathfinder

An interactive graph visualizer that implements BFS, DFS, and Dijkstra's pathfinding algorithms. Build a custom graph and watch the algorithms traverse it in real time.

## Features
- Interactive graph builder via edge input
- BFS, DFS, and Dijkstra's algorithm support
- Color-coded visualization (start, end, path, visited, unvisited)
- Weighted and unweighted graph support
- Path length and traversal order stats

## Tech Stack
- Python
- NetworkX
- Matplotlib
- Streamlit

## Setup

1. Clone the repo
```
git clone https://github.com/sdjing/graph-visualizer.git
cd graph-visualizer
```

2. Install dependencies
```
pip install -r requirements.txt
```

3. Run the app
```
python -m streamlit run graph_app.py
```

## Usage
1. Enter edges in the sidebar as `A B` (unweighted) or `A B 5` (weighted)
2. Set your start and end nodes
3. Select an algorithm (BFS, DFS, Dijkstra)
4. Click **Find Path**
5. Green = start, Red = end, Orange = path, Gray = visited, Blue = unvisited
