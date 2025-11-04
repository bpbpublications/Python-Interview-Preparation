from collections import Counter

def min_window(s, t):
    if not s or not t:
        return ""
 
    # Dictionary to count the frequency of characters in t
    char_count_t = Counter(t)
    required = len(char_count_t)
 
    # Left and right pointers for the window
    l, r = 0, 0
 
    # Dictionary to count the characters in the current window
    window_counts = {}
    formed = 0
 
    # Result tuple: (window length, left, right)
    ans = float("inf"), None, None
 
    while r < len(s):
        # Add the character from the right pointer
        char = s[r]
        window_counts[char] = window_counts.get(char, 0) + 1
 
        # Check if this character matches the frequency in t
        if char in char_count_t and window_counts[char] == char_count_t[char]:
            formed += 1
 
        # Try to shrink the window from the left
        while l <= r and formed == required:
            char = s[l]
 
            # Save the smallest window
            if r - l + 1 < ans[0]:
                ans = (r - l + 1, l, r)
 
            # Remove the character from the left
            window_counts[char] -= 1
            if char in char_count_t and window_counts[char] < char_count_t[char]:
                formed -= 1
 
            l += 1
 
        # Expand the window by moving the right pointer
        r += 1
 
    # Return the smallest window or an empty string if no valid window is found
    return "" if ans[0] == float("inf") else s[ans[1]:ans[2] + 1]
