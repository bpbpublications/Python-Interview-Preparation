def flatten_list(nested_list):
    result = []
    stack = [nested_list]
 
    while stack:
        current = stack.pop()
        if isinstance(current, list):
            stack.extend(current[::-1])  # Add sublists in reverse order to maintain order
        else:
            result.append(current)
 
    return result[::-1]  # Reverse the result since we processed it backwards
