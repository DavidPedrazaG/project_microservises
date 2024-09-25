from typing import List
from pydantic import BaseModel, validator

class WeeklyMenuModel(BaseModel):
    id: int