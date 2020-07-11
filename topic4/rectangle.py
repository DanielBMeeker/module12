"""
Program: rectangle.py
Author: Shell provided by instructor with a small addition by
        Daniel Meeker to the rectangle __init__ so that there
        is some validation to raise the invalid shape error
Date: 7/11/2020

This file is used to demonstrate abstract classes and unit testing
with abstract classes.
"""
from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        raise NotImplementedError("Abstract method not implemented")


class InvalidSideError(Exception):
    pass


@Shape.register
class Rectangle:
    def __init__(self, h, b):
        if h <= 0 or b <= 0:
            raise InvalidSideError
        self.height = h
        self.base = b

    def area(self):
        return self.height*self.base


if __name__ == '__main__':
    pass
