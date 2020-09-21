"""
Name: lab03_part4.py
Author: Jeff Martin
Date: 9/21/2020
Lab section: 61
Email: jmartin8@umbc.edu
Description: This is a demonstration file for Lab 3
"""

# We're going to use loops to demonstrate how integer division
# and modulus operations work.

# First we'll use a while loop to demonstrate the integer division operator
print("We're going to demonstrate integer division by 4.")
counter = -20
while counter <= 20:
    print(counter, "//", 4, "=", counter // 4)
    counter += 1

# Now we're going to use a "for i" or "range" loop to demonstrate the mod operator
# NOTICE that range WILL STOP at 20. It WILL NOT go to 21. This is important to know.
print("\n\nWe're going to demonstrate mod 4.")
for i in range(-20, 21):
    print(str(i) + " % 4 = " + str(i % 4))

# Remember to always include a space after the comma operator, and put
# spaces before and after the + operator.

