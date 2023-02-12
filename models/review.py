#!/usr/bin/python3
"""
This module defines the Review class.
Inherits the BaseModel class.
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """
    Defines the Review class.
    Attributes:
        place_id: (str) place id.
        user_id: (str) user id.
        text: (str).
    """
    place_id = ''
    user_id = ''
    text = ''
