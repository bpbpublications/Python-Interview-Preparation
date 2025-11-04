def max_subarray(nums):
    # Initialize max_sum as the first element
    max_sum = current_sum = nums[0]
 
    for num in nums[1:]:
        # Either continue the subarray or start a new one
        current_sum = max(num, current_sum + num)
 
        # Update the max_sum if current_sum is larger
        max_sum = max(max_sum, current_sum)
 
    return max_sum
