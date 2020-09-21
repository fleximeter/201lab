"""
Name: lab03_part1.py
Author: Jeff Martin
Date: 9/19/2020
Lab section: 61
Email: jmartin8@umbc.edu
Description: This is a demonstration file for Lab 3
"""

# Sometimes we want to group information together. For example,
# there are twelve months in a year. We could do this:
month_0 = "January"
month_1 = "February"
month_2 = "March"
month_3 = "April"
month_4 = "May"
month_5 = "June"
month_6 = "July"
month_7 = "August"
month_8 = "September"
month_9 = "October"
month_10 = "November"
month_11 = "December"

# But that's a pain. And what if we want to access the month by number?
# We can make a "list" to hold these months, like this:
months = ["January", "February", "March", "April", "May", "June", "July",
          "August", "September", "October", "November", "December"]

# Now, if I want to print May, I do this:
print(months[4])

# If I want to print January, I do this:
print(months[0])

# It's important to notice that the index of the item in the list starts at ZERO.
# This is very important to remember!!!!! So January is 0, not 1.

# What do we do here? Didn't I just forget what I said about indexing starting at 0
user_input = input("Enter the month number you want (1-12): ")

# Well, no. Suppose the user enters 1, for January. How do I display January? Like this:
print(months[user_input - 1])

# This is a common thing that you'll see in many programs.

# Now, what if I want to print each item in the list? Well, I can use something called a "loop":
counter = 0
while counter < 12:
    print(months[counter])
    counter += 1

# This is an infinite loop.
while True:
    print("infinite loop")

# There's a more elegant way of writing this, though:
counter = 0
while counter < len(months):
    print(months[counter])
    counter += 1

# The len() function gets us the number of items in a list. But there's an even slicker method:
for month in months:
    print(month)

# This is a special loop that's designed to iterate through a list. The for loop starts with the
# first month in "months" and prints it, then does the same with the second month, and so on.
# The variable "month" moves to the next item in the list each time, until we are finished.

