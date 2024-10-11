"""
This module defines the schema for group models, including attributes such as
ID, name, admin IDs, and weekly menu IDs.
"""

from typing import List
from pydantic import BaseModel

class GroupModel(BaseModel):
    """
    A model representing a group.

    Attributes:
        id (int): Unique identifier for the group.
        name (str): Name of the group.
        adminId (List[int]): List of IDs for the group administrators.
        weeklyMenuId (List[int]): List of IDs for the weekly menus associated with the group.
    """
    id: int
    name: str
    adminId: List[int]
    weeklyMenuId: List[int]

    # pylint: disable=too-few-public-methods
    class Config:
        """
        Pydantic configuration to allow arbitrary types and other settings.
        """
        arbitrary_types_allowed = True
