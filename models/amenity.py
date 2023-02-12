#!/usr/bin/python3
"""
This module defines the amenity class.
Inherits from the BaseModel class.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Defines the Amenity class.
    Attributes:
        name: name of amenity.
    """
    name = ''
