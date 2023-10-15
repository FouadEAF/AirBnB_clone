#!/usr/bin/python3
""" This module defines review class """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review made by users about a place"""
    id = ""
    user_id = ""
    place_id = ""
    text = ""
