def length_of_lis(nums):
    if not nums:
        return 0
 
    # Initialize the dp array where each element starts with length 1
    dp = [1] * len(nums)
 
    # Fill the dp array
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
 
    # The answer is the maximum value in the dp array
    return max(dp)
