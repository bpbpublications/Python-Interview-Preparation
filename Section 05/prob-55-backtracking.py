def combination_sum(candidates, target):
    result = []
 
    def backtrack(remaining, current_combination, start):
        # Base case: If the remaining target is 0, add the current combination to the result
        if remaining == 0:
            result.append(list(current_combination))
            return
        # Explore each candidate starting from the current index
        for i in range(start, len(candidates)):
            candidate = candidates[i]
            # If the candidate is greater than the remaining target, break (no point in continuing)
            if candidate > remaining:
                break
            # Include the candidate in the combination
            current_combination.append(candidate)
            # Recursively try to reach the target by reducing the remaining value
            backtrack(remaining - candidate, current_combination, i)
            # Backtrack by removing the last included candidate
            current_combination.pop()
 
    # Sort the candidates to ensure the combinations are generated in order
    candidates.sort()
    backtrack(target, [], 0)
    return result
