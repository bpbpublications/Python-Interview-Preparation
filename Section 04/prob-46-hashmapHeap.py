import heapq
from collections import Counter
 
def top_k_frequent(arr, k):
    # Step 1: Count frequencies
    freq_map = Counter(arr)
 
    # Step 2: Use a heap to keep the top K frequent elements
    heap = []
 
    # Iterate over the frequency map
    for num, freq in freq_map.items():
        heapq.heappush(heap, (freq, num))  # Push (frequency, element)
 
        # If the heap size exceeds k, remove the smallest element
        if len(heap) > k:
            heapq.heappop(heap)
 
    # Extract the elements from the heap
    return [num for freq, num in heap]
