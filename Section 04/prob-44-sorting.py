def find_kth_largest(arr, k):
    # Sort the array in descending order
    arr.sort(reverse=True)
 
    # Return the Kth largest element
    return arr[k-1]
