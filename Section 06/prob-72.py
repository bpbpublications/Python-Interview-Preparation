def unique_paths(m, n):
    # Create a DP table with m rows and n columns
    dp = [[1] * n for _ in range(m)]
 
    # Fill the DP table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
 
    # The result is in the bottom-right corner of the table
    return dp[m - 1][n - 1]
