N = 8  
def print_solution(board):
    """Function to print the chessboard solution"""
    for row in board:
        print(" ".join("Q" if col else "." for col in row))
    print("\n")
def is_safe(board, row, col):
    """Check if a queen can be placed at board[row][col]"""
    for i in range(row):
        if board[i][col]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j]:
            return False
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j]:
            return False
    return True
def solve_n_queens(board, row):
    """Recursive function to solve the N-Queens problem"""
    if row == N:  
        print_solution(board)
        return True  
    for col in range(N):  
        if is_safe(board, row, col):
            board[row][col] = 1  
            if solve_n_queens(board, row + 1):  
                return True  
            board[row][col] = 0  
    return False  
def solve():
    """Initialize the chessboard and call the solver"""
    board = [[0] * N for _ in range(N)]
    if not solve_n_queens(board, 0):
        print("No solution exists")
    else:
        print("Solution found!")
solve()
