"""
Name: lab06_part2.py
Author: Jeff Martin
Date: 10/12/2020
Lab section: 61
Email: jmartin8@umbc.edu
Description: This is a demonstration file for Lab 6
"""

# The number of strings for gaul_is_divided to divide into
NUM_STRINGS = 3

"""
A function to divide a string in three parts
(in the manner of Julius Caesar who wrote 2,000 years ago that "Gaul
[modern France] is divided into three parts")
:param a_string: The string to divide
:return: A list with three (relatively equal-sized) strings
"""
def gaul_is_divided(a_string):
    # The divided string
    divided_string = []

    # We need the string to be long enough to divide.
    if (len(a_string) < NUM_STRINGS):
        print("That string is not long enough.")
    else:
        substring_length = len(a_string) // NUM_STRINGS

        # Divide the string into NUM_STRINGS parts
        for i in range(NUM_STRINGS):
            starting_point = i * substring_length
            stopping_point = starting_point + substring_length

            # We want to make sure that the last division runs to the
            # end of the string.
            if stopping_point + substring_length > len(a_string):
                stopping_point = len(a_string)

            # This divides the string using the starting and stopping points
            # we calculated earlier.
            divided_string.append(a_string[starting_point:stopping_point])

    return divided_string


if __name__ == "__main__":
    string_to_divide = "Gaul is divided into three parts"
    divided_string = gaul_is_divided(string_to_divide)

    # Print the divided string
    for a_string in divided_string:
        print(a_string)