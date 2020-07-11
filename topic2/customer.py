"""
Program: customer.py
Author: Daniel Meeker
Date: 7/11/2020

This program defines a customer class with a constructor and 3 methods:
str, repr, and display. This program demonstrates the use of custom
exceptions.
"""
from topic2.custom_exceptions import *


class Customer:
    """
    Customer Class
    """

    def __init__(self, customer_id, last_name, first_name, phone_number):
        """
        Constructor for customer class - throws an error if customer_id not an int
        :param customer_id: required
        :param last_name: required
        :param first_name: required
        :param phone_number: required
        """
        if isinstance(customer_id, int) and 1000 <= customer_id <= 9999:
            self.customer_id = customer_id
        else:
            raise InvalidCustomerIDException("Customer ID not an int \nCustomer not created")
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(last_name) and name_characters.issuperset(first_name)):
            raise InvalidNameException("Name must be alphabetical characters, "
                                       "apostrophe's and hyphens are also allowed\nCustomer not created")
        phone_set = set("0123456789-")
        if not phone_set.issuperset(phone_number):
            raise InvalidPhoneNumberFormat("Phone number must be in the format:"
                                           " ###-###-####\nCustomer not created")
        else:
            try:
                phone_number_array = str(phone_number).split('-')
                area_code = phone_number_array[0]
                prefix = phone_number_array[1]
                line_number = phone_number_array[2]
                if len(area_code) != 3 or len(prefix) != 3 or len(line_number) != 4:
                    raise InvalidPhoneNumberFormat("Phone number must be in the"
                                                   " format: ###-###-####\nCustomer not created")
            except IndexError:
                raise InvalidPhoneNumberFormat("Phone number must be in the "
                                               "format: ###-###-####\nCustomer not created")
        self.last_name = last_name
        self.first_name = first_name
        self.phone_number = phone_number

    def __str__(self):
        """
        overrides built-in function
        :return: a basic string to identify the object
        """
        return ("Customer #{self.customer_id}: {self.last_name}, {self.first_name}, "
                "{self.phone_number}".format(self=self))

    def __repr__(self):
        """
        overrides built-in function
        :return: a string that mimics the constructor.
        """
        return ("{self.__class__.__name__}({self.customer_id}, '{self.last_name}', "
                "'{self.first_name}', '{self.phone_number}')".format(self=self))

    def display(self):
        """
        gathers all the info from the object to create a prettyfied string
        :return: a string
        """
        return ("Customer ID: " + str(self.customer_id) + "\n" + str(self.first_name) + " "
                + str(self.last_name) + "\n" + str(self.phone_number))


# Driver
if __name__ == '__main__':
    try:
        print("Customer 1:")  # invalid customer id
        customer1 = Customer(12345, 'Meeker', 'Daniel', '515-555-5555')
        print(customer1.display())
        print(customer1)
        print(repr(customer1))
        del customer1
    except InvalidCustomerIDException as e:
        print(e)
    try:
        print("Customer 2:")  # invalid last name
        customer2 = Customer(1234, '010110', 'Daniel', '515-555-5555')
        print(customer2.display())
        print(customer2)
        print(repr(customer2))
        del customer2
    except InvalidNameException as e:
        print(e)
    try:
        print("Customer 3:")  # invalid first name
        customer3 = Customer(1234, 'Meeker', '123', '515-555-5555')
        print(customer3.display())
        print(customer3)
        print(repr(customer3))
        del customer3
    except InvalidNameException as e:
        print(e)
    try:
        print("Customer 4:")  # invalid phone number format
        customer4 = Customer(1234, 'Meeker', 'Daniel', 'ABC-555-5555')
        print(customer4.display())
        print(customer4)
        print(repr(customer4))
        del customer4
    except InvalidPhoneNumberFormat as e:
        print(e)
    try:
        print("Customer 5:")  # invalid phone number format
        customer5 = Customer(1234, 'Meeker', 'Daniel', '1-515-555-5555')
        print(customer5.display())
        print(customer5)
        print(repr(customer5))
        del customer5
    except InvalidPhoneNumberFormat as e:
        print(e)
    try:
        print("Customer 6:")  # invalid phone number format
        customer6 = Customer(1234, 'Meeker', 'Daniel', '(515)555-5555')
        print(customer6.display())
        print(customer6)
        print(repr(customer6))
        del customer6
    except InvalidPhoneNumberFormat as e:
        print(e)
    try:
        print("Customer 7:")  # working customer object
        customer7 = Customer(1234, 'Meeker', 'Daniel', '515-555-5555')
        print(customer7.display())
        print(str(customer7))
        print(repr(customer7))
        del customer7
    except InvalidPhoneNumberFormat as e:
        print(e)


