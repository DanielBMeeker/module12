"""
Program: abstract_class_assignment.py
Author: Daniel Meeker
Date: 7/11/2020

This program demonstrates implementing abstract classes in python
"""
from abc import ABC, abstractmethod


class Rider(ABC):
    """
    Abstract Rider Class
    """
    @abstractmethod
    def ride(self):
        raise NotImplementedError("Method not implemented")

    @abstractmethod
    def riders(self):
        raise NotImplementedError("Method not implemented")


class Bicycle(Rider):
    """
    Bicycle Class - a subclass of Rider
    """
    def ride(self):
        return "Pedal Powered, not enclosed"

    def riders(self):
        return "1 for sure, 2 if you're brave"


class Motorcycle(Rider):
    """
    Motorcycle Class - a subclass of Rider
    """
    def ride(self):
        return "Gas Engine Powered, not enclosed"

    def riders(self):
        return "1 or 2, possibly 3 if you've got a side car"


class Car(Rider):
    """
    Car Class = a subclass of Rider
    """
    def ride(self):
        return "Gas Engine powered, often enclosed"

    def riders(self):
        return "Usually will accommodate at least 4, sometimes more, sometimes less"


if __name__ == '__main__':
    b = Bicycle()
    m = Motorcycle()
    c = Car()
    print(b.ride())
    print(b.riders())
    print(m.ride())
    print(m.riders())
    print(c.ride())
    print(c.riders())
