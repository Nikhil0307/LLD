import threading
import time
from collections import defaultdict
from typing import DefaultDict

from ..base_strategy import BaseStrategy

class FixedWindowRateLimitingStrategy(BaseStrategy):
    def __init__(self, limit: int = 10, client_limit: int = 0, window: int = 60):
        """
        limit: total number of requests allowed per window (global).
        client_limit: per-client request limit per window.
        window: duration of the window in seconds.
        """
        self.limit = limit
        self.client_limit = client_limit if client_limit > 0 else None
        self.window = window
        self.window_start = 0
        self.counter = 0
        self.tracker: DefaultDict[str, int] = defaultdict(int)
        self.lock = threading.Lock()

    def allow_request(self, client_id: str) -> bool:
        """
        client_id: str = client id
        """
        now = int(time.time())
        current_window = now - (now % self.window)
        with self.lock:
            if current_window != self.window_start:
                self.window_start = current_window
                if self.client_limit:
                    self.tracker.clear()
                    self.counter = self.tracker[client_id] = 1
                return True

            if self.counter >= self.limit:
                return False
            if self.client_limit and self.tracker[client_id] >= self.client_limit:
                return False

            self.counter += 1
            if self.client_limit:
                self.tracker[client_id] += 1
            return True