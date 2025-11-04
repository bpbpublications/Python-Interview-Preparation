def combination_sum_optimized(candidates, target):
    result = []
 
    def backtrack(remaining, current_combination, start):
        if remaining == 0:
            result.append(list(current_combination))
            return
        for i in range(start, len(candidates)):
            candidate = candidates[i]
            if candidate > remaining:
                break
            current_combination.append(candidate)
            backtrack(remaining - candidate, current_combination, i)
            current_combination.pop()
 
    candidates.sort()
    backtrack(target, [], 0)
    return result
