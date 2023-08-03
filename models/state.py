#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = name = Column(String(128), nullable=False)
    """relationship with tha class City"""
    cities = relationship('City', backref='state',
                          cascade='all, delete-orphan')

    @property
    def cities(self, cls=None):
        """getter for City instances"""
        from models import storage
        cities_state = []
        instance = storage.all(cls)
        for k, element in instance.items():
            cities_state.append(element)
        return (cities_state)
