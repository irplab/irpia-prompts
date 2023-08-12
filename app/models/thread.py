"""
Model for suggestion thread
"""
from pydantic import BaseModel


class Thread(BaseModel):
    """
    Model for suggestion thread
    """
    uri: str
