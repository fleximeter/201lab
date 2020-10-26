"""
Name: lab08_part1.py
Author: Jeff Martin
Date: 10/25/2020
Lab section: 61
Email: jmartin8@umbc.edu
Description: This is a demonstration file for Lab 8
"""

def read_data_file(file_name):
    """
    A function for reading a CSV data file
    :param file_name: The file to read
    :return: A 2D list containing the contents of the CSV
    """
    # Read the data from the file
    data_file = open(file_name)
    raw_data = data_file.read()
    data_file.close()

    # Turn the data into a 2D list
    csv_data = []
    lines = raw_data.split('\n')
    for line in lines:
        csv_data.append(line.split(','))

    return csv_data


def print_csv_data(csv_data):
    """
    A function for printing a CSV file to screen
    :param csv_data: A 2D list containing the data from the CSV file
    :return: nothing
    """
    for line in csv_data:
        for cell in line:
            print(cell, end=' ')
        print()


if __name__ == "__main__":
    # Replace this with any CSV file you want to read.
    csv_file_path = "C:\\Users\\Jeffrey Martin\\Desktop\\uszips.csv"
    print_csv_data(read_data_file(csv_file_path))