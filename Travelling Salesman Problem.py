from itertools import permutations
def calculate_cost(graph, path):
    cost = 0
    for i in range(len(path) - 1):
        cost += graph[path[i]][path[i + 1]]
    cost += graph[path[-1]][path[0]] 
    return cost
def tsp_brute_force(graph):
    n = len(graph)
    cities = list(range(n))  
    min_cost = float("inf")
    best_path = None
    for perm in permutations(cities[1:]):
        path = [0] + list(perm)  
        cost = calculate_cost(graph, path)
        if cost < min_cost:
            min_cost = cost
            best_path = path
    return best_path, min_cost
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
best_path, min_cost = tsp_brute_force(graph)
print("Best Route:", best_path + [best_path[0]])  
print("Minimum Cost:", min_cost)
