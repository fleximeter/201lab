"""
Name: lab09_part1.py
Author: Jeff Martin
Date: 11/1/2020
Lab section: 61
Email: jmartin8@umbc.edu
Description: This is a demonstration file for Lab 9
"""

def break_my_pc():
    """
    This function simply runs again and again until it is forcibly stopped.
    :return: nothing
    """
    print("Break my PC")
    break_my_pc()

def more_sophisticated_break_my_pc(number):
    """
    This function simply runs again and again until it is forcibly stopped.
    It's a bit more sophisticated because it tells us how many times it runs.
    :param number: An index that we increase each time the function runs
    :return: nothing
    """
    print(f"Break my PC {number} times")
    more_sophisticated_break_my_pc(number + 1)

def dont_break_my_pc(number):
    """
    This function runs again and again, but stops when number is equal to 500.
    :param number: An index that we increase each time the function runs
    :return: nothing
    """
    # Base case
    if number >= 500:
        print(f"Break my PC {number} times")
    # Recursive case
    else:
        print(f"Break my PC {number} times")
        dont_break_my_pc(number + 1)

def fibonacci(index, prev_value_1, prev_value_2):
    """
    Prints numbers in the Fibonacci sequence
    :param index: The index in the Fibonacci sequence
    :param prev_value_1: The immediately previous value
    :param prev_value_2: The value before that
    :return: nothing
    """
    # Base case
    if index == 100:
        print(prev_value_1 + prev_value_2)

    # Recursive case
    else:
        print(prev_value_1 + prev_value_2)
        fibonacci(index + 1, prev_value_1 + prev_value_2, prev_value_1)


if __name__ == "__main__":
    dont_break_my_pc(0)
    print(1)
    print(1)
    fibonacci(3, 1, 1)