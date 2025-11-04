def subset_sum(nums, target):
    def backtrack(index, current_sum):
        # Base case: If the current sum equals the target, return True
        if current_sum == target:
            return True
        # If we've processed all elements or exceeded the target, return False
        if index >= len(nums) or current_sum > target:
            return False
 
        # Option 1: Include the current number
        include = backtrack(index + 1, current_sum + nums[index])
        # Option 2: Exclude the current number
        exclude = backtrack(index + 1, current_sum)
 
        # Return True if either option results in the target sum
        return include or exclude
 
    return backtrack(0, 0)
