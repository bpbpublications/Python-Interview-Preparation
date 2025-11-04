def longest_palindrome(s):
    def is_palindrome(substring):
        return substring == substring[::-1]
 
    n = len(s)
    longest = ""
 
    for i in range(n):
        for j in range(i, n):
            if is_palindrome(s[i:j + 1]) and len(s[i:j + 1]) > len(longest):
                longest = s[i:j + 1]
 
    return longest
