def find_missing_number(arr):
    n = len(arr) + 1  # The range is from 1 to n
    full_set = set(range(1, n + 1))  # Create a set with numbers from 1 to n
 
    for num in arr:
        full_set.remove(num)  # Remove each number in the array from the set
 
    return full_set.pop()  # Return the remaining number in the set
