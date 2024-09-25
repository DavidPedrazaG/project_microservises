from typing import List
from pydantic import BaseModel, validator

class PurchaseHistoryModel(BaseModel):
    id: int
    userId: List[int]
    ingredientsId: List[int]
    purchaseDate: str