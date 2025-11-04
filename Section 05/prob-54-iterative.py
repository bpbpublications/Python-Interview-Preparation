def permute_iterative(nums):
    result = [[]]
    for num in nums:
        new_result = []
        for perm in result:
            for i in range(len(perm)+1):
                new_result.append(perm[:i] + [num] + perm[i:])
        result = new_result
    return result

# usage
nums = [1, 2, 3]
print(permute_iterative(nums))
