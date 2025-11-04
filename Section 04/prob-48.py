def bucket_sort(arr):
    n = len(arr)
    if n == 0:
        return arr
 
    # Step 1: Create empty buckets
    buckets = [[] for _ in range(n)]
 
    # Step 2: Distribute elements into buckets
    for num in arr:
        # Determine the bucket index based on the value
        index = int(num * n)
        buckets[index].append(num)
 
    # Step 3: Sort individual buckets
    for i in range(n):
        buckets[i].sort()
 
    # Step 4: Concatenate the sorted buckets
    sorted_array = []
    for bucket in buckets:
        sorted_array.extend(bucket)
 
    return sorted_array
