def can_partition(nums):
    total_sum = sum(nums)
 
    # If the total sum is odd, we can't split it equally
    if total_sum % 2 != 0:
        return False
 
    target = total_sum // 2
    dp = [False] * (target + 1)
    dp[0] = True  # Base case: A sum of 0 can always be achieved
 
    # Update dp array for each number in nums
    for num in nums:
        for i in range(target, num - 1, -1):
            dp[i] = dp[i] or dp[i - num]
 
    return dp[target]
