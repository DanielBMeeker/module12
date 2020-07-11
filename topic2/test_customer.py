"""
Program: test_customer.py
Author: Daniel Meeker
Date: 7/11/2020

This program defines a customer class with a constructor and 3 methods:
str, repr, and display. This program demonstrates the use of custom
exceptions. This file tests the class and exceptions.
"""
import unittest
from topic2 import customer as t
from topic2.custom_exceptions import *


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.customer = t.Customer(1234, "Meeker", "Daniel", "319-560-2402")

    def tearDown(self):
        del self.customer

    def test_inital_all_attributes(self):  # test constructor with all valid input
        customer = t.Customer(1234, 'Duck', 'Daisy', '111-111-1111')
        assert customer.customer_id == 1234
        assert customer.last_name == 'Duck'
        assert customer.first_name == 'Daisy'
        assert customer.phone_number == '111-111-1111'

    def test_object_not_created_error_last_name(self):
        with self.assertRaises(InvalidNameException):
            c = t.Customer(1234, '515', 'Daisy', '111-111-1111')

    def test_object_not_created_error_fist_name(self):
        with self.assertRaises(InvalidNameException):
            c = t.Customer(1234, 'Duck', '515', '111-111-1111')

    def test_object_not_created_error_customer_id(self):
        with self.assertRaises(InvalidCustomerIDException):
            p = t.Customer(12345, 'Duck', 'Daisy', '515-555-5555')

    def test_object_not_created_error_phone_number(self):
        with self.assertRaises(InvalidPhoneNumberFormat):
            p = t.Customer(1234, 'Duck', 'Daisy', '(515)555-5555')
            d = t.Customer(1234, 'Duck', 'Daisy', '5155555555')
            q = t.Customer(1234, 'Duck', 'Daisy', '1(515)555-5555')
            b = t.Customer(1234, 'Duck', 'Daisy', '(ABC)555-5555')

    def test_customer_str(self):
        self.assertEqual(str(self.customer), 'Customer #1234: Meeker, Daniel, 319-560-2402')


if __name__ == '__main__':
    unittest.main()
