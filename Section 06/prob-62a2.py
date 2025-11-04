def rob_optimized(nums):
    n = len(nums)
 
    # Handle base cases
    if n == 0:
        return 0
    if n == 1:
        return nums[0]
    if n == 2:
        return max(nums[0], nums[1])
 
    # Variables to store the last two results
    prev1 = nums[0]
    prev2 = max(nums[0], nums[1])
 
    # Calculate the maximum money for each house from 2 to n-1
    for i in range(2, n):
        current = max(prev2, prev1 + nums[i])
        prev1, prev2 = prev2, current
 
    return prev2
