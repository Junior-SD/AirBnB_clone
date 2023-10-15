#!/usr/bin/python3
"""Defining the BaseModel class """
from uuid import uuid4
from datetime import datetime
import uuid
import models


class BaseModel:
    """ The parent class ofvthe AIRBNB project
    """
    def __init__(self, *args, **kwargs):
        """ initialization of class attributes
        args:
            id - string - assign with an uuid when an instance is created
            created_at - datetime - shows when an instance was created
            updated_at - datetime - updates an instance created
        """
        time_format = "%Y-%m-%dT%H:%M:%S.%f"
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, time_format))
                elif key != '__class__':
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """prints the string representation of the objects
        print class name, id, __dict__
        """
        c = self.__class__.__name__
        dic = self.__class__.__dict__
        return (f"[{c}] ({self.id}) {dic}")

    def save(self):
        """ updates the public instance attribute
        updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        """return self.save()"""
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__
        by using:
            self.__dict__, only instance attributes set will be returned
            a key __class__ must be added to this dictionary with
            the class name of the object
        """
        new_dict = self.__dict__.copy()
        if "created_at" in new_dict:
            new_dict["created_at"] = self.created_at.isoformat()
        if "updated_at" in new_dict:
            new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
