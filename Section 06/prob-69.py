def word_break(s, wordDict):
    word_set = set(wordDict)  # Convert wordDict to a set for faster lookups
    dp = [False] * (len(s) + 1)
    dp[0] = True  # Base case: Empty string can always be segmented
 
    # Fill the dp array
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break  # No need to check further if dp[i] is True
 
    return dp[len(s)]
