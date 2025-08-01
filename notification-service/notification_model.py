from typing import Optional, Dict, List

from pydantic import BaseModel
from enum import Enum

class Channel(str, Enum):
    email = "email"
    sms = "sms"
    push = "push"

class Priority(str, Enum):
    high = "high"
    normal = "normal"
    low = "low"

class Notification(BaseModel):
    id: str
    channel: Channel
    priority: Priority = Priority.normal
    retries_left: int = 3
    to: Optional[str]
    cc: Optional[List[str]]
    body: Optional[str]
    subject: Optional[str]
    attachment: Optional[bytes]
    recipient: Optional[str]
    subject: Optional[str]
    message: Optional[str]
    metadata: Optional[Dict[str,str]] = None
    queue: Optional[str]
    dql: Optional[str] = "default_dead_letter_queue"
    data: Optional[str or bytes]
