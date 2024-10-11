"""
This module defines the schema for ingredient models, including attributes such as
ID, food IDs, quantity, measurement unit, expiration date, and measure.
"""

from typing import List
from pydantic import BaseModel

class IngredientModel(BaseModel):
    """
    A model representing an ingredient.

    Attributes:
        id (int): Unique identifier for the ingredient.
        foodId (List[int]): List of food IDs associated with the ingredient.
        quantity (int): Quantity of the ingredient.
        measurementUnit (str): The unit of measurement for the quantity.
        expirationDate (str): Expiration date of the ingredient.
        measure (int): Measure value of the ingredient.
    """
    id: int
    foodId: List[int]
    quantity: int
    measurementUnit: str
    expirationDate: str
    measure: int

    # pylint: disable=too-few-public-methods
    class Config:
        """
        Pydantic configuration to allow arbitrary types and other settings.
        """
        arbitrary_types_allowed = True
