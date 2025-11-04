def permute(nums):
    result = []
    used = [False] * len(nums)

    def backtrack(current_permutation):
        if len(current_permutation) == len(nums):
            result.append(current_permutation[:])
            return

        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                current_permutation.append(nums[i])
                backtrack(current_permutation)
                current_permutation.pop()
                used[i] = False

    backtrack([])
    return result

# usage
nums = [1, 2, 3]
print(permute(nums))
