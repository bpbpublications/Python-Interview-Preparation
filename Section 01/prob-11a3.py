def remove_duplicates(lst):
    seen = set()
    return [num for num in lst if num not in seen and not seen.add(num)]
