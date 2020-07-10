"""
Program: iowa_demographics
Author: Daniel Meeker
Date: 7/10/2020

This file defines a class that is used to save all the data
from a CSV file.
"""


class CountyDemographics:
    """
    County Demographics Class
    """
    def __init__(self, rank, county, per_capita_income,
                 median_household_income, median_family_income,
                 population, number_of_households):
        """

        :param rank: required
        :param county: required
        :param per_capita_income: required
        :param median_household_income: required
        :param median_family_income: required
        :param population: required
        :param number_of_households: required
        """
        self.rank = rank
        self.county = county
        self.per_capita_income = per_capita_income
        self.median_household_income = median_household_income
        self.median_family_income = median_family_income
        self.population = population
        self.number_of_households = number_of_households

    def __repr__(self):
        """
        overrides build-in repr function
        :return: a string that could be used to recreate the object
        """
        return ("{self.__class__.__name__}({self.rank}, "
                "'{self.county}', '{self.per_capita_income}', "
                "'{self.median_household_income}', '{self.median_family_income}', "
                "'{self.population}', '{self.number_of_households}')\n").format(self=self)

    def __str__(self):
        """
        overrides built-in str function
        :return: a string with all the data neatly organized
        """
        return ("County Rank: {self.rank}"
                "\nCounty: '{self.county}'"
                "\nPer-Capita Income: '{self.per_capita_income}'"
                "\nMedian Household Income: '{self.median_household_income}'"
                "\nMedian Family Income: '{self.median_family_income}'"
                "\nPopulation: '{self.population}'"
                "\nNumber of Households: '{self.number_of_households}'".format(self=self))


if __name__ == '__main__':
    pass
