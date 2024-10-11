"""
This module defines the schema for menu models, including attributes such as
ID, weekly menu IDs, day, hour, and type.
"""

from typing import List
from pydantic import BaseModel

class MenuModel(BaseModel):
    """
    A model representing a menu.

    Attributes:
        id (int): Unique identifier for the menu.
        weeklyMenuId (List[int]): List of IDs for the associated weekly menus.
        day (str): Day of the week for the menu.
        hour (str): Time of the day for the menu.
        type (str): Type of the menu (e.g., breakfast, lunch, dinner).
    """
    id: int
    weeklyMenuId: List[int]
    day: str
    hour: str
    type: str

    # pylint: disable=too-few-public-methods
    class Config:
        """
        Pydantic configuration to allow arbitrary types and other settings.
        """
        arbitrary_types_allowed = True
