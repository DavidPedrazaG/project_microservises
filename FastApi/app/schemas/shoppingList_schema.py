from typing import List
from pydantic import BaseModel, validator

class ShoppingListModel(BaseModel):
    id: int
    user: List[int]
    ingredientId: List[int]
    dateCreated: str