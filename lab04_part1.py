"""
Name: lab4_part1.py
Author: Jeff Martin
Date: 9/28/2020
Lab section: 61
Email: jmartin8@umbc.edu
Description: This is a demonstration file for Lab 4. The purpose of this
             program is to demonstrate coding standards.
             Notice the use of comments in this file. There are more comments
             here than you are likely to need in normal circumstances. But
             each comment affects a group of lines that perform one operation.
             Notice that I only used one comment at the bottom for the while
             loop and the ending print statement.
             Notice that no line of code has more than 80 characters in it.
"""

# We don't need this constant, but here it is anyway
VALUE_OF_PI = 3.14159

if __name__ == "__main__":
    # We will use this to demonstrate proper operator spacing
    operator_demonstration = 50

    # This will be used for summing a list of numbers
    user_input = ""
    summation = 0

    # This demonstrates proper spacing around operators
    operator_demonstration = 50 + 90
    print(operator_demonstration)
    operator_demonstration = 50 + 90 * 2
    print(operator_demonstration)

    # Notice that parentheses changed the order of operations
    operator_demonstration = (50 + 90) * 2
    print(operator_demonstration)

    # This demonstrates not using more than 80 characters per line, and proper
    # indentation (4 spaces)
    print("If you manually run this file using the command python3 "
        + "lab4_part1.py, this section will execute. Otherwise, if "
        + "another file calls this one, this section will not execute.")

    # Here we ask a user for numbers to add. The user should enter "done" when
    # they are finished.
    while user_input != "done":
        print("Enter a number to sum, or enter \"done\" if you are "
            + "finished: ", end = "")
        user_input = input()
        if user_input != "done":
            summation += float(user_input)

    print("The sum is", summation)