from collections import deque
initial_state = (3, 3, 1, 0, 0)
goal_state = (0, 0, 0, 3, 3)
moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
def is_valid(state):
    """ Check if the state is valid (no side has more cannibals than missionaries) """
    m_left, c_left, _, m_right, c_right = state
    if (m_left < c_left and m_left > 0) or (m_right < c_right and m_right > 0):
        return False
    if any(x < 0 or x > 3 for x in [m_left, c_left, m_right, c_right]):
        return False
    return True
def get_next_states(state):
    """ Generate all possible valid states from the current state """
    next_states = []
    m_left, c_left, boat, m_right, c_right = state
    if boat == 1:
        for m, c in moves:
            new_state = (m_left - m, c_left - c, 0, m_right + m, c_right + c)
            if is_valid(new_state):
                next_states.append(new_state)
    else:  
        for m, c in moves:
            new_state = (m_left + m, c_left + c, 1, m_right - m, c_right - c)
            if is_valid(new_state):
                next_states.append(new_state)
    return next_states
def bfs():
    """ Perform BFS to find the solution """
    queue = deque([(initial_state, [])])
    visited = set()
    while queue:
        state, path = queue.popleft()
        if state in visited:
            continue
        visited.add(state)
        if state == goal_state:
            return path + [state]
        for next_state in get_next_states(state):
            queue.append((next_state, path + [state]))
    return None
solution = bfs()
if solution:
    print("Solution found! Steps:")
    for step in solution:
        print(step)
else:
    print("No solution found.")
