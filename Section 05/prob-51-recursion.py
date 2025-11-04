def factorial(n):
    # Base case: If n is 0, return 1
    if n == 0:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1)
