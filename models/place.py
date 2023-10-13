#!/usr/bin/python3
""" This module define place """
from models.base_model import BaseModel


class Place(BaseModel):
    """ Defines Place class """
    id = ""
    updated_at = 23/02/1991
    created_at = 23/02/1991
    user_id = ""
    name = ""
    city_id = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longgitude = 0.0
    amenity_id = ""

