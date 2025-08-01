from ..base_channel import BaseChannel
from ..notification_model import Notification, Channel
from ..clients.email_client import EmailServiceClient
from ..models.email_payload import EmailPayload


class EmailChannel(BaseChannel):
    def __init__(self):
        self.client = EmailServiceClient()

    def send(self, notification: Notification):
        if notification.channel != Channel.email:
            return False

        payload = EmailPayload(
            to=notification.to,
            cc=notification.cc,
            subject=notification.subject,
            body=notification.body,
            attachment=notification.attachment,
            metadata=notification.metadata,
            priority=notification.priority,
            retry_count=notification.retries_left
        )

        return self.client.send(payload)

