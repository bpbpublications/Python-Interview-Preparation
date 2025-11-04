def are_anagrams(str1, str2):
    if len(str1) != len(str2):
        return False
 
    # Create an array of size 26 for lowercase English letters
    count = [0] * 26
 
    # Count characters in both strings
    for i in range(len(str1)):
        count[ord(str1[i]) - ord('a')] += 1
        count[ord(str2[i]) - ord('a')] -= 1
 
    # Check if all counts are zero
    for c in count:
        if c != 0:
            return False
 
    return True
