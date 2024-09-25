from typing import List
from pydantic import BaseModel, validator

class FoodModel(BaseModel):
    """A simple model for food items"""
    id: int
    name: set
    macronutrientsId:int
    micronutrientsId: int