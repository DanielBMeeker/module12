"""
Program: custom_exceptions.py
Author: Daniel Meeker
Date: 7/11/2020

This program defines a customer class with a constructor and 3 methods:
str, repr, and display. This program demonstrates the use of custom
exceptions. This file contains the custom exceptions used in the program.
"""


class InvalidCustomerIDException(Exception):
    """
    Invalid Customer ID Exception Class
    """
    pass


class InvalidNameException(Exception):
    """
    Invalid Name Exception Class
    """
    pass


class InvalidPhoneNumberFormat(Exception):
    """
    Invalid Phone Number Format Class
    """
    pass
