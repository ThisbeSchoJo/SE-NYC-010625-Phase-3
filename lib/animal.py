# import ipdb

class Animal:

    def __init__(self, name, age):
        self.name =name
        self.age = age

    def make_animal_sound(self):
        print("Animal sound!")


# Dog class inherits from the Animal class
# So all the methods and instance variables in Animal will be available to Dog as well
# Dogs will have the same init
class Dog(Animal):
    
    def __init__(self, name, age, bark_volume=1, obedience_level=1):
        # self.name = name
        # self.age = age
        # ^^ these two lines get replaced with super()
        super().__init__(name, age)
        # super references the animal class's init method
        self.bark_volume = bark_volume
        self.obedience_level = obedience_level

    # If you define the same method in Dog, it will overwrite what it inherits from Animal
    def make_animal_sound(self):
        print(f"Bark{'!' * self.bark_volume}")

class Cat(Animal):

    def make_animal_sound(self):
        print("Meow!")

# Whole notion of Inheritance is to copy everything from a template, and then change some things to make it more specific