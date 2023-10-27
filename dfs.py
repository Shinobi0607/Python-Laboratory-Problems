def dfs(visited, graph, node):
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

graph_input = {}
num_edges = int(input("Enter the number of edges: "))

for _ in range(num_edges):
    src_node, *adj_nodes = input("Enter source node and its adjacent nodes separated by spaces: ").split()
    graph_input[src_node] = adj_nodes

start_node = input("Enter the start node for DFS traversal: ")

graph = {key: value for key, value in graph_input.items()}

visited = set()

print("Following is the Depth-First Search:")
dfs(visited, graph, start_node)

