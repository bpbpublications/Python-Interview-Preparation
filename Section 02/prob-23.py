class TicTacToe:
    def __init__(self):
        # Initialize an empty 3x3 board
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_winner = None
 
    def print_board(self):
        # Print the current game board
        for row in self.board:
            print(' | '.join(row))
            print('-' * 9)
 
    def make_move(self, row, col, player):
        # Make a move if the chosen cell is empty
        if self.board[row][col] == ' ':
            self.board[row][col] = player
            # Check if this move wins the game
            if self.check_winner(row, col, player):
                self.current_winner = player
            return True
        else:
            print("This move is not valid. Try again.")
            return False
 
    def check_winner(self, row, col, player):
        # Check the row
        if all([self.board[row][i] == player for i in range(3)]):
            return True
        # Check the column
        if all([self.board[i][col] == player for i in range(3)]):
            return True
        # Check the diagonals
        if row == col and all([self.board[i][i] == player for i in range(3)]):
            return True
        if row + col == 2 and all([self.board[i][2 - i] == player for i in range(3)]):
            return True
        return False
 
    def is_draw(self):
        # Check if the game is a draw (all cells are filled and no winner)
        return all([self.board[row][col] != ' ' for row in range(3) for col in range(3)]) and self.current_winner is None
