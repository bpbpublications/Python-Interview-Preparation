def intersection(nums1, nums2):
    result = set()
 
    for num in nums1:
        if num in nums2:
            result.add(num)
 
    return list(result)
