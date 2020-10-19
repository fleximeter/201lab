"""
Name: lab07_part1.py
Author: Jeff Martin
Date: 10/19/2020
Lab section: 61
Email: jmartin8@umbc.edu
Description: This is a demonstration file for Lab 7
"""

# Notice that some_value here is different from some_value under
# if __name__ == "__main__". This is because of variable scope.
def sample_function(some_value):
    return some_value + 5

# Although some_list is different from some_list under
# if __name__ == "__main__", this function WILL modify the
# original list.
# That's because lists are passed by REFERENCE, not by VALUE.
# This is often called a "shallow copy" as opposed to a "deep copy".
def sample_function_1(some_list):
    some_list.append(5)

if __name__ == "__main__":
    some_value = 53
    some_list = [1, 2, 3, 4]
    some_value = sample_function(some_value)
    sample_function_1(some_list)