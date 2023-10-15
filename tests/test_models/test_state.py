#!/usr/bin/python3
""" This module unittest for amenity.py """
import unittest
from models.state import State
import datetime


class TestState(unittest.TestCase):
    """ Test instances and methods from State class """
    stat = State()

    def test_class_exists(self):
        """ Test if class is exist """
        self.assertEqual(str(type(self.stat)), "<class 'models.state.State'>")

    def test_user_inheritance(self):
        """ Test if State is a subclass of BaseModel """
        self.assertIsInstance(self.stat, State)

    def testHasAttributes(self):
        """ Verify if attributes exist """
        self.assertTrue(hasattr(self.stat, 'id'))
        self.assertTrue(hasattr(self.stat, 'name'))
        self.assertTrue(hasattr(self.stat, 'created_at'))
        self.assertTrue(hasattr(self.stat, 'updated_at'))

    def test_types(self):
        """ Test if the type of the attribute is the correct 1 """
        self.assertIsInstance(self.stat.id, str)
        self.assertIsInstance(self.stat.name, str)
        self.assertIsInstance(self.stat.created_at, datetime.datetime)
        self.assertIsInstance(self.stat.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
