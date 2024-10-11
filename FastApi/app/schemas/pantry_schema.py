"""
This module defines the schema for pantry models, including attributes such as
ID, user IDs, ingredient IDs, and the date last updated.
"""

from typing import List
from pydantic import BaseModel

class PantryModel(BaseModel):
    """
    A model representing a pantry.

    Attributes:
        id (int): Unique identifier for the pantry.
        userId (List[int]): List of user IDs associated with the pantry.
        ingredientIds (List[int]): List of ingredient IDs contained in the pantry.
        dateLastUpdated (str): Date when the pantry was last updated.
    """
    id: int
    userId: List[int]
    ingredientIds: List[int]
    dateLastUpdated: str

    # pylint: disable=too-few-public-methods
    class Config:
        """
        Pydantic configuration to allow arbitrary types and other settings.
        """
        arbitrary_types_allowed = True
