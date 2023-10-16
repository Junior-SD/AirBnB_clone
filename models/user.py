#!/use/bin/python3
""" a class user that inherits from the BaseModel class """
from models.base_model import BaseModel


class User(BaseModel):
    """ Define the attributes of the user """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
