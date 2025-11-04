def counting_sort(arr):
    if len(arr) == 0:
        return arr
 
    # Step 1: Find the maximum element in the array
    max_value = max(arr)
 
    # Step 2: Create a count array to store the count of each element
    count = [0] * (max_value + 1)
 
    # Step 3: Count each element in the input array
    for num in arr:
        count[num] += 1
 
    # Step 4: Modify the count array so that each element contains the actual position of the element
    for i in range(1, len(count)):
        count[i] += count[i - 1]
 
    # Step 5: Build the output array
    output = [0] * len(arr)
    for num in reversed(arr):
        output[count[num] - 1] = num
        count[num] -= 1
 
    return output
