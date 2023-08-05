#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


env = getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """created class amenity"""
    __tablename__ = 'amenities'
    if env == "db":
        name = Column(String(128), nullable=False)
        """place_amenities = relationship("Place", secondary=place_amenity,
                                       backref='amenity')"""
    else:
        name = ""
