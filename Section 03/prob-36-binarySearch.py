def find_missing(nums):
    left, right = 0, len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        # Check if the current element matches the expected value
        if nums[mid] != nums[0] + mid:
            right = mid - 1
        else:
            left = mid + 1
    return nums[0] + left
