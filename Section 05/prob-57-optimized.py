def subset_sum_dp(nums, target):
    # Create a DP table with dimensions (n+1) x (target+1)
    dp = [[False] * (target + 1) for _ in range(len(nums) + 1)]
 
    # A sum of 0 can always be achieved with the empty subset
    for i in range(len(nums) + 1):
        dp[i][0] = True
 
    # Fill the DP table
    for i in range(1, len(nums) + 1):
        for j in range(1, target + 1):
            if nums[i - 1] > j:
                dp[i][j] = dp[i - 1][j]  # Can't include current element
            else:
                dp[i][j] = dp[i - 1][j] or dp[i - 1][j - nums[i - 1]]  # Include or exclude current element
 
    return dp[len(nums)][target]
