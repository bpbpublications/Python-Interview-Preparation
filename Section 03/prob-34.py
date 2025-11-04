def find_min(nums):
    left, right = 0, len(nums) - 1
 
    # If the array is not rotated (sorted in ascending order)
    if nums[left] <= nums[right]:
        return nums[left]
 
    while left < right:
        mid = (left + right) // 2
 
        # Check if the minimum is in the right half
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
 
    return nums[left]
