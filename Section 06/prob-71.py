def count_palindromic_substrings(s):
    def expand_around_center(left, right):
        count = 0
        while left >= 0 and right < len(s) and s[left] == s[right]:
            count += 1
            left -= 1
            right += 1
        return count
 
    total_palindromes = 0
 
    # Expand around each character (odd-length palindromes)
    for i in range(len(s)):
        total_palindromes += expand_around_center(i, i)  # Odd length
 
    # Expand around each pair of characters (even-length palindromes)
    for i in range(len(s) - 1):
        total_palindromes += expand_around_center(i, i + 1)  # Even length
 
    return total_palindromes
