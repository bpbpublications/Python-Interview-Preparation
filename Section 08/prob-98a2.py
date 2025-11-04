import time
 
class KeyValueStoreWithTTL:
    def __init__(self):
        self.store = {}
 
    def put(self, key, value, ttl=None):
        """Insert a key-value pair with an optional time-to-live (TTL)."""
        expiry_time = time.time() + ttl if ttl else None
        self.store[key] = (value, expiry_time)
        print(f"Key '{key}' added/updated with value: {value}, TTL: {ttl}s")
 
    def get(self, key):
        """Retrieve the value associated with the key, considering TTL."""
        if key in self.store:
            value, expiry_time = self.store[key]
            if expiry_time and time.time() > expiry_time:
                print(f"Key '{key}' has expired.")
                self.delete(key)
                return None
            return value
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
        return [key for key in self.store if not self._is_expired(key)]
 
    def _is_expired(self, key):
        """Helper method to check if a key has expired."""
        if key in self.store:
            _, expiry_time = self.store[key]
            return expiry_time and time.time() > expiry_time
        return False
