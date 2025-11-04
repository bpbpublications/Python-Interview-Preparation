class TrieNode:
    def __init__(self):
        self.children = {}  # Dictionary to store child nodes
        self.is_end_of_word = False  # Marks the end of a word
 
class Trie:
    def __init__(self):
        self.root = TrieNode()  # Root node of the Trie
 
    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()  # Create new node if char doesn't exist
            current_node = current_node.children[char]  # Move to the next node
        current_node.is_end_of_word = True  # Mark the end of the word
 
    def search(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False  # Word not found
            current_node = current_node.children[char]
        return current_node.is_end_of_word  # Check if it's the end of the word
 
    def starts_with(self, prefix):
        current_node = self.root
        for char in prefix:
            if char not in current_node.children:
                return False  # Prefix not found
            current_node = current_node.children[char]
        return True  # Prefix exists
