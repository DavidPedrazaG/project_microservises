"""
This module defines the schema for recipe models, including attributes such as
ID, name, type of food, difficulty, preparation time, nutritional information ID, 
images, and preparation process.
"""

from typing import List
from pydantic import BaseModel

class RecipeModel(BaseModel):
    """
    A model representing a recipe.

    Attributes:
        id (int): Unique identifier for the recipe.
        name (str): Name of the recipe.
        typeOfFood (str): Type of food (e.g., appetizer, main course).
        difficulty (str): Difficulty level of the recipe (e.g., easy, medium, hard).
        preparationTime (int): Time required to prepare the recipe in minutes.
        nutritionalInfoId (int): ID of the nutritional information associated with the recipe.
        images (List[str]): List of image URLs for the recipe.
        preparationProcess (str): Step-by-step instructions for preparing the recipe.
    """
    id: int
    name: str
    typeOfFood: str
    difficulty: str
    preparationTime: int
    nutritionalInfoId: int
    images: List[str]
    preparationProcess: str

    # pylint: disable=too-few-public-methods
    class Config:
        """
        Pydantic configuration to allow arbitrary types and other settings.
        """
        arbitrary_types_allowed = True
