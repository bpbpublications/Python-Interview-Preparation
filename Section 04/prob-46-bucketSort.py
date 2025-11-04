from collections import Counter
 
def top_k_frequent(arr, k):
    # Step 1: Count frequencies
    freq_map = Counter(arr)
 
    # Step 2: Create a list of empty lists (buckets)
    bucket = [[] for _ in range(len(arr) + 1)]
 
    # Step 3: Populate the buckets
    for num, freq in freq_map.items():
        bucket[freq].append(num)
 
    # Step 4: Gather the top K frequent elements
    result = []
    for i in range(len(bucket) - 1, 0, -1):
        for num in bucket[i]:
            result.append(num)
            if len(result) == k:
                return result
