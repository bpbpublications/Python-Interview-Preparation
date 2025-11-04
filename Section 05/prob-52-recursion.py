def fibonacci(n):
    # Base case: Return n if n is 0 or 1
    if n == 0 or n == 1:
        return n
    else:
        # Recursive case: Return the sum of the two preceding numbers
        return fibonacci(n - 1) + fibonacci(n - 2)
