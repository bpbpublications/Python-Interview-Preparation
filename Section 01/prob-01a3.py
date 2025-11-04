def reverse_string(s):
    reversed_list = []
    for char in range(len(s)-1, -1, -1):
        reversed_list.append(s[char])
    return ''.join(reversed_list)
