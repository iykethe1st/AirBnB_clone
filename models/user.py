#!/usr/bin/python3
"""
This module defines the user class.
inherits the BaseModel class.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Defines the User attributes.
    Attributes:
        email: User email.
        password: User password.
        first_name: User first name.
        last_name = User last name.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
