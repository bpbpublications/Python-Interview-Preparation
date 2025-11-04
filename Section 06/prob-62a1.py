def rob(nums):
    n = len(nums)
 
    # Handle base cases
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
 
    # DP array to store the maximum money that can be robbed up to house i
    dp = [0] * n
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
 
    # Fill the dp array
    for i in range(2, n):
        dp[i] = max(dp[i-1], dp[i-2] + nums[i])
 
    # The result will be stored in dp[n-1]
    return dp[n-1]
