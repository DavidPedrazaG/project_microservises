from typing import List
from pydantic import BaseModel, validator

class RecipeModel(BaseModel):
    id: int
    name: str
    typeOfFood: str
    difficulty: str
    preparationTime: int
    nutritionalInfoId: int
    images: List[str]
    preparationProcess: str
