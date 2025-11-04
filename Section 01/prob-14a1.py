def find_missing_number(arr):
    n = len(arr) + 1  # The range is from 1 to n, where n is len(arr) + 1
    total_sum = n * (n + 1) // 2  # Sum of numbers from 1 to n
    array_sum = sum(arr)  # Sum of elements in the array
    return total_sum - array_sum  # The missing number is the difference
