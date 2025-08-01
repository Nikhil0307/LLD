from ..base_channel import BaseChannel
from ..notification_model import Notification, Channel
from ..clients.push_client import PushServiceClient
from ..models.push_payload import PushPayload

class PushChannel(BaseChannel):
    def __init__(self):
        self.client = PushServiceClient()

    def send(self, notification: Notification):
        if notification.channel != Channel.push:
            return False

        payload = PushPayload(
            queue=notification.queue,
            dlq=notification.dql,
            data=notification.data,
            priority=notification.priority,
            retry_count=notification.retries_left
        )

        return self.client.send(payload)

