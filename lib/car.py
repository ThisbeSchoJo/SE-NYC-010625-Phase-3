import ipdb

# Deliverable #1
class Car:
    def __init__(self, make, model, year, horn_volume="1"):
        self.make = make
        self.model = model
        self.year = year
        self.horn_volume=horn_volume

    def get_year(self):
        return self.get_year
    
    def set_year(self, year):
        if (isinstance(year, int)):
            self._year = year
        else:
            raise TypeError("Year must be an integer")

# Notes:
# A Class is similar to a factory (or blueprint)
# When you call a class, you're calling __init__ behind the scenes
# You can use class to create different instances of that class
# if you don't store that instance in the variable, it won't be saved and you won't have access to it
# "is" is often used with instances bcause it compares where two things are in memory
# The value of self is the instance itself
# When you make an instance, the returned value is the object of the information about the instance
# The value of self is a reference to the instance itself
# self is the python standard for what we use to hold the value of the instance


# 1. Create a `Car` class that takes in values for the following parameters for the `__init__` method: 
# `make`, `model`, `year`. 
# The `__init__` method should also take an optional value for the `horn_volume` parameter 
# (set the default value for `horn_volume` to `1`). 
# Write the code to create the appropriate instance variables and assign the values from the input parameters to the appropriate instance variables.
#    - The `Car` class should have the following instance variables and values:
#      - An instance variable named `make` that has the value of the `make` parameter from the `__init__` method.
#      - An instance variable named `model` that has the value of the `model` parameter from the `__init__` method.
#      - An instance variable named `year` that has the value of the `year` parameter from the `__init__` method.
#      - An instance variable named `horn_volume` that has the value of the `horn_volume` parameter from the `__init__` method.

# 2. Create a property for the `year` instance variable. 
# For the setter method, the `year` must be an `int` that is between `1900` and `2024`. 
# If the value is not an `int`, raise a `TypeError` with the message `"Year must be an integer!"`. 
# If the value is not between `1900` and `2024`, raise a `ValueError` with the message `"Year must be between 1900 and 2024!"`