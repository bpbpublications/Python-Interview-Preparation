import bisect
 
def length_of_lis_optimized(nums):
    lis = []
 
    for num in nums:
        # Find the index where num can be placed
        pos = bisect.bisect_left(lis, num)
 
        # If num is larger than any element in lis, append it
        if pos == len(lis):
            lis.append(num)
        else:
            # Otherwise, replace the existing element
            lis[pos] = num
 
    return len(lis)
