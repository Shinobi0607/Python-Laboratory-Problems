graph = {
    "S": {"A": 1, "B": 3, "C": 5},
    "A": {"G": 3},
    "B": {"F": 5},
    "C": {"E": 2},
    "E": {"Dest": 1},
}

import heapq

def ucs(graph, start, goal):
    queue = [(0, start, [])]
    visited = set()

    while queue:
        cost, node, path = heapq.heappop(queue)

        if node in visited:
            continue

        path = path + [node]
        if node == goal:
            return path

        visited.add(node)

        for neighbor, neighbor_cost in graph.get(node, {}).items():
            if neighbor not in visited:
                heapq.heappush(queue, (cost + neighbor_cost, neighbor, path))

    return None

start_node = "S"
end_node = "Dest"

result = ucs(graph, start_node, end_node)
if result:
    print(f"Shortest path from {start_node} to {end_node}: {result}")
else:
    print(f"No path found from {start_node} to {end_node}.")





