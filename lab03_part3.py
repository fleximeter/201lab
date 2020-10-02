"""
Name: lab03_part3.py
Author: Jeff Martin
Date: 9/19/2020
Lab section: 61
Email: jmartin8@umbc.edu
Description: This is a demonstration file for Lab 3
"""

# We can do more with lists.
numbers = [1, 0, 3, 2, 5]

# If we want to add a number, we can do this:
numbers.append(6)

# If we want to remove a number, we remove it by its value:
numbers.remove(2)

# This DID NOT remove the third item from the list. Instead, it searched the list for 2, and removed it.
# To remove the third item from the list, we do this:
del numbers[2]

# What if we want to know if a list contains a number? We do this:
1 in numbers

# This is true if 1 is in numbers, and false otherwise. We can say:
if 1 in numbers:
    print("1 is in the list of numbers!")

