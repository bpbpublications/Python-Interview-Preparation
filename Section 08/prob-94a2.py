class TrieNode:
    def __init__(self):
        self.children = [None] * 26  # Array of size 26 for lowercase letters
        self.is_end_of_word = False
 
class Trie:
    def __init__(self):
        self.root = TrieNode()
 
    def _char_to_index(self, char):
        return ord(char) - ord('a')  # Convert character to index (0-25)
 
    def insert(self, word):
        current_node = self.root
        for char in word:
            index = self._char_to_index(char)
            if current_node.children[index] is None:
                current_node.children[index] = TrieNode()
            current_node = current_node.children[index]
        current_node.is_end_of_word = True
 
    def search(self, word):
        current_node = self.root
        for char in word:
            index = self._char_to_index(char)
            if current_node.children[index] is None:
                return False
            current_node = current_node.children[index]
        return current_node.is_end_of_word
 
    def starts_with(self, prefix):
        current_node = self.root
        for char in prefix:
            index = self._char_to_index(char)
            if current_node.children[index] is None:
                return False
            current_node = current_node.children[index]
        return True
