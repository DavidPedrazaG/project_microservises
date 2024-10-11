"""
This module defines the schema for user models, including attributes such as
ID, identification number, name, lastname, password, email, phone number, and role.
"""

from pydantic import BaseModel

class UserModel(BaseModel):
    """
    A model representing a user.

    Attributes:
        id (int): Unique identifier for the user.
        cc (str): Identification number (e.g., citizen card).
        name (str): First name of the user.
        lastname (str): Last name of the user.
        password (str): User's password.
        email (str): User's email address.
        phoneNumber (str): User's phone number.
        role (int): User's role identifier.
    """
    id: int
    cc: str
    name: str
    lastname: str
    password: str
    email: str
    phoneNumber: str
    role: int

    # pylint: disable=too-few-public-methods
    class Config:
        """
        Pydantic configuration to allow arbitrary types and other settings.
        """
        arbitrary_types_allowed = True
