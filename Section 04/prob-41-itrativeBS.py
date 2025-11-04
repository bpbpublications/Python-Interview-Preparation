def binary_search(arr, target):
    left, right = 0, len(arr) - 1
 
    while left <= right:
        mid = (left + right) // 2
 
        # Check if the middle element is the target
        if arr[mid] == target:
            return mid
 
        # If target is smaller, search the left half
        elif target < arr[mid]:
            right = mid - 1
 
        # If target is larger, search the right half
        else:
            left = mid + 1
 
    # Target not found
    return -1
