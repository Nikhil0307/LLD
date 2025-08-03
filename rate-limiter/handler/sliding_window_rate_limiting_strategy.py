import threading
import time
from collections import defaultdict, deque
from typing import DefaultDict, Deque

from ..base_strategy import BaseStrategy

class SlidingWindowLogStrategy(BaseStrategy):
    def __init__(self, limit: int = 10, window: int = 60):
        self.limit = limit
        self.window = window
        self.requests_log: DefaultDict[str, Deque[int]] = defaultdict(deque)
        self.lock = threading.Lock()

    def allow_request(self, client_id: str) -> bool:
        now = int(time.time())
        with self.lock:
            q = self.requests_log[client_id]

            while q and now - q[0] >= self.window:
                q.popleft()

            if len(q) < self.limit:
                q.append(now)
                return True
            return False
