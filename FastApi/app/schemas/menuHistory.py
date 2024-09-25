from typing import List
from pydantic import BaseModel, validator

class MenuHistoryModel(BaseModel):
    id: int
    userId: List[int]
    weeklyMenuId: List[int]
    dateCreated: str