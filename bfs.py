def bfs(graph, start_node):
    visited = [] 
    queue = [start_node]  

    while queue:
        s = queue.pop(0)  
        if s not in visited:  
            print(s, end=" ")  
            visited.append(s)  

            for neighbour in graph[s]: 
                if neighbour not in visited:  
                    queue.append(neighbour)  


graph_input = {}
num_edges = int(input("Enter the number of edges: "))

for _ in range(num_edges):
    src_node, *adj_nodes = input("Enter source node and its adjacent nodes separated by spaces: ").split()
    graph_input[src_node] = adj_nodes

start_node = input("Enter the start node for BFS traversal: ")

bfs(graph_input, start_node)

