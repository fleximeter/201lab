"""
Name: lab07_part2.py
Author: Jeff Martin
Date: 10/19/2020
Lab section: 61
Email: jmartin8@umbc.edu
Description: This is a demonstration file for Lab 7
"""

if __name__ == "__main__":
    # A 10x10 matrix of numbers from 0-99
    a_list = [[ 0,  1,  2,  3,  4,  5,  6,  7,  8,  9],
              [10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
              [20, 21, 22, 23, 24, 25, 26, 27, 28, 29],
              [30, 31, 32, 33, 34, 35, 36, 37, 38, 39],
              [40, 41, 42, 43, 44, 45, 46, 47, 48, 49],
              [50, 51, 52, 53, 54, 55, 56, 57, 58, 59],
              [60, 61, 62, 63, 64, 65, 66, 67, 68, 69],
              [70, 71, 72, 73, 74, 75, 76, 77, 78, 79],
              [80, 81, 82, 83, 84, 85, 86, 87, 88, 89],
              [90, 91, 92, 93, 94, 95, 96, 97, 98, 99]]

    # The row and column we want to access
    row = 0
    column = 0

    # Print the first position
    print(a_list[row][column])

    # What if we want to move down?
    row += 1
    print(a_list[row][column])

    # What if we want to move right 5 columns?
    column += 5
    print(a_list[row][column])

    # What if we want to make sure we're moving to a real index?
    if column + 5 < len(a_list[row]):
        column += 5
        print(a_list[row][column])

    # If we're moving the other way, we want to change what we're checking for:
    if column - 20 >= 0:
        column -= 20
        print(a_list[row][column])

