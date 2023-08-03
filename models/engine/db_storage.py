#!/usr/bin/python3
"""
this module define a class to manage Db storage
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import models

class DBStorage:
    """
    this class manages storage of hbnb models
    Private class attributes:
        __engine: set to None
        __session: set to None
    """
    

