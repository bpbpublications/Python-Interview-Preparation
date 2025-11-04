def product_except_self(nums):
    n = len(nums)
    answer = [1] * n
 
    # Step 1: Fill in the left products
    left_product = 1
    for i in range(n):
        answer[i] = left_product
        left_product *= nums[i]
 
    # Step 2: Multiply by the right products
    right_product = 1
    for i in range(n - 1, -1, -1):
        answer[i] *= right_product
        right_product *= nums[i]
 
    return answer
