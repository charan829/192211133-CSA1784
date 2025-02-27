def dfs_iterative(graph, start_node):     
    if start_node not in graph:
        print("Error: Start node not found in graph.")
        return
    visited = set()  
    stack = [start_node]  
    print("DFS Traversal Order:")
    while stack:
        node = stack.pop()  
        if node not in visited:
            print(node, end=" ")
            visited.add(node)
            for neighbor in reversed(graph[node]):  
                if neighbor not in visited:
                    stack.append(neighbor)
    print() 
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F', 'G'],
    'D': ['B'],
    'E': ['B', 'H'],
    'F': ['C'],
    'G': ['C'],
    'H': ['E']
}
start_node = input("Enter the starting node: ").strip().upper()
dfs_iterative(graph, start_node)
