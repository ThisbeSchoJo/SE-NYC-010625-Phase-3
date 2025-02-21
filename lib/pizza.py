import ipdb

class Pizza:

    # Regular instance method (can be called on any instance):
    # Scope of set_name is within the class (so can't be called outside of the class)
    
    # dunder methods are methods that are happening under the hood
    # __init__ is called whenever we initially create a new instance
    def __init__(self, name, ingredients, price=25.99):
        # print(self) #prints out the actual reference to the instance
        # print(name)
        self.name = name
        self.ingredients = ingredients
        self.price = price

    def get_name(self):
        return self._name
    
    def set_name(self, value):
        if type(value) == str:
            self._name = value
        else:
            raise TypeError

    name = property(get_name, set_name)
    # Now whenever we reference name, it will trigger the set_name function to get called, and the value on the right hand side gets passed into set_name

    # Using a property decorator -- slapping something onto a function to achieve a new feature
    @property #this allows price to become a getter method
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if not (type(value) in [int, float]):
            raise TypeError
        elif value < 20:
            raise ValueError
        # by default set price to value if there are no errors
        self._price = value

# instances always have at least one parameter (self)
# first parameter passed in is set to the second parameter in __init__
pepperoni_pizza = Pizza("Pepperoni Pizza", "Cheese, pepperoni", 24.99)
supreme_pizza = Pizza("Supreme Pizza", "Cheese, sausage, pepperoni, onions", 26.99)

# If you wanted to change the name... you can do it through reassignment
# pepperoni_pizza.name = "Grandma Pizza"
# obviously same goes for ingredients
# You can use properties when you want to make sure it's valid/authenticate it
# Need a property bc you can still assign a bad property to the instance variable otherwise
# 2 ways to make a property:
# 1 - property()
# 2 - with property decorator


ipdb.set_trace()