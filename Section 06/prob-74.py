def num_decodings(s):
    if not s or s[0] == '0':
        return 0
 
    n = len(s)
    dp = [0] * (n + 1)
    dp[0] = 1  # Base case: One way to decode an empty string
    dp[1] = 1  # One way to decode a string if the first digit is valid
 
    for i in range(2, n + 1):
        # Single digit decoding (s[i-1])
        if s[i-1] != '0':
            dp[i] += dp[i-1]
 
        # Two-digit decoding (s[i-2:i])
        if 10 <= int(s[i-2:i]) <= 26:
            dp[i] += dp[i-2]
 
    return dp[n]
