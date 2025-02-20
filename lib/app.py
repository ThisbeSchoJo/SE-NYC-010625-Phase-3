import ipdb


# A list of numbers
numbers_list = [7, 14]

# A list with just one item is still a list, 
# but a tuple with just one item isn't a tuple 
# (unless you put a comma after the number)

# A tuple that has 1 number
numbers_tuple = (8,)

# A tuple that has a string and a boolean
items = ("pizza", True)

# A list of duplicate numbers
duplicate_numbers_list = [2, 2, 3, 3, 4, 4]

# A set that removes the duplicate items from the list
numbers_set = set(duplicate_numbers_list)

numbers_list_without_duplicates = list(numbers_set)

# A string
phrase = "Hello flatiron"

# A string with duplicate characters
food = "pizza"

# A set that removes the duplicate characters from the "pizza" string
set_of_chars = set(food)

# If you wanted to convert a set back to a string... you'd want to do it manually*
# Taking the characters from the set and creating a new string that contains these characters with the duplicates having been removed
new_string = ""
for char in set_of_chars:
    new_string += char

# interpolation
print(f"My favorite phrase is: {phrase}")

# Deliverable #1
# should return a single sequence of the elements of `seq1` followed by the elements of `seq2`
def combine_sequences(seq1, seq2):
    return (seq1 + seq2)

# Deliverable #2
# should return a single sequence of `seq` repeated `n` times
def sequence_n_times(seq, n):
    return (seq * n)

# Deliverable #3
# should return the average of the numbers in `seq`, the input sequence
def average(seq):
    return ((sum(seq)) / (len(seq)))

# We also have max and min
# max(numbers_list)
# >> 14
# min(numbers_list)
# >>7

# Deliverable #4
# should return a list with an element append to it `n` times. 
# The list is contained within the `input_list` parameter.
def append_n_times(input_list, element, n):
    for char in range(n):
        input_list.append(element)
    return input_list
    # return input_list + [element] * n
    # return combine_sequences(input_list, sequence_n_times(element,n))

foods = [
    {
        "name": "Flatburger",
        "price": 9.50
    },
    {
        "name": "French Fries",
        "price": 1.25
    },
    {
        "name": "Burrito",
        "price": 7.25
    }
]


# LIST COMPREHENSIONS
# List comprehensions is basically like map combined with filter
# List compherensions returns a list, and we can shape the list however we want and filter out what we don't want
# start with "[]"
# [food for food in foods] 
# >>Will give you the exact same list as foods
# [food['name'] for food in foods]
# >> will return the foods list but just the names
# [food['price'] for food in foods]
# >> returns only the prices from the food list
# sum([food['price'] for food in foods])
# >> gives you sum of the prices of all the foods
# [food['price'] for food in foods if food['price'] > 3]
# returns price for the foods only if it's greater than 3
# can assign it to a value so we can do other things... 
# filtered_prices_list = [food['price'] for food in foods if food['price'] > 3]

# Item on left of list comprehension is the return value, 
# the second item is the iterator, 
# next item is the list, 
# then there is an optional condition (filters out some of them)
# The list comprehension is expecting something with key and value pairs (a dictionary)

# side note... we do sort of have a map and filter method in python... 
# but we don't have time to go over that rn (you supply a condition and an iterable**)

# Deliverable #5
# List Comprehension that constructs a list containing the names of the foods from the `foods` variable. 
# Store the result of this List Comprehension into a variable called `food_names`
food_names = [food['name'] for food in foods]

# Deliverable #6
# List Comprehension that constructs a list of the prices of the foods from the `foods` variable. 
# Store the result of this List Comprehension into a variable called `food_prices`. 
# Then, get the average price of the prices in the list stored in the `food_prices` variable 
# and store that result in a variable called `average_price`.
food_prices = [food['price'] for food in foods]
average_price = (average([food['price'] for food in foods]))
# average_price = average([food_prices])


animals = [
    {
        "name": "Fido",
        "animal_type": "Dog"
    },
    {
        "name": "Kitty",
        "animal_type": "Cat"
    },
    {
        "name": "Fluffy",
        "animal_type": "Guinea Pig"
    }
]

# Deliverable #7
# List Comprehension that constructs a list such that each item in the list with be in the following format: 
# `{name} is a {animal_type}`, where `{name}` references the name of the animal, 
# and `{animal_type}` references the animal_type of the animal. 
# Store the result of this List Comprehension into a variable called `animal_descriptions`.
animal_descriptions = [f"{animal['name']} is a {animal['animal_type']}" for animal in animals]



# Generator Expressions
# import sys
# sys.getsizeof lets you check the amount of memory being used for a particular object
# sys.getsizeof([1,2,3])
# >>>80
# Mainly just to make sure something doesn't take up too much memory
# Not really other useful things for this...


# ipdb.set_trace()
# allows you to put a breakpoint at that line of code
# pytest won't work if you leave in ipdb.set_trace tho


# Python spread operator: "*" instead of "..." FOR A LIST
# If you're working with a dictionary, it's something else
# [1, *numbers_list, 21]

# Use "**" to use spread operator with a dictionary
# {*foods[0]} would return {'price', 'name'} which is a set 
# a set is pretty much a list but the items aren't ordered and duplicates are removed
# {**foods[0]} will give you a copy of a dictionary
# {**foods[0], 'age':1}
# This nondestructively makes a copy -- foods will not be changed



# index
# [4,5,4].index(5)
# >>> 1
# [4,5,4].index(4)
# >>> 0 (bc that's the first place it sees it)
# [4,5,4].index(7)
# >>> ValueError: 7 is nout in list

# count
# [4,5,4].count(5)
# >>> 1 (bc there is only 1 5 in the list)
# [4,5,4].count(4)
# >>> 2
# [4,5,4].index(7)
# >>> 0

# append to add something new to the end
# numbers_list.append(21)
# Adds 21 to the end of the list

# pop to remove something from the end
# numbers_list.pop()
# if list is already empty, you'll get an IndexError

# append and pop do not work on tuple or strings


# You can iterate over a set (but it doesn't have indices)
# You can also convert a set back into a list


# Two ways to update a dictionary...
# One is with brackets
# food['name'] = "Hot Dog"
# Other way is update method
# Should use this if you're going to update just a single key and value pair (would just use brackets)
# If you have an unspecified amount or more than one to update, then use update
# key_value_pairs = {'name': 'Ice Cream', 'age': 1}
# item.update(key_value_pairs)
# Update is destructive
# can also use spread operator**
# {**item, **key_value_pairs}