def exist(board, word):
    rows, cols = len(board), len(board[0])
 
    def dfs(r, c, i):
        # Base case: if we've found the entire word
        if i == len(word):
            return True
        # If out of bounds or the current cell doesn't match the current letter
        if r < 0 or c < 0 or r >= rows or c >= cols or board[r][c] != word[i]:
            return False
 
        # Temporarily mark the cell as visited by modifying its value
        temp, board[r][c] = board[r][c], '#'
 
        # Explore all four directions: up, down, left, right
        found = (dfs(r + 1, c, i + 1) or  # down
                 dfs(r - 1, c, i + 1) or  # up
                 dfs(r, c + 1, i + 1) or  # right
                 dfs(r, c - 1, i + 1))    # left
 
        # Restore the original value after backtracking
        board[r][c] = temp
 
        return found
 
    # Start the search from every cell in the board
    for row in range(rows):
        for col in range(cols):
            if board[row][col] == word[0] and dfs(row, col, 0):
                return True
 
    return False
