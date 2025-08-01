from pydantic import BaseModel
from typing import Optional, Dict

class SMSPayload(BaseModel):
    phone_number: str
    text: str
    sender_id: Optional[str] = None
    metadata: Optional[Dict[str, str]] = None
    priority: Optional[str] = "normal"
    retry_count: int = 3
