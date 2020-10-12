"""
Name: lab06_part1.py
Author: Jeff Martin
Date: 10/12/2020
Lab section: 61
Email: jmartin8@umbc.edu
Description: This is a demonstration file for Lab 6
"""

def demonstrate_slicing(some_string):
    # This prints the entire string, obviously
    print(some_string)

    # This prints the third character in the string - 's'
    print(some_string[2])

    # This prints characters 12-20 in the string - "doing the"
    # Note - the slice goes to end - 1, like range loops!
    print(some_string[12:21])

    # This prints characters 0-10 in the string - "Insanity is"
    print(some_string[:11])

    # This prints characters 12-end in the string - "doing ..."
    print(some_string[12:])

    # This prints the entire string, funnily enough
    print(some_string[:])


def weird_slicing(some_string):
    # this...reverses...the string
    print(some_string[::-1])


if __name__ == "__main__":
    a_string = "Insanity is doing the same thing over and over again and expecting different results."

    demonstrate_slicing(a_string)
    weird_slicing(a_string)
