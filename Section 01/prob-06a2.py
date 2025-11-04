from collections import OrderedDict
 
def first_non_repeating_char(s):
    # Step 1: Use OrderedDict to preserve the insertion order
    char_count = OrderedDict()
 
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
 
    # Step 2: Find the first character with a count of 1
    for char, count in char_count.items():
        if count == 1:
            return char
 
    return None
