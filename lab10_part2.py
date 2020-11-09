"""
Name: lab10_part2.py
Author: Jeff Martin
Date: 11/8/2020
Lab section: 61
Email: jmartin8@umbc.edu
Description: This is a demonstration file for Lab 10
"""

# A custom data type is defined using a "class". Here we will
# create a custom data type for a person.
class Person:
    # Constants that are true for each Person
    HEART_DISEASE_AGE = 50
    BMI_OBESE = 30

    def __init__(self):
        """
        This is a special function called a "constructor". It runs each time
        we create a new Person variable. For this class, all it does is to
        create variables that are unique to each Person, such as their name,
        age, height (in centimeters), and weight (in kilograms).
        """
        self.name = ""
        self.age = 0
        self.height = 0
        self.weight = 0

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
    # This is how we create variables of our Person type.
    gandalf = Person()

    # Now we need to update Gandalf's information.
    gandalf.name = "Gandalf the Grey"
    gandalf.age = 1000
    gandalf.height = 190
    gandalf.weight = 90

    # We will now check to see if Gandalf is at risk of heart disease.
    # Notice that we call the risk_of_heart_disease function from gandalf,
    # just as we would call append() from a list.
    if gandalf.risk_of_heart_disease() == True:
        print(gandalf.name, "is at risk of heart disease")
    else:
        print(gandalf.name, "is not at risk of heart disease")