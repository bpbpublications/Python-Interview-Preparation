def reverse_string(s):
    reversed_str = ""
    for char in range(len(s)-1, -1, -1):
        reversed_str += s[char]
    return reversed_str
