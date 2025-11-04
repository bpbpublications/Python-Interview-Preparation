def reverse(lst, start, end):
    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1
 
def rotate_list(lst, k):
    n = len(lst)
    k = k % n  # Handle cases where k is greater than the length of the list
 
    # Step 1: Reverse the entire list
    reverse(lst, 0, n - 1)
 
    # Step 2: Reverse the first K elements
    reverse(lst, 0, k - 1)
 
    # Step 3: Reverse the remaining elements
    reverse(lst, k, n - 1)
