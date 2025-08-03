from abc import ABC, abstractmethod

class BaseStrategy(ABC):
    @abstractmethod
    def allow_request(self, client_id: str) -> bool:
        pass