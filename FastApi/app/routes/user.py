"""
User routes for managing user-related operations in the FastAPI application.
This module includes user creation, update, deletion, and login functionality.
"""

from schemas.user_schema import UserModel as UserSchema  # Third-party import
from config.database import UserModel  # Third-party import
from helpers.api_key_auth import get_api_key  # Third-party import
from fastapi import APIRouter, Depends, HTTPException  # First-party import



router = APIRouter()

@router.post("/users/")
async def create_user(user: UserSchema) -> UserModel:
    """
    Create a new user.

    Args:
        user (UserSchema): The user data to create.

    Returns:
        UserModel: The created user.
    """
    db_user = UserModel.create(
        name=user.name,
        email=user.email,
        password=user.password,
        cc=user.cc,
        lastName=user.lastname,
        phoneNumber=user.phoneNumber,
        role=user.role
    )
    return db_user

@router.put("/users/{user_id}", dependencies=[Depends(get_api_key)])
async def update_user(cc: str, user: UserSchema) -> UserModel:
    """
    Update an existing user.

    Args:
        cc (str): The credit card number of the user.
        user (UserSchema): The updated user data.

    Returns:
        UserModel: The updated user.

    Raises:
        HTTPException: If the user is not found.
    """
    db_user = UserModel.get(UserModel.cc == cc)  # Use the cc parameter
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    db_user.name = user.name
    db_user.lastName = user.lastname
    db_user.email = user.email
    db_user.password = user.password  # Consider hashing this password
    db_user.phoneNumber = user.phoneNumber
    db_user.save()
    return db_user

@router.delete("/users/{cc}", dependencies=[Depends(get_api_key)])
async def delete_user(cc: str) -> dict:
    """
    Delete a user.

    Args:
        cc (str): The credit card number of the user to delete.

    Returns:
        dict: A message indicating the result.

    Raises:
        HTTPException: If the user is not found.
    """
    rows_deleted = UserModel.delete().where(UserModel.cc == cc).execute()
    if rows_deleted:
        return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")

@router.post("/login")
async def login(email: str, password: str) -> str:
    """
    User login.

    Args:
        email (str): The email of the user.
        password (str): The user's password.

    Returns:
        str: The API key if login is successful.

    Raises:
        HTTPException: If the login fails.
    """
    user = UserModel.get(UserModel.email == email)
    if user and user.password == password:  # Consider checking hashed passwords
        return os.getenv("API_KEY")
    raise HTTPException(status_code=401, detail="Invalid email or password")
