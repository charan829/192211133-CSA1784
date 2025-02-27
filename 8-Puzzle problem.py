import heapq

class Puzzle:
    def __init__(self, board, moves=0):
        self.board = board
        self.moves = moves
        self.empty_pos = [(r, c) for r in range(3) for c in range(3) if board[r][c] == 0][0]
    
    def heuristic(self):
        goal = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        return sum(abs(r - i) + abs(c - j)
                   for r, row in enumerate(self.board)
                   for c, val in enumerate(row)
                   for i, goal_row in enumerate(goal)
                   for j, goal_val in enumerate(goal_row) if val == goal_val and val != 0)
    
    def is_goal(self):
        return self.board == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
    
    def possible_moves(self):
        r, c = self.empty_pos
        directions = [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]
        moves = []
        for nr, nc in directions:
            if 0 <= nr < 3 and 0 <= nc < 3:
                new_board = [row[:] for row in self.board]
                new_board[r][c], new_board[nr][nc] = new_board[nr][nc], new_board[r][c]
                moves.append(Puzzle(new_board, self.moves + 1))
        return moves
    
    def __lt__(self, other):
        return (self.moves + self.heuristic()) < (other.moves + other.heuristic())

def solve_puzzle(start_board):
    pq = [(0, Puzzle(start_board))]
    visited = set()
    
    while pq:
        _, node = heapq.heappop(pq)
        if node.is_goal():
            return node.moves
        visited.add(tuple(map(tuple, node.board)))
        
        for neighbor in node.possible_moves():
            if tuple(map(tuple, neighbor.board)) not in visited:
                heapq.heappush(pq, (neighbor.heuristic(), neighbor))
    return -1

initial_board = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]
print("Moves to solve:", solve_puzzle(initial_board))
