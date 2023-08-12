"""
Model for keyword suggestions
"""
from pydantic import BaseModel


class Keywords(BaseModel):
    """
    Model for keyword suggestions
    """
    keywords: list[str]
