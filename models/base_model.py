#!/usr/bin/python3
# Author: Chisom Ibekwe
"""This module contains the BaseModel class that defines all common
attributes/methods for other classes."""
import cmd
import uuid
import datetime


class BaseModel(cmd.Cmd):
    """BaseModel <class> - defines the common attributs/methods for othr classes."""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instane.
        Assigns a unique id to it, time created,
        and time updated (updates each time the object is changed).
        """
        if kwargs:
            out = ['__class__', 'created_at', 'updated_at']
            self.__dict__.update((key, val) for key, val in kwargs.items() if key not in out)
            self.created_at = datetime.datetime.today()
            self.updated_at = self.created_at
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.today()
            self.updated_at = self.created_at

    def __str__(self):
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the instance attribute - updated_at with the current datetime."""
        self.updated_at = datetime.datetime.today()

    def to_dict(self):
        """
        Returns a dicitionary containing all keys/values of __dict__  of the instance.
        """
        json = self.__dict__
        json['__class__'] = self.__class__.__name__
        json['created_at'] = json['created_at'].isoformat()
        json['updated_at'] = json['updated_at'].isoformat()
        return json
