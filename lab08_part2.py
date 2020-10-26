"""
Name: lab08_part1.py
Author: Jeff Martin
Date: 10/25/2020
Lab section: 61
Email: jmartin8@umbc.edu
Description: This is a demonstration file for Lab 8
"""

if __name__ == "__main__":
    a_dictionary = {"apple": "Arkansas Black", "peach": "Clingstone"}

    # Add items to the dictionary. Format: a_dictionary["key"] = "value"
    a_dictionary["grape"] = "Muscat"
    a_dictionary["grass"] = "Chinese Silver"
    a_dictionary["tree"] = "Kentucky Coffee"

    # Access the whole dictionary or just one value
    print(a_dictionary)
    print(a_dictionary["tree"])

    # Change the value of an item
    a_dictionary["tree"] = "Joshua"
    print(a_dictionary)

    # Remove an item
    del a_dictionary["peach"]
    print(a_dictionary)

    # Get the keys of a dictionary as a list
    some_list = list(a_dictionary.keys())
    print(some_list)

    # Get the values of a dictionary as a list
    some_list = list(a_dictionary.values())
    print(some_list)

    # Declare a 2D dictionary
    a_2d_dictionary = {
        "Fruits": {
            "apple": "Arkansas Black",
            "grape": "Muscat"
        },

        "Other": {
            "grass": "Chinese Silver",
            "tree": "Joshua"
        }
    }

    # Access the dictionary
    print(a_2d_dictionary)
    print(a_2d_dictionary["Fruits"])
    print(a_2d_dictionary["Fruits"]["grape"])

    # Delete one value
    del a_2d_dictionary["Fruits"]["apple"]
    print(a_2d_dictionary)

    # Delete a subdictionary
    del a_2d_dictionary["Other"]
    print(a_2d_dictionary)

