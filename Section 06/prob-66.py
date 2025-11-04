def coin_change(coins, amount):
    # Initialize dp array with amount + 1 (infeasible large number)
    dp = [amount + 1] * (amount + 1)
    dp[0] = 0  # Base case: no coins are needed to make amount 0
 
    # Fill dp array
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
 
    # If dp[amount] is still amount + 1, return -1 (unattainable)
    return dp[amount] if dp[amount] != amount + 1 else -1
