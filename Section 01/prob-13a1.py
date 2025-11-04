def flatten_list(nested_list):
    result = []
    for element in nested_list:
        if isinstance(element, list):
            result.extend(flatten_list(element))  # Recursively flatten
        else:
            result.append(element)
    return result
