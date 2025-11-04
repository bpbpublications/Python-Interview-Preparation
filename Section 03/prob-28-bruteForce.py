def product_except_self(nums):
    n = len(nums)
    answer = []
 
    for i in range(n):
        product = 1
        for j in range(n):
            if i != j:
                product *= nums[j]
        answer.append(product)
 
    return answer
