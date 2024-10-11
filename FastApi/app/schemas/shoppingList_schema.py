"""
This module defines the schema for shopping list models, including attributes such as
ID, user IDs, ingredient IDs, and the date created.
"""

from typing import List
from pydantic import BaseModel

class ShoppingListModel(BaseModel):
    """
    A model representing a shopping list.

    Attributes:
        id (int): Unique identifier for the shopping list.
        user (List[int]): List of user IDs associated with the shopping list.
        ingredientId (List[int]): List of ingredient IDs included in the shopping list.
        dateCreated (str): Date when the shopping list was created.
    """
    id: int
    user: List[int]
    ingredientId: List[int]
    dateCreated: str

    # pylint: disable=too-few-public-methods
    class Config:
        """
        Pydantic configuration to allow arbitrary types and other settings.
        """
        arbitrary_types_allowed = True
