from collections import Counter
 
def majority_element(nums):
    counts = Counter(nums)
    for num, count in counts.items():
        if count > len(nums) // 2:
            return num
