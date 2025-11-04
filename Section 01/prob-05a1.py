def count_occurrences(s, char):
    count = 0
    for c in s:
        if c == char:
            count += 1
    return count
