def climb_stairs(n):
    # Base case for n = 1 or n = 2
    if n == 1:
        return 1
    if n == 2:
        return 2
 
    # DP array to store the number of ways to reach each step
    dp = [0] * (n + 1)
    dp[1] = 1  # 1 way to reach step 1
    dp[2] = 2  # 2 ways to reach step 2
 
    # Build the dp array from step 3 to n
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
 
    # The answer is stored in dp[n]
    return dp[n]
