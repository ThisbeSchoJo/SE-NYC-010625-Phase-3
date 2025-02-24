# import ipdb

class Car:
    # class variables are meant to contain information about all the instances (rather than just a single instance) - usually all of them but really just two or more
    # for example, what if you wanted to keep track of the number of cars or the cars themselves
    # should be within the class but not inside the scope of the instance methods
    # Deliverable #3 Solution Code:
    all = [] #making a list so we can keep track of all the cars made
    
    def __init__(self, make, model, year, horn_volume=1):
        self.make = make
        self.model = model
        self.year = year
        self.horn_volume = horn_volume

        if len(Car.all) == 0:
            self.id = 1
        else:
            last_car = Car.all[-1]
            last_car_id = last_car.id
            self.id = last_car_id +1

        # will add each car insance to the all list
        Car.all.append(self)

    @property
    def make(self):
        return self._make
    
    @make.setter
    def make(self, value):
        if not (type(value) == str):
            raise TypeError("Make must be a string!")
        elif len(value) < 3:
            raise ValueError("Make must be at least 3 characters long!")
        else:
            self._make = value

    @property
    def year(self):
        return self._year
    
    @year.setter
    def year(self, value):
        if not (type(value) == int):
            raise TypeError("Year must be an integer!")
        elif not (1900 <= value <= 2024):
            raise ValueError("Year must be between 1900 and 2024!")
        else:
            self._year = value

    @property
    def horn_volume(self):
        return self._horn_volume
    
    @horn_volume.setter
    def horn_volume(self, value):
        if not (type(value) == int):
            raise TypeError("Horn Volume must be an integer!")
        elif not (1 <= value <= 10):
            raise ValueError("Horn Volume must be between 1 and 10!")
        else:
            self._horn_volume = value

    def honk_horn(self):
        print(f"BEEP BEEP{'!' * self.horn_volume}")

    # Solution code for Deliverable #2
    @property
    def model(self):
        # use _model because it will trigger the getter method if you just do self.model (which would trigger self.model again and then create a loop*)
        return self._model
    
    # the getter and setter are related... once we have property for getter, that's what is referenced with the setter (in this example "model").... i think
    @model.setter
    def model(self, value):
        # if something "cannot be changed after it is initialized" it means you need to use hasattr....
        # we check if the attribute "model" exists and raise an exception if it does
        # if the type of value is not a string, we'll raise an exception
        # if both things are false, we will do what we want to do
        if hasattr(self, 'model') or not (type(value) == str):
            raise Exception
        # if the attribute "model" does not exist and is a string, set it to value*
        self._model = value

    # Deliverable #4
    # make a class method with a decorator:
    @classmethod
    # change "self" to "cls" because it's referncing the class now, instead of the instance
    def average_year(cls):
        year_list = [car.year for car in cls.all]
        return sum(year_list)/len(year_list)
        
    @classmethod
    def cars_with_make(cls, make):
        return [car for car in cls.all if car.make == make]
    
    def __repr__(self):
        return f"<Car # {self.id} - Make: {self.make}, Model: {self.model}, Year: {self.year}, Horn Volume: {self.horn_volume}>"

# Difference between regular function and instance method (or really just a method in general) is:
# You can only call an instance method within a class
# A method belongs to something -- linked to something.
# functions can be directly called


# Can't call instance methods on a class -- can only call on an instance
# Car.honk_horn() 
# >> TypeError

# getter just gets the variable

# ipdb.set_trace()

ferrari_enzo = Car("Ferrari", "Enzo", 2023, 2)
