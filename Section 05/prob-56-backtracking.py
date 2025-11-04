def solve_n_queens(n):
    result = []
 
    # Helper function to check if placing a queen at (row, col) is valid
    def is_valid(board, row, col):
        # Check the same column
        for i in range(row):
            if board[i][col] == 'Q':
                return False
        # Check the upper left diagonal
        for i, j in zip(range(row - 1, -1, -1), range(col - 1, -1, -1)):
            if board[i][j] == 'Q':
                return False
        # Check the upper right diagonal
        for i, j in zip(range(row - 1, -1, -1), range(col + 1, n)):
            if board[i][j] == 'Q':
                return False
        return True
 
    # Helper function to backtrack and find all solutions
    def backtrack(board, row):
        if row == n:
            # Found a valid configuration, add it to the result
            result.append(["".join(row) for row in board])
            return
        for col in range(n):
            if is_valid(board, row, col):
                board[row][col] = 'Q'  # Place a queen
                backtrack(board, row + 1)  # Move to the next row
                board[row][col] = '.'  # Backtrack and remove the queen
 
    # Initialize an empty board
    board = [["." for _ in range(n)] for _ in range(n)]
    backtrack(board, 0)
    return result
