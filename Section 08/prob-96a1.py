import time
from collections import deque
 
class RateLimiter:
    def __init__(self, limit, time_window):
        self.limit = limit  # Maximum number of requests
        self.time_window = time_window  # Time window in seconds
        self.requests_log = {}  # Dictionary to store user requests
 
    def allow_request(self, user_id):
        current_time = time.time()
 
        # Initialize request log for the user if not present
        if user_id not in self.requests_log:
            self.requests_log[user_id] = deque()
 
        # Clean up old requests outside the current time window
        while self.requests_log[user_id] and self.requests_log[user_id][0] < current_time - self.time_window:
            self.requests_log[user_id].popleft()
 
        # Check if the user has reached the request limit
        if len(self.requests_log[user_id]) < self.limit:
            # Allow the request and log the timestamp
            self.requests_log[user_id].append(current_time)
            print(f"Request allowed for user {user_id}.")
            return True
        else:
            # Deny the request
            print(f"Request denied for user {user_id}. Rate limit exceeded.")
            return False
 
# Example usage
limiter = RateLimiter(limit=5, time_window=60)  # 5 requests per minute
 
# Simulate user requests
user_id = "user123"
for i in range(7):
    limiter.allow_request(user_id)
    time.sleep(10)  # Simulate a delay between requests
