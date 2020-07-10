"""
Program: csv_to_class.py
Author: Daniel Meeker
Date: 7/10/2020

This program imports a CSV file and uses the information
for data analysis functions.
"""
import csv
from topic1.iowa_demographics import CountyDemographics

with open('Iowa 2010 Census Data Population Income.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    # initialize dictionary
    county = {}
    for row in csv_reader:
        # skip first row (data headers)
        if line_count == 0:
            line_count += 1
            continue
        county[str(row[1])] = CountyDemographics(rank=row[0], county=row[1], per_capita_income=row[2],
                                                 median_household_income=row[3], median_family_income=row[4],
                                                 population=row[5], number_of_households=row[6])
    # sanitize the data by removing dictionary entries for the United States and the state of Iowa
    county.pop('United States')
    county.pop('Iowa State')

    def people_per_household_county(key):
        """
        Function to find the number of people per house in a specific county
        :param key: required
        :return: a number
        """
        return (int(county[key].population.replace(',', ''))
                / int(county[key].number_of_households.replace(',', '')))

    def people_per_household_state():
        """
        Function to find the number of people per house in the state
        :return: a number
        """
        return sum_of_population()/sum_of_households()

    def sum_of_population():
        """
        Function to find the total population of the state
        :return: a number
        """
        pop_sum = 0
        for key in county:
            pop_sum += int(county[key].population.replace(',', ''))
        return pop_sum

    def sum_of_households():
        """
        Function to find the total number of households - used in
        people_per_household_state function
        :return: a number
        """
        house_sum = 0
        for key in county:
            house_sum += int(county[key].number_of_households.replace(',', ''))
        return house_sum


if __name__ == '__main__':
    print(county)
    print(sum_of_population())
    print(people_per_household_county('Dallas'))
    print(people_per_household_state())
    print(str(county['Dallas']))
