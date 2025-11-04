def find_kth_largest(arr, k):
    # Create a min-heap of the first k elements
    heap = arr[:k]
    heapq.heapify(heap)
 
    # Process the remaining elements
    for num in arr[k:]:
        if num > heap[0]:
            heapq.heappushpop(heap, num)
 
    # The root of the heap is the Kth largest element
    return heap[0]
