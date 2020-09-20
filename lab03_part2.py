"""
Name: lab03_part2.py
Author: Jeff Martin
Date: 9/19/2020
Lab section: 61
Email: jmartin8@umbc.edu
Description: This is a demonstration file for Lab 3
"""

# What if we have a list like this:
numbers = [1, 2, 3, 4, 5]

# and we want to change one of the numbers? We can do this:
numbers[0] = 20

# and now the first number is 20. But what if we want to change all of them?
numbers[0] = 0
numbers[1] = 1
numbers[2] = 2
numbers[3] = 3
numbers[4] = 4

# That's a pain. We can do better, like this:
counter = 0
while counter < len(numbers):
    numbers[counter] = 5 + counter

# Now our list contains 5, 6, 7, 8, 9
# Can we do it this way?
for number in numbers:
    number = 9

# We can't! We don't have an index, and changing "number" doesn't change anything in the "numbers" list anyway.
# But we can do THIS, which is called a "for i" loop. It's called "for i" because instead of "numbers" we often
# just use i for the counter variable.
for i in range(0, len(numbers)):
    numbers[i] = 5 + i

# This solves our problem and means that we don't have to make the "counter" variable separately.
# When the for loop is done, the "i" variable disappears.

# DO NOT USE A FOR I LOOP FOR LAB 3! You have not officially been "taught" it.
# I've introduced it here to prepare you for the idea.
