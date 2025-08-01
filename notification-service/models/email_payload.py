from pydantic import BaseModel
from typing import Optional, Dict, List

class EmailPayload(BaseModel):
    to: str
    cc: Optional[List[str]] = None
    subject: str
    body: Optional[str] = None
    attachment: Optional[bytes] = None
    metadata: Optional[Dict[str, str]] = None
    priority: Optional[str] = "normal"
    retry_count: int = 3
