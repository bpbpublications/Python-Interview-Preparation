def restore_ip_addresses(s):
    def is_valid(segment):
        # Check if the segment is between 0 and 255 and has no leading zeros
        return len(segment) == 1 or (segment[0] != '0' and int(segment) <= 255)
 
    def backtrack(start, dots, path):
        # If we have placed 3 dots and the remaining part is valid, add the result
        if dots == 3:
            segment = s[start:]
            if is_valid(segment):
                result.append(path + segment)
            return
 
        # Try placing a dot after 1, 2, or 3 digits
        for i in range(start, min(start + 3, len(s))):
            segment = s[start:i + 1]
            if is_valid(segment):
                backtrack(i + 1, dots + 1, path + segment + '.')
 
    result = []
    if len(s) > 12:  # Too long to be a valid IP address
        return result
    backtrack(0, 0, "")
    return result
