from typing import List
from pydantic import BaseModel, validator

class NutritionalInfoModel(BaseModel):

    id: int
    calories: int
    carbohydrates: int
    proteins: int
    fats: int
    vitamins: str
    minerals: str