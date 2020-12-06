# @TODO: Write a function that returns the arithmetic average for a list of numbers


# Test your function with the following:
# print(average([1, 5, 9]))
# print(average(range(11)))


def average(list)
    avg = sum (list) / len(list)
    return avg

my_list=[2,7,6,8,1,9]
average = avg(my_list)
print("Average of my list", average)


import os
import csv

# Path to collect data from the Resources folder

# Define the function and have it accept the 'wrestlerData' as its sole parameter

# Find the total number of matches wrestled

# Find the percentage of matches won

# Find the percentage of matches lost

# Find the percentage of matches drawn

# Print out the wrestler's name and their percentage stats

# Read in the CSV file
with open(wrestling_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    # Prompt the user for what wrestler they would like to search for
    name_to_check = input("What wrestler do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if(name_to_check == row[0]):
            print_percentages(row)
