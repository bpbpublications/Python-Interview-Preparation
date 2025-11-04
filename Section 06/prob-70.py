def maximal_square(matrix):
    if not matrix:
        return 0
 
    rows = len(matrix)
    cols = len(matrix[0])
 
    # Create a DP table with (rows + 1) x (cols + 1) size
    dp = [[0] * (cols + 1) for _ in range(rows + 1)]
 
    max_square_length = 0
 
    # Fill the DP table
    for i in range(1, rows + 1):
        for j in range(1, cols + 1):
            if matrix[i - 1][j - 1] == "1":
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
                max_square_length = max(max_square_length, dp[i][j])
 
    # The area of the largest square
    return max_square_length ** 2
