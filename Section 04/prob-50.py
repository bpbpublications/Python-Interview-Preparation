def counting_sort_for_radix(arr, exp):
    n = len(arr)
 
    # Output array to store sorted numbers
    output = [0] * n
 
    # Count array to store the occurrences of digits (0-9)
    count = [0] * 10
 
    # Count occurrences of digits in the current place value (exp)
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1
 
    # Modify the count array to store actual positions of digits
    for i in range(1, 10):
        count[i] += count[i - 1]
 
    # Build the output array
    for i in reversed(range(n)):
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
 
    # Copy the sorted numbers back to the original array
    for i in range(n):
        arr[i] = output[i]
 
 
def radix_sort(arr):
    # Step 1: Find the maximum number to know the number of digits
    max_value = max(arr)
 
    # Step 2: Perform counting sort for each digit, starting from the least significant digit
    exp = 1  # Initialize exp to 1 (1's place)
    while max_value // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10  # Move to the next place value (10's place, 100's place, etc.)
