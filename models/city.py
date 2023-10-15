#!/usr/bin/python3
""" This module define a city """
from models.base_model import BaseModel


class City(BaseModel):
    """ Define city to look for """
    id = ""
    state_id = ""
    name = ""
