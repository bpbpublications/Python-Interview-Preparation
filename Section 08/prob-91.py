class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
 
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}  # Hash map to store key and node reference
        self.head = Node()  # Dummy head node for doubly linked list
        self.tail = Node()  # Dummy tail node for doubly linked list
        self.head.next = self.tail
        self.tail.prev = self.head
 
    def _remove(self, node):
        """Helper function to remove a node from the linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
 
    def _add_to_front(self, node):
        """Helper function to add a node to the front (right after head)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
 
    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self._remove(node)  # Move node to front as it's recently used
            self._add_to_front(node)
            return node.value
        return -1
 
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._remove(node)
            self._add_to_front(node)
        else:
            if len(self.cache) >= self.capacity:
                # Remove least recently used node
                lru_node = self.tail.prev
                self._remove(lru_node)
                del self.cache[lru_node.key]
            new_node = Node(key, value)
            self._add_to_front(new_node)
            self.cache[key] = new_node
