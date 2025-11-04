def climb_stairs_optimized(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
 
    # Variables to store the last two steps
    prev1, prev2 = 1, 2
 
    # Calculate the number of ways for each step from 3 to n
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev1, prev2 = prev2, current
 
    return prev2
