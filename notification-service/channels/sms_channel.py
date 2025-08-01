from ..base_channel import BaseChannel
from ..notification_model import Notification, Channel
from ..clients.sms_client import SmsServiceClient
from ..models.sms_payload import SMSPayload

class SmsChannel(BaseChannel):
    def __init__(self, provider_key="demo"):
        self.client = SmsServiceClient(provider_key=provider_key)

    def send(self, notification: Notification) -> bool:
        if notification.channel != Channel.sms:
            return False

        payload = SMSPayload(
            phone_number=notification.recipient,
            text=notification.message,
            sender_id=notification.metadata.get("sender_id") if notification.metadata else None,
            metadata=notification.metadata,
            priority=notification.priority.value,
            retry_count=notification.retries_left
        )
        return self.client.send(payload)
