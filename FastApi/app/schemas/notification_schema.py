"""
This module defines the schema for notification models, including attributes such as
ID, user IDs, message, date sent, and type.
"""

from typing import List
from pydantic import BaseModel

class NotificationModel(BaseModel):
    """
    A model representing a notification.

    Attributes:
        id (int): Unique identifier for the notification.
        userId (List[int]): List of user IDs associated with the notification.
        message (str): The content of the notification message.
        dateSent (str): Date when the notification was sent.
        type (str): Type of the notification (e.g., alert, reminder).
    """
    id: int
    userId: List[int]
    message: str
    dateSent: str
    type: str

    # pylint: disable=too-few-public-methods
    class Config:
        """
        Pydantic configuration to allow arbitrary types and other settings.
        """
        arbitrary_types_allowed = True
