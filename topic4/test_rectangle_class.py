"""
Program: test_rectangle_class.py
Author: Shell provided by instructor with some changes by Daniel Meeker
Date: 7/11/2020

This program demonstrates unit testing with abstract classes
"""
import unittest
from topic4.rectangle import *


class RectangleClassTest(unittest.TestCase):

    def setUp(self):
        self.shape = Rectangle(12, 23.4)

    def tearDown(self):
        del self.shape

    def test_constructor(self):
        with self.assertRaises(InvalidSideError):
            r = Rectangle(5, -5)
        with self.assertRaises(InvalidSideError):
            r = Rectangle(-5, 5)

    def test_shape_area(self):
        self.assertAlmostEqual(280.8, self.shape.area())
        with self.assertRaises(NotImplementedError):
            r = Shape.area(self.shape)


if __name__ == '__main__':
    unittest.main()
