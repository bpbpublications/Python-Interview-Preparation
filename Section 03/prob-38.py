def longest_common_prefix(strs):
    if not strs:
        return ""
 
    # Start with the first string as the reference prefix
    prefix = strs[0]
 
    # Compare the prefix with each string
    for string in strs[1:]:
        # Shorten the prefix until it matches the current string
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
 
    return prefix
