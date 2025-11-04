def longest_consecutive(nums):
    if not nums:
        return 0
 
    num_set = set(nums)  # Store all numbers in a hash set
    longest_sequence = 0
 
    for num in num_set:
        # Only check for the start of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_sequence = 1
 
            # Check for the next consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_sequence += 1
 
            # Update the longest sequence
            longest_sequence = max(longest_sequence, current_sequence)
 
    return longest_sequence
