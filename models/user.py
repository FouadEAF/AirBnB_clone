#!/usr/bin/python3
""" This module for User creation class """
from models.base_model import BaseModel


class User(BaseModel):
    """ Define attributes for user creation """
    id = ""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
