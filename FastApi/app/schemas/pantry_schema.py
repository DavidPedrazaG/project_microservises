from typing import List
from pydantic import BaseModel, validator

class PantryModel(BaseModel):
    id: int
    userId: List[int]
    ingredientIds : List[int]
    dateLastUpdated: str