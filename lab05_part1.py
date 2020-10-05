"""
Name: lab05_part1.py
Author: Jeff Martin
Date: 10/5/2020
Lab section: 61
Email: jmartin8@umbc.edu
Description: This is a demonstration file for Lab 5
"""

if __name__ == "__main__":
    # We'll start by messing around with a string.
    a_string = "This is a string to mess around with."
    print(a_string)
    print(a_string[5], a_string[0], a_string[20])

    # Here we're printing every non-whitespace character
    # in the string, separated by a space.
    for character in a_string:
        if character != ' ':
            print(character, end=' ')
    # This print statement is necessary because otherwise we
    # would not move to the next line.
    print()

    # Here we're going to split the string into a list. We split
    # by space characters.
    a_list = a_string.split()
    print(a_list)

    # Now we're going to join the strings together again. We
    # use a space to join them in this case.
    a_string2 = " ".join(a_list)
    print(a_string2)

    a_list2 = []

    # This creates a square 2D list of the numbers
    # from 1 to 100. See if you can figure out why this works.
    for i in range(10):
        temp_list = []
        for j in range(10):
            temp_list.append(i * 10 + j + 1)
        a_list2.append(temp_list)

    # Two ways of printing out a 2D list. The first is a bit more crude.
    for i in range(10):
        print(a_list2[i])

    for i in range(10):
        for j in range(10):
            print(a_list2[i][j], end=' ')
        print()

    # We can single out an individual item in the list to print
    print(a_list2[2][5])

    # If we want, we can print out each item on the diagonal
    for i in range(10):
        print(a_list2[i][i])

    # In this case, we'll print each row. But if we get to a number
    # that is divisible by 3, we'll skip the next 2 characters in
    # that row.
    counter = 0
    while counter < len(a_list2):
        counter1 = 0

        while counter1 < len(a_list2[counter]):
            print(a_list2[counter][counter1], end=' ')
            if a_list2[counter][counter1] % 3 == 0:
                counter1 += 2
            counter1 += 1
        print()

        counter += 1
