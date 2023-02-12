#!/usr/bin/python3
"""
This module defines the state class.
inherits the BaseModel class.
"""
from models.base_models import BaseModel


class State(BaseModel):
    """
    Defines the state info.
    Attributes:
        name: state name
    """
    state = ''
