from typing import List
from pydantic import BaseModel, validator

class StoreModel(BaseModel):
    id: int
    name: str
    location: str
    inventoryId: List[int]