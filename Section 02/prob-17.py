class Stack:
    def __init__(self):
        # Initialize an empty stack using a list
        self.stack = []
 
    def push(self, item):
        # Add an item to the top of the stack
        self.stack.append(item)
 
    def pop(self):
        # Remove and return the top item from the stack
        if not self.is_empty():
            return self.stack.pop()
        else:
            return "Stack is empty, cannot pop."
 
    def peek(self):
        # Return the top item without removing it
        if not self.is_empty():
            return self.stack[-1]
        else:
            return "Stack is empty, nothing to peek."
 
    def is_empty(self):
        # Check if the stack is empty
        return len(self.stack) == 0
 
    def size(self):
        # Return the number of items in the stack
        return len(self.stack)
