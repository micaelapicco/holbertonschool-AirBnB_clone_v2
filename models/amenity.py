#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from os import getenv


env = getenv("HBNB_TYPE_STORAGE")
class Amenity(BaseModel):
    """created class amenity"""
    if env == "db":
        pass
    else:
        name = ""
