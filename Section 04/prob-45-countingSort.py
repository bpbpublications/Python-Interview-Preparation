def sort_colors(arr):
    count = [0, 0, 0]  # counts for 0s, 1s, and 2s
 
    for num in arr:
        count[num] += 1
 
    # Overwrite the array with sorted elements
    index = 0
    for i in range(count[0]):
        arr[index] = 0
        index += 1
    for i in range(count[1]):
        arr[index] = 1
        index += 1
    for i in range(count[2]):
        arr[index] = 2
        index += 1
 
    return arr
