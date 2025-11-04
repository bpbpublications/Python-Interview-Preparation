def find_second_largest(lst):
    if len(lst) < 2:
        return None
 
    first, second = None, None
 
    for num in lst:
        if first is None or num > first:
            second = first
            first = num
        elif num != first and (second is None or num > second):
            second = num
 
    return second
