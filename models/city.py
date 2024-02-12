#!/usr/bin/python3
""" Module for Urban Area in HBNB project """
from models.base_model import BaseModel


class City(BaseModel):
    """ The City class comprises the state identifier and name. """
    state_id = ""
    name = ""
