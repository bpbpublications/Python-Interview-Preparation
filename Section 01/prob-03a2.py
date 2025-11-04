def find_max_of_three(a, b, c):
    return a if a >= b and a >= c else (b if b >= c else c)
