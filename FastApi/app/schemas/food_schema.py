""" 
This module defines the schema for food items, including attributes such as
ID, name, macronutrients, and micronutrients.
"""

from pydantic import BaseModel

class FoodModel(BaseModel):
    """
    A simple model for food items.

    Attributes:
        id (int): Unique identifier for the food item.
        name (str): Name of the food item.
        macronutrientsId (int): Reference ID for the macronutrients.
        micronutrientsId (int): Reference ID for the micronutrients.
    """
    id: int
    name: str
    macronutrientsId: int
    micronutrientsId: int

    # pylint: disable=too-few-public-methods
    class Config:
        """
        Pydantic configuration to allow arbitrary types and other settings.
        """
        arbitrary_types_allowed = True
