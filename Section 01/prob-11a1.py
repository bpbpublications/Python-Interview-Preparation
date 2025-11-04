def remove_duplicates(lst):
    seen = set()
    result = []
 
    for num in lst:
        if num not in seen:
            seen.add(num)
            result.append(num)
 
    return result
