"""
This module defines the schema for comments in the system. It includes
a Pydantic model that ensures data validation for comments, including 
attributes like recipe ID, user ID, content, rating, and date posted.
"""

from typing import List
from pydantic import BaseModel, validator

class CommentModel(BaseModel):
    """
    Model to represent a comment in the system.

    Attributes:
        id (int): Unique identifier for the comment.
        recipe_id (List[int]): List of related recipe IDs.
        user_id (List[int]): List of related user IDs.
        content (str): The content of the comment.
        rating (int): The rating of the comment, must be between 1 and 5.
        date_posted (str): The date the comment was posted.
    """
    id: int
    recipe_id: List[int]
    user_id: List[int]
    content: str
    rating: int
    date_posted: str

    @validator('rating')
    # pylint: disable=no-self-argument
    def check_rating(cls, value):
        """
        Validates that the rating is between 1 and 5.

        Args:
            value (int): The rating value.

        Returns:
            int: The validated rating value.

        Raises:
            ValueError: If the rating is outside the allowed range (1-5).
        """
        if value < 1 or value > 5:
            raise ValueError('Rating must be between 1 and 5')
        return value

    class Config:
        """
        Pydantic configuration to allow arbitrary types and other settings.
        """
        arbitrary_types_allowed = True

        # pylint: disable=too-few-public-methods
