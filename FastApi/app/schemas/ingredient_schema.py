from typing import List
from pydantic import BaseModel, validator

class IngredientModel(BaseModel):

    id: int
    foodId: List[int]
    quantity: int
    measurementUnit: str
    expirationDate: str
    meassure: int