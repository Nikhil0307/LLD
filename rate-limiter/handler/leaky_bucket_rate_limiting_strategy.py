import threading
import time
from collections import defaultdict
from typing import DefaultDict

from ..base_strategy import BaseStrategy

class LeakyBucketStrategy(BaseStrategy):
    def __init__(self, rate: float = 1.0, capacity: int = 10):
        self.rate = rate
        self.capacity = capacity
        self.buckets: DefaultDict[str, float] = defaultdict(lambda: 0.0)
        self.last_checked: DefaultDict[str, float] = defaultdict(time.time)
        self.lock = threading.Lock()

    def allow_request(self, client_id: str) -> bool:
        now = time.time()
        elapsed = now - self.last_checked[client_id]
        leaked = elapsed * self.rate
        with self.lock:
            self.buckets[client_id] = max(0.0, self.buckets[client_id] - leaked)
            self.last_checked[client_id] = now

            if self.buckets[client_id] < self.capacity:
                self.buckets[client_id] += 1
                return True
            return False
