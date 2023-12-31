#!/usr/bin/python3
""" this module to unittest for user.py """
import unittest
from models.city import City
import datetime


class TestCity(unittest.TestCase):
    """ Test instances and methods from city class """
    city = City()

    def test_class_exists(self):
        """ Test if class exists """
        self.assertEqual(str(type(self.city)), "<class 'models.city.City'>")

    def test_user_inheritance(self):
        """ Test if city is a subclass of BaseModel """
        self.assertTrue(self.city, City)

    def testHasAttributes(self):
        """ Verify if attributes exist """
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))
        self.assertTrue(hasattr(self.city, 'id'))
        self.assertTrue(hasattr(self.city, 'created_at'))
        self.assertTrue(hasattr(self.city, 'updated_at'))

    def test_types(self):
        """ Test if the type of the attribute is the correct 1 """
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)
        self.assertIsInstance(self.city.id, str)
        self.assertIsInstance(self.city.created_at, datetime.datetime)
        self.assertIsInstance(self.city.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
