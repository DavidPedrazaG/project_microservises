import os
from fastapi import APIRouter, Depends, HTTPException
from schemas.user_schema import UserModel as UserSchema
from config.database import UserModel
from helpers.api_key_auth import get_api_key

router = APIRouter()

@router.post("/users/")
async def create_user(user: UserSchema):
    db_user = UserModel.create(name=user.name, email=user.email, password=user.password, cc = user.cc, lastName=user.lastname, phoneNumber =user.phoneNumber, role=user.role)
    return db_user

@router.put("/users/{user_id}", dependencies=[Depends(get_api_key)])
async def update_user(cc: str, user: UserSchema):
    db_user = UserModel.get(cc==UserModel.cc)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    db_user.name = user.name
    db_user.lastName = user.lastname
    db_user.email = user.email
    db_user.password = user.password
    db_user.phoneNumber = user.phoneNumber
    
    db_user.save()
    return db_user

@router.delete("/users/{user_id}", dependencies=[Depends(get_api_key)])
async def delete_user(cc: str):
    rows_deleted = UserModel.delete().where(UserModel.cc == cc).execute()
    if rows_deleted:
        return {"message": "User deleted successfully"}
    raise HTTPException(status_code=404, detail="User not found")

@router.post("/login", dependencies=None)
async def login(email:str, password:str):
    user = UserModel.get(UserModel.email == email)
    if user:
        if user.password == password:
            return os.getenv("API_KEY")