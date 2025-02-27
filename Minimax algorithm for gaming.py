import math
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  
        self.current_player = 'X'  
    def print_board(self):
        print("Current board:")
        for i in range(3):
            print(f"{self.board[i*3]} | {self.board[i*3 + 1]} | {self.board[i*3 + 2]}")
            if i < 2:
                print("---------")
    def is_winner(self, player):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  
            (0, 4, 8), (2, 4, 6)              
        ]
        for combo in winning_combinations:
            if self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]] == player:
                return True
        return False
    def is_draw(self):
        return ' ' not in self.board
    def minimax(self, depth, is_maximizing):
        if self.is_winner('X'):
            return -1  
        if self.is_winner('O'):
            return 1 
        if self.is_draw():
            return 0  
        if is_maximizing:
            best_score = -math.inf
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'O'  
                    score = self.minimax(depth + 1, False)
                    self.board[i] = ' ' 
                    best_score = max(score, best_score)
            return best_score
        else:
            best_score = math.inf
            for i in range(9):
                if self.board[i] == ' ':
                    self.board[i] = 'X'  
                    score = self.minimax(depth + 1, True)
                    self.board[i] = ' '  
                    best_score = min(score, best_score)
            return best_score
    def best_move(self):
        best_score = -math.inf
        move = -1
        for i in range(9):
            if self.board[i] == ' ':
                self.board[i] = 'O'  
                score = self.minimax(0, False)
                self.board[i] = ' ' 
                if score > best_score:
                    best_score = score
                    move = i
        return move
    def play(self):
        while True:
            self.print_board()
            if self.current_player == 'X':
                try:
                    move = int(input(f"Player {self.current_player}, enter your move (1-9): ")) - 1
                    if move < 0 or move > 8:
                        print("Invalid move. Please enter a number between 1 and 9.")
                        continue
                except ValueError:
                    print("Invalid input. Please enter a number between 1 and 9.")
                    continue
            else:
                move = self.best_move() 
            if self.board[move] == ' ':
                self.board[move] = self.current_player
                if self.is_winner(self.current_player):
                    self.print_board()
                    print(f"Player {self.current_player} wins!")
                    break
                if self.is_draw():
                    self.print_board()
                    print("It's a draw!")
                    break
                self.switch_player()
            else:
                print("This position is already taken. Try again.")
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
if __name__ == "__main__":
    game = TicTacToe()
    game.play()
