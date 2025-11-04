class Node:
    def __init__(self, data):
        # Each node has data and a reference to the next node
        self.data = data
        self.next = None
 
class LinkedList:
    def __init__(self):
        # Initialize the linked list with an empty head
        self.head = None
 
    def append(self, data):
        # Add a new node with the given data to the end of the list
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
 
    def prepend(self, data):
        # Add a new node with the given data to the beginning of the list
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
 
    def delete(self, data):
        # Remove the first occurrence of the node with the given data
        if not self.head:
            return "List is empty, nothing to delete."
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next and current.next.data != data:
            current = current.next
        if current.next:
            current.next = current.next.next
        else:
            return f"Node with data {data} not found."
 
    def find(self, data):
        # Find and return the node with the given data
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None
 
    def print_list(self):
        # Print all the elements of the linked list
        current = self.head
        if not current:
            print("List is empty.")
            return
        while current:
            print(current.data, end=" -> " if current.next else "\\n")
            current = current.next
