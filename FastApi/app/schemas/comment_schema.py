from typing import List
from pydantic import BaseModel, validator

class CommentModel(BaseModel):

    id: int
    recipe_id: List[int]
    user_id: List[int]
    content: str
    rating: int
    date_posted: str