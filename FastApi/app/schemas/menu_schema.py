from typing import List
from pydantic import BaseModel, validator

class MenuModel(BaseModel):
    id: int
    weeklyMenuId: List[int]
    day: str
    hour: str
    type: str