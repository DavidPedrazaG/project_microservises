"""
This module defines the schema for menu history models, including attributes such as
ID, user IDs, weekly menu IDs, and the date created.
"""

from typing import List
from pydantic import BaseModel

class MenuHistoryModel(BaseModel):
    """
    A model representing the history of menus.

    Attributes:
        id (int): Unique identifier for the menu history entry.
        userId (List[int]): List of user IDs associated with the menu.
        weeklyMenuId (List[int]): List of IDs for the associated weekly menus.
        dateCreated (str): Date when the menu was created.
    """
    id: int
    userId: List[int]
    weeklyMenuId: List[int]
    dateCreated: str

    # pylint: disable=too-few-public-methods
    class Config:
        """
        Pydantic configuration to allow arbitrary types and other settings.
        """
        arbitrary_types_allowed = True
