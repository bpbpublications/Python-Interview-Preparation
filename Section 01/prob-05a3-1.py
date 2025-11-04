def count_occurrences_recursive(s, char):
    if not s:
        return 0
    return (1 if s[0] == char else 0) + count_occurrences_recursive(s[1:], char)
