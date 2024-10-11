"""
This module defines the schema for measure models, including attributes such as
measure ID and measure name.
"""

from pydantic import BaseModel

class MeasureModel(BaseModel):
    """
    A model representing a measure.

    Attributes:
        measureId (int): Unique identifier for the measure.
        measureName (str): Name of the measure.
    """
    measureId: int
    measureName: str

    # pylint: disable=too-few-public-methods
    class Config:
        """
        Pydantic configuration to allow arbitrary types and other settings.
        """
        arbitrary_types_allowed = True
