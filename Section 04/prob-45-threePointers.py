def sort_colors(arr):
    # Initialize pointers
    low, mid, high = 0, 0, len(arr) - 1
 
    # Traverse through the array
    while mid <= high:
        if arr[mid] == 0:
            # Swap 0 to the front
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            # 1 is already in the right place, just move mid
            mid += 1
        else:
            # Swap 2 to the end
            arr[high], arr[mid] = arr[mid], arr[high]
            high -= 1
 
    return arr
