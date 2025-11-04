def knapsack(weights, values, W):
    n = len(weights)
 
    # Initialize the dp table with all zeros
    dp = [[0] * (W + 1) for _ in range(n + 1)]
 
    # Build the dp table
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                # Either take the current item or don't take it
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weights[i - 1]] + values[i - 1])
            else:
                dp[i][w] = dp[i - 1][w]
 
    # The last cell of the dp table will contain the maximum value
    return dp[n][W]
