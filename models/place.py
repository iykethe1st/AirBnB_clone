#!/usr/bin/python3
"""
This module defines the Place class.
Inherits the BaseModel class.
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Defines the place class.
    Attributes:
        city_id: (str) id of the city.
        user_id: (str) user id.
        name: (str) name of place.
        description: (str) place description.
        number_rooms: (int) number of rooms.
        number_bathrooms: (int) number of bathrooms.
        max_guest: (int)
        price_by_night: (int)
        latitude: (float)
        amenity_ids: (list of strings) list of amenity ids.
    """
    city_id = ''
    user_id = ''
    name = ''
    description = ''
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    amenity_ids = []

