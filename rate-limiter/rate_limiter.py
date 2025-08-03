from base_strategy import BaseStrategy

class RateLimiter:
    def __init__(self, strategy: BaseStrategy):
        self.strategy = strategy

    def allow_request(self, client_id: str) -> bool:
        return self.strategy.allow_request(client_id)
