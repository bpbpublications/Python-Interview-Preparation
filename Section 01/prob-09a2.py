def are_anagrams(str1, str2):
    # If lengths of the strings are not equal, they can't be anagrams
    if len(str1) != len(str2):
        return False
 
    # Create a dictionary to count characters in both strings
    char_count = {}
 
    # Count the characters in the first string
    for char in str1:
        char_count[char] = char_count.get(char, 0) + 1
 
    # Subtract the character count based on the second string
    for char in str2:
        if char not in char_count:
            return False
        char_count[char] -= 1
 
    # Check if all counts are zero (meaning both strings have the same characters)
    for count in char_count.values():
        if count != 0:
            return False
 
    return True
