#!/usr/bin/python3
""" The city class """
from models.base_model import BaseModel


class City(BaseModel):
    """ Defining the City attributes """
    state_id = ''  # it will be the State.id
    name = ''
