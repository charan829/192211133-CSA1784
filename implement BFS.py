from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        if v not in self.graph:
            self.graph[v] = []
        self.graph[u].append(v)
        self.graph[v].append(u) 

    def bfs(self, start):
        visited = set() 
        queue = deque([start]) 
        visited.add(start)

        while queue:
            node = queue.popleft()  
            print(node, end=' ') 
            for neighbor in self.graph.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(3, 6)
    g.add_edge(4, 7)

    print("BFS starting from node 0:")
    g.bfs(0)
