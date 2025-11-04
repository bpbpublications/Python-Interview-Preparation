def fibonacci_memo(n, memo={}):
    # Base case: Return n if n is 0 or 1
    if n == 0 or n == 1:
        return n
 
    # Check if the result is already in the memo dictionary
    if n not in memo:
        # Store the result in memo after computing
        memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo)
 
    return memo[n]
