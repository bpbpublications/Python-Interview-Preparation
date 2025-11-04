import redis
 
# Create a Redis connection
r = redis.Redis()
 
# Enqueue operation
def enqueue(message):
    r.rpush('message_queue', message)
    print(f"Message Enqueued: {message}")
 
# Dequeue operation
def dequeue():
    message = r.lpop('message_queue')
    if message:
        print(f"Message Dequeued: {message.decode()}")
    else:
        print("Queue is empty!")
 
# Example usage
enqueue("Hello, Redis!")
dequeue()
