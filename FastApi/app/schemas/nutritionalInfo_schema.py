"""
This module defines the schema for nutritional information models, including attributes such as
ID, calories, macronutrients, and micronutrients.
"""

from pydantic import BaseModel

class NutritionalInfoModel(BaseModel):
    """
    A model representing nutritional information.

    Attributes:
        id (int): Unique identifier for the nutritional entry.
        calories (int): Number of calories in the food.
        carbohydrates (int): Amount of carbohydrates in grams.
        proteins (int): Amount of proteins in grams.
        fats (int): Amount of fats in grams.
        vitamins (str): Vitamins present in the food.
        minerals (str): Minerals present in the food.
    """
    id: int
    calories: int
    carbohydrates: int
    proteins: int
    fats: int
    vitamins: str
    minerals: str

    # pylint: disable=too-few-public-methods
    class Config:
        """
        Pydantic configuration to allow arbitrary types and other settings.
        """
        arbitrary_types_allowed = True
