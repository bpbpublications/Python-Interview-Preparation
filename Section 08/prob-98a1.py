class KeyValueStore:
    def __init__(self):
        # Initialize an empty dictionary to store key-value pairs
        self.store = {}
 
    def put(self, key, value):
        """Insert or update a key-value pair."""
        self.store[key] = value
        print(f"Key '{key}' added/updated with value: {value}")
 
    def get(self, key):
        """Retrieve the value associated with the key."""
        if key in self.store:
            return self.store[key]
        else:
            print(f"Key '{key}' not found.")
            return None
 
    def delete(self, key):
        """Remove a key-value pair."""
        if key in self.store:
            del self.store[key]
            print(f"Key '{key}' deleted.")
        else:
            print(f"Key '{key}' not found.")
 
    def keys(self):
        """Return all keys in the store."""
        return list(self.store.keys())
