from typing import List
from pydantic import BaseModel, validator

class GroupModel(BaseModel):
    id: int
    name: str
    adminId: List[int]
    weeklyMenuId: List[int]