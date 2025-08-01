from abc import ABC, abstractmethod
from notification_model import Notification

class BaseChannel(ABC):
    @abstractmethod
    def send(self, notification: Notification):
        pass
