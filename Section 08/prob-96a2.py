import time
 
class TokenBucket:
    def __init__(self, capacity, refill_rate):
        self.capacity = capacity  # Max number of tokens
        self.tokens = capacity  # Current number of tokens
        self.refill_rate = refill_rate  # Tokens added per second
        self.last_refill_time = time.time()  # Last refill timestamp
 
    def allow_request(self):
        current_time = time.time()
 
        # Refill tokens based on time passed since last refill
        time_passed = current_time - self.last_refill_time
        refill_tokens = time_passed * self.refill_rate
        self.tokens = min(self.capacity, self.tokens + refill_tokens)
        self.last_refill_time = current_time
 
        if self.tokens >= 1:
            self.tokens -= 1
            print("Request allowed.")
            return True
        else:
            print("Request denied. No tokens available.")
            return False
 
# Example usage
bucket = TokenBucket(capacity=5, refill_rate=1)  # 5 tokens max, 1 token per second
 
# Simulate user requests
for i in range(7):
    bucket.allow_request()
    time.sleep(0.5)  # Simulate delay between requests
