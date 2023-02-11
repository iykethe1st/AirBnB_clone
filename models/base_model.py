#!/usr/bin/python3
# Author: Chisom Ibekwe
"""This module contains the BaseModel class that defines all common
attributes/methods for other classes."""

import models
import cmd
from uuid import uuid4
from datetime import datetime


class BaseModel(cmd.Cmd):
    """BaseModel <class> - defines the common attributs/methods for othr classes."""

    def __init__(self, *args, **kwargs):
        """
        Initializes a new BaseModel instane.
        Assigns a unique id to it, time created,
        and time updated (updates each time the object is changed).
        """
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, tform)
                else:
                    self.__dict__[k] = v
        else:
            models.storage.new(self)

    def __str__(self):
        return '[{}] ({}) {}'.format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the instance attribute - updated_at with the current datetime."""
        self.updated_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dicitionary containing all keys/values of __dict__  of the instance.
        """
        json = self.__dict__
        json['__class__'] = self.__class__.__name__
        json['created_at'] = json['created_at'].isoformat()
        json['updated_at'] = json['updated_at'].isoformat()
        return json
