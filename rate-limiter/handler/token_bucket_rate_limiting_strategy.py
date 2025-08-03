import threading
import time
from collections import defaultdict
from typing import DefaultDict

from ..base_strategy import BaseStrategy

class TokenBucketStrategy(BaseStrategy):
    def __init__(self, refill_rate: float = 1.0, capacity: int = 10):
        self.refill_rate = refill_rate  # tokens per second
        self.capacity = capacity
        self.tokens: DefaultDict[str, float] = defaultdict(lambda: capacity)
        self.last_refill: DefaultDict[str, float] = defaultdict(time.time)
        self.lock = threading.Lock()

    def allow_request(self, client_id: str) -> bool:
        now = time.time()
        elapsed = now - self.last_refill[client_id]

        new_tokens = elapsed * self.refill_rate
        with self.lock:
            self.tokens[client_id] = min(self.capacity, self.tokens[client_id] + new_tokens)
            self.last_refill[client_id] = now

            if self.tokens[client_id] >= 1:
                self.tokens[client_id] -= 1
                return True
            return False
