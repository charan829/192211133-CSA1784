import heapq
class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0 
        self.h = 0  
        self.f = 0  
    def __lt__(self, other):
        return self.f < other.f  
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1]) 
def a_star(start, goal, grid):
    open_list = []
    closed_list = set()
    start_node = Node(start)
    goal_node = Node(goal)
    heapq.heappush(open_list, start_node)
    while open_list:
        current_node = heapq.heappop(open_list)
        closed_list.add(current_node.position)
        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
        neighbors = [(0, 1), (1, 0), (0, -1), (-1, 0)]  
        for new_position in neighbors:
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])
            if (0 <= node_position[0] < len(grid)) and (0 <= node_position[1] < len(grid[0])) and grid[node_position[0]][node_position[1]] == 0:
                child_node = Node(node_position, current_node)
                if child_node.position in closed_list:
                    continue
                child_node.g = current_node.g + 1
                child_node.h = heuristic(child_node.position, goal_node.position)
                child_node.f = child_node.g + child_node.h
                if all(child_node.position != node.position or child_node.g < node.g for node in open_list):
                    heapq.heappush(open_list, child_node)
    return None  
if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0],
        [0, 0, 0, 0, 0]
    ]
    start = (0, 0)  
    goal = (4, 4)  
    path = a_star(start, goal, grid)
    if path:
        print("Path found:", path)
    else:
        print("No path found.")
