"""
This module defines the schema for weekly menu models, including attributes such as
the unique identifier for the weekly menu.
"""

from pydantic import BaseModel

class WeeklyMenuModel(BaseModel):
    """
    A model representing a weekly menu.

    Attributes:
        id (int): Unique identifier for the weekly menu.
    """
    id: int

    # pylint: disable=too-few-public-methods
    class Config:
        """
        Pydantic configuration to allow arbitrary types and other settings.
        """
        arbitrary_types_allowed = True
