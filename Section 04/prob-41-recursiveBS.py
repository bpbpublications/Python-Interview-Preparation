def recursive_binary_search(arr, target, left, right):
    # Base case: if the search space is exhausted
    if left > right:
        return -1
 
    # Calculate the middle index
    mid = (left + right) // 2
 
    # Check if the middle element is the target
    if arr[mid] == target:
        return mid
 
    # If target is smaller, search the left half
    elif target < arr[mid]:
        return recursive_binary_search(arr, target, left, mid - 1)
 
    # If target is larger, search the right half
    else:
        return recursive_binary_search(arr, target, mid + 1, right)
