"""
This module defines the schema for recipe suggestion models, including attributes such as
ID, user IDs, suggested recipe IDs, matched ingredient IDs, missing ingredient IDs, and the date suggested.
"""

from typing import List
from pydantic import BaseModel

class RecipeSuggestionModel(BaseModel):
    """
    A model representing a recipe suggestion.

    Attributes:
        id (int): Unique identifier for the recipe suggestion.
        userId (List[int]): List of user IDs associated with the suggestion.
        suggestedRecipeId (List[int]): List of suggested recipe IDs.
        matchedIngredientId (List[int]): List of matched ingredient IDs found in the user's pantry.
        missingIngredientesId (List[int]): List of ingredient IDs that are missing for the recipe.
        dateSuggested (str): Date when the recipe was suggested.
    """
    id: int
    userId: List[int]
    suggestedRecipeId: List[int]
    matchedIngredientId: List[int]
    missingIngredientesId: List[int]
    dateSuggested: str

    # pylint: disable=too-few-public-methods
    class Config:
        """
        Pydantic configuration to allow arbitrary types and other settings.
        """
        arbitrary_types_allowed = True
