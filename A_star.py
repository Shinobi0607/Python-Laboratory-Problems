import heapq

def a_star(graph, heuristics, start, goal):
    open_list = [(0, start)]
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0
    f_score = {node: float('inf') for node in graph}
    f_score[start] = heuristics[start]
    
    while open_list:
        current_f, current_node = heapq.heappop(open_list)
        
        if current_node == goal:
            path = []
            total_cost = g_score[current_node]
            while current_node in came_from:
                path.append(current_node)
                current_node = came_from[current_node]
            path.append(start)
            path.reverse()
            return path, total_cost
        
        for neighbor, cost in graph[current_node]:
            tentative_g = g_score[current_node] + cost
            
            if tentative_g < g_score[neighbor]:
                came_from[neighbor] = current_node
                g_score[neighbor] = tentative_g
                f_score[neighbor] = tentative_g + heuristics[neighbor]
                heapq.heappush(open_list, (f_score[neighbor], neighbor))

    return None, None

def main():
    graph = {}
    heuristics = {}
    
    vertices = int(input("Enter the number of vertices: "))
    
    for _ in range(vertices):
        vertex = int(input("Enter vertex: "))
        heuristic = float(input(f"Enter heuristic for vertex {vertex}: "))
        neighbors = int(input(f"Enter the number of neighbors for vertex {vertex}: "))
        
        edge_list = []
        for _ in range(neighbors):
            neighbor, cost = map(int, input(f"Enter neighbor and cost for vertex {vertex} (neighbor cost): ").split())
            edge_list.append((neighbor, cost))
        
        graph[vertex] = edge_list
        heuristics[vertex] = heuristic
    
    start = int(input("Enter the start vertex: "))
    goal = int(input("Enter the goal vertex: "))
    
    path, total_cost = a_star(graph, heuristics, start, goal)
    if path:
        print("Path found:", path)
        print("Total cost:", total_cost)
    else:
        print("No path found")

if __name__== "__main__":
     main()