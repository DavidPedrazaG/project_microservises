from typing import List
from pydantic import BaseModel, validator

class RolesModel(BaseModel):

    id: int
    roleName: str