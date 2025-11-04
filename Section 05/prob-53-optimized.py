def subsets_iterative(nums):
    result = [[]]
    for num in nums:
        result += [curr + [num] for curr in result]
    return result
