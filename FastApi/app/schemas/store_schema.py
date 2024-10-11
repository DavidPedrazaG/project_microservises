"""
This module defines the schema for store models, including attributes such as
ID, name, location, and inventory IDs.
"""

from typing import List
from pydantic import BaseModel

class StoreModel(BaseModel):
    """
    A model representing a store.

    Attributes:
        id (int): Unique identifier for the store.
        name (str): Name of the store.
        location (str): Location of the store.
        inventoryId (List[int]): List of inventory IDs associated with the store.
    """
    id: int
    name: str
    location: str
    inventoryId: List[int]

    # pylint: disable=too-few-public-methods
    class Config:
        """
        Pydantic configuration to allow arbitrary types and other settings.
        """
        arbitrary_types_allowed = True
