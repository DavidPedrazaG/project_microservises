"""
This module defines the schema for purchase history models, including attributes such as
ID, user IDs, ingredient IDs, and the purchase date.
"""

from typing import List
from pydantic import BaseModel

class PurchaseHistoryModel(BaseModel):
    """
    A model representing a purchase history entry.

    Attributes:
        id (int): Unique identifier for the purchase history entry.
        userId (List[int]): List of user IDs associated with the purchase.
        ingredientsId (List[int]): List of ingredient IDs purchased.
        purchaseDate (str): Date when the purchase was made.
    """
    id: int
    userId: List[int]
    ingredientsId: List[int]
    purchaseDate: str

    # pylint: disable=too-few-public-methods
    class Config:
        """
        Pydantic configuration to allow arbitrary types and other settings.
        """
        arbitrary_types_allowed = True
