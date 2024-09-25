from typing import List
from pydantic import BaseModel, validator

class UserModel(BaseModel):
    id: int
    cc : str
    name: str
    lastname: str
    password: str
    email: str
    phoneNumber: str
    role: int