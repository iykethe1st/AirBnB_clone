#!/usr/bin/python3
"""
This module defines the city class.
Inherits from the BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    Defines the city info.
    Attributes:
        state_id: state id
        name: name of city
    """
    state_id = ''
    name = ''
