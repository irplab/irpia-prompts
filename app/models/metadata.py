"""
Resource metadata representation
"""
from pydantic import BaseModel


class Metadata(BaseModel):
    """
    Resource metadata representation
    """
    title: str
    description: str | None = None
