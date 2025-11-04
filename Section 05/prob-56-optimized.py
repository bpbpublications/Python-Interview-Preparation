def solve_n_queens_optimized(n):
    result = []
    columns = set()
    pos_diagonals = set()  # (r + c)
    neg_diagonals = set()  # (r - c)
 
    def backtrack(row, board):
        if row == n:
            result.append(["".join(row) for row in board])
            return
        for col in range(n):
            if col in columns or (row + col) in pos_diagonals or (row - col) in neg_diagonals:
                continue
            # Place the queen
            columns.add(col)
            pos_diagonals.add(row + col)
            neg_diagonals.add(row - col)
            board[row][col] = 'Q'
            # Move to the next row
            backtrack(row + 1, board)
            # Backtrack: Remove the queen
            columns.remove(col)
            pos_diagonals.remove(row + col)
            neg_diagonals.remove(row - col)
            board[row][col] = '.'
 
    board = [["." for _ in range(n)] for _ in range(n)]
    backtrack(0, board)
    return result
