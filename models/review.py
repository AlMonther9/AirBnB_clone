#!/usr/bin/python3
""" HBNB project review Module """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Feedback class to store review data """
    place_id = ""
    user_id = ""
    text = ""
