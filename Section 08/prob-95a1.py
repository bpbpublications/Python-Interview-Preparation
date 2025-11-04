import threading
from collections import deque
 
class MessageQueue:
    def __init__(self):
        self.queue = deque()  # FIFO queue
        self.lock = threading.Lock()  # Lock for concurrency
 
    def enqueue(self, message):
        with self.lock:  # Ensure exclusive access
            self.queue.append(message)
            print(f"Message Enqueued: {message}")
 
    def dequeue(self):
        with self.lock:  # Ensure exclusive access
            if len(self.queue) == 0:
                print("Queue is empty!")
                return None
            message = self.queue.popleft()  # Get the front message
            print(f"Message Dequeued: {message}")
            return message
