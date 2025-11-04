def find_missing_number(arr):
    n = len(arr) + 1  # The range is from 1 to n
    xor_all = 0
    xor_array = 0
 
    # XOR all numbers from 1 to n
    for i in range(1, n + 1):
        xor_all ^= i
 
    # XOR all elements in the array
    for num in arr:
        xor_array ^= num
 
    # XOR the two results to get the missing number
    return xor_all ^ xor_array
