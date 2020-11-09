"""
Name: lab10_part3.py
Author: Jeff Martin
Date: 11/8/2020
Lab section: 61
Email: jmartin8@umbc.edu
Description: This is a demonstration file for Lab 10
"""

class Person:
    # Constants that are true for each Person
    HEART_DISEASE_AGE = 50
    BMI_OBESE = 30

    def __init__(self, name, age, height, weight):
        """
        This is a special function called a "constructor". It runs each time
        we create a new Person variable.
        :param name: The name of the Person
        :param age: The age of the Person
        :param height: The Person's height in centimeters
        :param weight: The Person's weight in kilograms
        """
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def calculate_body_mass_index(self):
        """
        Calculates the BMI for the current Person
        :return: The BMI as a float
        """
        return self.weight / (self.height / 100) ** 2

    def risk_of_heart_disease(self):
        """
        Determines if the Person is at risk of heart disease. This is computed
        by retrieving the Person's age and BMI.
        :return: True if the person is at risk of heart disease; False otherwise
        """
        if self.age > Person.HEART_DISEASE_AGE and self.calculate_body_mass_index() > Person.BMI_OBESE:
            return True
        else:
            return False

if __name__ == "__main__":
    # We will create a Person named Gandalf. We will pass his information to the constructor,
    # rather than setting each variable separately.
    gandalf = Person("Gandalf the Grey", 1000, 190, 90)

    # We can change Gandalf's weight if we want. Let's give him 5 more kilograms.
    gandalf.weight += 5

    # We will now check to see if Gandalf is at risk of heart disease.
    # Notice that we call the risk_of_heart_disease function from gandalf,
    # just as we would call append() from a list.
    if gandalf.risk_of_heart_disease() == True:
        print(gandalf.name, "is at risk of heart disease")
    else:
        print(gandalf.name, "is not at risk of heart disease")