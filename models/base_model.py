#!/usr/bin/python3
"""Defining the BaseModel class """
from uuid import uuid4
from datetime import datetime
import uuid


class BaseModel:
    """ The parent class ofvthe AIRBNB project that puts in place initialization, serialization and deserialization
    """
    def __init__(self):
        """ initialization of class attributes
        args:
            id - string - assign with an uuid when an instance is created
            created_at - datetime - assign with the current datetime when an instance is created
            updated_at - datetime - assign with the current datetime when an instance is created and it will be updated every time you change your object
        """
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """prints the string representation of the objects
        print class name, id, __dict__
        """
        return(f"[{self.__class__.__name__}] ({self.id}) {self.__class__.__dict__}")
       
    def save(self):
        """ updates the public instance attribute updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        save()

    def to_dict(self):
        """returns a dictionary containing all keys/values of __dict__ of the instance:
        by using:
            self.__dict__, only instance attributes set will be returned
            a key __class__ must be added to this dictionary with the class name of the object
        """
        """"###Not sure how to implement it ####"""
