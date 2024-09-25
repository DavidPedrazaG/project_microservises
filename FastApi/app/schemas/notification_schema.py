from typing import List
from pydantic import BaseModel, validator

class NotificationModel(BaseModel):
    id: int
    userId: List[int]
    message: str
    dateSent: str
    type: str