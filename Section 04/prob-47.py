def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
 
    # Check if the left child exists and is greater than the root
    if left < n and arr[left] > arr[largest]:
        largest = left
 
    # Check if the right child exists and is greater than the current largest
    if right < n and arr[right] > arr[largest]:
        largest = right
 
    # If the largest element is not the root, swap and heapify the affected subtree
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)
 
def heap_sort(arr):
    n = len(arr)
 
    # Step 1: Build a max-heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
 
    # Step 2: Extract elements one by one from the heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Swap the root (largest) with the last element
        heapify(arr, i, 0)  # Heapify the reduced heap
 
    return arr
