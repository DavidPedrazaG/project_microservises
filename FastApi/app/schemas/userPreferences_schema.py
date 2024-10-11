"""
This module defines the schema for user preferences models, including attributes such as
ID, user IDs, dietary restrictions, preferred cuisines, and allergens.
"""

from typing import List
from pydantic import BaseModel

class UserPreferencesModel(BaseModel):
    """
    A model representing user preferences.

    Attributes:
        id (int): Unique identifier for the user preferences.
        userId (List[int]): List of user IDs associated with the preferences.
        dietaryRestrictions (str): Dietary restrictions of the user.
        preferredCuisines (str): Preferred cuisines of the user.
        allergens (str): Allergens that the user is sensitive to.
    """
    id: int
    userId: List[int]
    dietaryRestrictions: str
    preferredCuisines: str
    allergens: str

    # pylint: disable=too-few-public-methods
    class Config:
        """
        Pydantic configuration to allow arbitrary types and other settings.
        """
        arbitrary_types_allowed = True
