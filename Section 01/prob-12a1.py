def rotate_list(lst, k):
    # Handle cases where K is greater than the length of the list
    k = k % len(lst)
 
    # Rotate the list using slicing
    return lst[-k:] + lst[:-k]
