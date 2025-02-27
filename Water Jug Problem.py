from collections import deque
def water_jug_problem(capacity_a, capacity_b, target):
    queue = deque()
    visited = set()
    initial_state = (0, 0)
    queue.append(initial_state)
    visited.add(initial_state)
    while queue:
        a, b = queue.popleft() 
        if a == target or b == target or a + b == target:
            return True
        possible_states = [
            (capacity_a, b),
            (a, capacity_b),  
            (0, b),           
            (a, 0),          
            (min(a + b, capacity_a), max(0, b - (capacity_a - a))), 
            (max(0, a - (capacity_b - b)), min(a + b, capacity_b))  
        ]
        for state in possible_states:
            if state not in visited:
                visited.add(state)
                queue.append(state)
    return False  
if __name__ == "__main__":
    capacity_a = 4 
    capacity_b = 3 
    target = 2     
    if water_jug_problem(capacity_a, capacity_b, target):
        print(f"It is possible to measure {target} liters using the jugs.")
    else:
        print(f"It is not possible to measure {target} liters using the jugs.")
