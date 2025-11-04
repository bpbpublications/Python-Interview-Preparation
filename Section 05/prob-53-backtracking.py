def subsets(nums):
    result = []
 
    def backtrack(current_subset, index):
        # Add the current subset to the result
        result.append(list(current_subset))
 
        # Explore further subsets by including or excluding the next element
        for i in range(index, len(nums)):
            # Include nums[i] in the current subset
            current_subset.append(nums[i])
            # Move to the next element
            backtrack(current_subset, i + 1)
            # Backtrack: Remove nums[i] to explore other subsets
            current_subset.pop()
 
    backtrack([], 0)
    return result
