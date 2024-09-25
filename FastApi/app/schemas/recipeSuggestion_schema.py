from typing import List
from pydantic import BaseModel, validator

class RecipeSuggestionModel(BaseModel):
    id: int
    userId: List[int]
    suggestedRecipeId: List[int]
    matchedIngredientId: List[int]
    missingIngredientesId: List[int]
    dateSuggested: str