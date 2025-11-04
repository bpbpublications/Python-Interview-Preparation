def reverse_words(s):
    # Step 1: Split the string into words, ignoring extra spaces
    words = s.split()
 
    # Step 2: Reverse the list of words
    reversed_words = words[::-1]
 
    # Step 3: Join the words back into a single string
    return ' '.join(reversed_words)
