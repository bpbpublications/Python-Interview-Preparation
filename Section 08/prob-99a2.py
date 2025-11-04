class SearchAutocompleteHashMap:
    def __init__(self):
        self.search_terms = {}
 
    def insert(self, term, frequency=1):
        """Insert or update a search term."""
        if term in self.search_terms:
            self.search_terms[term] += frequency
        else:
            self.search_terms[term] = frequency
 
    def autocomplete(self, prefix, top_n=5):
        """Return the top N suggestions for the given prefix."""
        # Filter search terms that start with the prefix
        results = [(term, freq) for term, freq in self.search_terms.items() if term.startswith(prefix)]
 
        # Sort by frequency and return the top N
        results.sort(key=lambda x: (-x[1], x[0]))
        return [term for term, freq in results[:top_n]]
