class MapColoring:
    def __init__(self, graph, colors):
        self.graph = graph  
        self.colors = colors  
        self.color_assignment = {node: None for node in graph}  
    def is_safe(self, node, color):
        for neighbor in self.graph[node]:
            if self.color_assignment[neighbor] == color:
                return False
        return True
    def backtrack(self, node):
        if node == len(self.graph):
            return True
        current_node = list(self.graph.keys())[node]
        for color in self.colors:
            if self.is_safe(current_node, color):
                self.color_assignment[current_node] = color 
                if self.backtrack(node + 1):  
                    return True
                self.color_assignment[current_node] = None  
        return False  
    def solve(self):
        if self.backtrack(0):
            return self.color_assignment
        else:
            return None 
if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    colors = ['Red', 'Green', 'Blue']
    map_coloring = MapColoring(graph, colors)
    solution = map_coloring.solve()
    if solution:
        print("Color assignment:", solution)
    else:
        print("No solution found.")
