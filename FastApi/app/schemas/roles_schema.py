"""
This module defines the schema for roles models, including attributes such as ID and role name.
"""

from pydantic import BaseModel

class RolesModel(BaseModel):
    """
    A model representing a user role.

    Attributes:
        id (int): Unique identifier for the role.
        roleName (str): Name of the role (e.g., admin, user).
    """
    id: int
    roleName: str

    # pylint: disable=too-few-public-methods
    class Config:
        """
        Pydantic configuration to allow arbitrary types and other settings.
        """
        arbitrary_types_allowed = True
