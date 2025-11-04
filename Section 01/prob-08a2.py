def find_second_largest(lst):
    # Remove duplicates and sort the list in descending order
    lst = list(set(lst))
    lst.sort(reverse=True)
 
    # Return the second element if it exists
    if len(lst) >= 2:
        return lst[1]
    else:
        return None
