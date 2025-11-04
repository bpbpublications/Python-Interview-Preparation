def quick_sort(arr):
    # Base case: if the array has 1 or 0 elements, it's already sorted
    if len(arr) <= 1:
        return arr
 
    # Choose the pivot (here we use the last element as the pivot)
    pivot = arr[len(arr) - 1]
 
    # Partition the array
    left = [x for x in arr[:-1] if x <= pivot]
    right = [x for x in arr[:-1] if x > pivot]
 
    # Recursively sort the left and right parts and return the combined result
    return quick_sort(left) + [pivot] + quick_sort(right)
