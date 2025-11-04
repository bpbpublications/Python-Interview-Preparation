class TrieNode:
    def __init__(self):
        # Initialize child nodes as an empty dictionary and other attributes
        self.children = {}
        self.is_word = False
        self.frequency = 0
 
class SearchAutocompleteSystem:
    def __init__(self):
        # Root of the Trie
        self.root = TrieNode()
 
    def insert(self, word, frequency=1):
        """Insert a word into the Trie with an optional frequency count."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_word = True
        node.frequency += frequency
        print(f"Inserted word '{word}' with frequency {node.frequency}")
 
    def search_prefix(self, prefix):
        """Return the node where the prefix ends."""
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node
 
    def autocomplete(self, prefix, top_n=5):
        """Return the top N autocomplete suggestions for the given prefix."""
        node = self.search_prefix(prefix)
        if not node:
            return []
 
        # Perform DFS to find all words starting with the prefix
        results = []
        self._dfs(node, prefix, results)
 
        # Sort the results by frequency in descending order and return the top N
        results.sort(key=lambda x: (-x[1], x[0]))  # Sort by frequency (highest first)
        return [word for word, freq in results[:top_n]]
 
    def _dfs(self, node, prefix, results):
        """Perform a depth-first search to collect all words starting with the given prefix."""
        if node.is_word:
            results.append((prefix, node.frequency))
 
        for char, child_node in node.children.items():
            self._dfs(child_node, prefix + char, results)
