def first_non_repeating_char(s):
    # Step 1: Create a frequency array for lowercase letters
    char_count = [0] * 26
 
    # Step 2: Count the frequency of each character
    for char in s:
        char_count[ord(char) - ord('a')] += 1
 
    # Step 3: Find the first non-repeating character
    for char in s:
        if char_count[ord(char) - ord('a')] == 1:
            return char
 
    return None
