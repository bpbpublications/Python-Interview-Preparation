def two_sum(nums, target):
    # Dictionary to store number and its index
    seen = {}
 
    for i, num in enumerate(nums):
        # Calculate complement
        complement = target - num
 
        # Check if complement exists in the dictionary
        if complement in seen:
            return [seen[complement], i]
 
        # Store the number and its index in the dictionary
        seen[num] = i
