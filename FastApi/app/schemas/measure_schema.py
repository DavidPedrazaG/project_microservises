from typing import List
from pydantic import BaseModel, validator

class MeasureModel(BaseModel):

    measureId: int 
    measureName: str