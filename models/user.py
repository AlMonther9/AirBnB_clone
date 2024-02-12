#!/usr/bin/python3
"""I have made this module to define user class"""
from models.base_model import BaseModel


class User(BaseModel):
    """This class delineates a user through a multitude of ATTRs"""
    email = ''
    password = ''
    first_name = ''
    last_name = ''
