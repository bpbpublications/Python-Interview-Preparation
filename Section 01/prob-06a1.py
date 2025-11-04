def first_non_repeating_char(s):
    # Step 1: Count the frequency of each character
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1
 
    # Step 2: Find the first character with a count of 1
    for char in s:
        if char_count[char] == 1:
            return char
 
    return None
