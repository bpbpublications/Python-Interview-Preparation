def reverse_string(s):
    s = list(s)  # Convert string to list
    left, right = 0, len(s) - 1
 
    while left < right:
        s[left], s[right] = s[right], s[left]  # Swap characters
        left += 1
        right -= 1
 
    return ''.join(s)  # Convert list back to string
