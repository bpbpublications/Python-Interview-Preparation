def longest_common_subsequence_optimized(text1, text2):
    m, n = len(text1), len(text2)
 
    # Use only two rows for the dp array
    prev = [0] * (n + 1)
    curr = [0] * (n + 1)
 
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                curr[j] = prev[j - 1] + 1
            else:
                curr[j] = max(prev[j], curr[j - 1])
        prev, curr = curr, prev
 
    return prev[n]
