def min_path_sum(grid):
    m, n = len(grid), len(grid[0])
 
    # Initialize the dp table
    dp = [[0] * n for _ in range(m)]
 
    # Base case: starting point
    dp[0][0] = grid[0][0]
 
    # Fill the first row (can only move right)
    for j in range(1, n):
        dp[0][j] = dp[0][j-1] + grid[0][j]
 
    # Fill the first column (can only move down)
    for i in range(1, m):
        dp[i][0] = dp[i-1][0] + grid[i][0]
 
    # Fill the rest of the dp table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = grid[i][j] + min(dp[i-1][j], dp[i][j-1])
 
    return dp[m-1][n-1]
