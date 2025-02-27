from collections import deque
def is_valid(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols
def vacuum_cleaner(grid, start_x, start_y):
    rows, cols = len(grid), len(grid[0])
    moves = [(0, 1), (0, -1), (1, 0), (-1, 0)]  
    visited = set()
    queue = deque([(start_x, start_y, 0)])  
    print("\nCleaning process starts...\n")
    while queue:
        x, y, steps = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        print(f"Step {steps}: Vacuum at ({x}, {y})")
        if grid[x][y] == 1:
            grid[x][y] = 0
            print(f"    -> Cleaned at ({x}, {y})")
        if all(grid[i][j] == 0 for i in range(rows) for j in range(cols)):
            print("\nAll tiles are clean! Task complete.\n")
            return
        for dx, dy in moves:
            new_x, new_y = x + dx, y + dy
            if is_valid(new_x, new_y, rows, cols) and (new_x, new_y) not in visited:
                queue.append((new_x, new_y, steps + 1))
    print("\nCleaning finished.\n")
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
grid = []
print("\nEnter grid row by row (0 for clean, 1 for dirty):")
for i in range(rows):
    grid.append(list(map(int, input().split())))
start_x = int(input("Enter starting row of vacuum cleaner: "))
start_y = int(input("Enter starting column of vacuum cleaner: "))
vacuum_cleaner(grid, start_x, start_y)
