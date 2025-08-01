from ..models.email_payload import EmailPayload

class EmailServiceClient:
    def __init__(self):
        # Initialize auth/session/etc.
        pass

    def send(self, payload: EmailPayload) -> bool:
        try:
            print(f"Sending email to {payload.to}")
            return True
        except Exception as e:
            print(f"Failed to send SMS: {e}")
            return False
