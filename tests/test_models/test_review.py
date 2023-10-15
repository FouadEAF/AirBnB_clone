#!/usr/bin/python3
""" This module unittest for review.py """
import unittest
from models.review import Review
import datetime


class TestReview(unittest.TestCase):
    """ Tests instances and methods from Review class """
    rvw = Review()

    def test_class_exists(self):
        """ Tests if class exist """
        self.assertEqual(str(type(self.rvw)), "<class 'models.review.Review'>")

    def test_user_inheritance(self):
        """ Test if Review is a subclass of BaseModel """
        self.assertIsInstance(self.rvw, Review)

    def testHasAttributes(self):
        """ Verify if attributes is exist """
        self.assertTrue(hasattr(self.rvw, 'place_id'))
        self.assertTrue(hasattr(self.rvw, 'user_id'))
        self.assertTrue(hasattr(self.rvw, 'text'))
        self.assertTrue(hasattr(self.rvw, 'id'))
        self.assertTrue(hasattr(self.rvw, 'created_at'))
        self.assertTrue(hasattr(self.rvw, 'updated_at'))

    def test_types(self):
        """ Test if the type of the attribute is the correct 1 """
        self.assertIsInstance(self.rvw.place_id, str)
        self.assertIsInstance(self.rvw.user_id, str)
        self.assertIsInstance(self.rvw.text, str)
        self.assertIsInstance(self.rvw.id, str)
        self.assertIsInstance(self.rvw.created_at, datetime.datetime)
        self.assertIsInstance(self.rvw.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
