from pydantic import BaseModel
from typing import Optional, Dict, List

class PushPayload(BaseModel):
    queue: str
    dlq: Optional[str] = "default_dead_letter_queue"
    data: Optional[str or bytes] = None
    priority: Optional[str] = "normal"
    retry_count: int = 3
