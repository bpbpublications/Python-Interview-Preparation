class Node:
    def __init__(self, data):
        # Each node has data and a reference to the next node
        self.data = data
        self.next = None
 
class CircularLinkedList:
    def __init__(self):
        # Initialize the circular linked list with an empty head
        self.head = None
 
    def append(self, data):
        # Add a new node with the given data to the end of the list
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
 
    def prepend(self, data):
        # Add a new node with the given data to the beginning of the list
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head
            self.head = new_node
 
    def delete(self, data):
        # Remove the first occurrence of the node with the given data
        if self.head:
            if self.head.data == data:
                if self.head.next == self.head:
                    self.head = None
                else:
                    current = self.head
                    while current.next != self.head:
                        current = current.next
                    current.next = self.head.next
                    self.head = self.head.next
            else:
                current = self.head
                prev = None
                while current.next != self.head:
                    prev = current
                    current = current.next
                    if current.data == data:
                        prev.next = current.next
                        break
 
    def print_list(self):
        # Print all the elements of the circular linked list
        current = self.head
        if not current:
            print("List is empty.")
            return
        while True:
            print(current.data, end=" -> ")
            current = current.next
            if current == self.head:
                break
        print("(back to head)")
