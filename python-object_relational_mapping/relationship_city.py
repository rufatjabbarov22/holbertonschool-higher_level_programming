#!/usr/bin/python3
"""
Module that contains the City class
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from relationship_state import Base

class City(Base):
    """ Class representation of cities table """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)

