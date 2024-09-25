from typing import List
from pydantic import BaseModel, validator

class UserPreferencesModel(BaseModel):
    id: int
    userId: List[int]
    dietaryRestrictions: str
    preferredCuisines: str
    allergens: str