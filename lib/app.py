# import ipdb

# Functions
# Defining functions starts with def and :
# Python uses snake case as default (instead of camel case, though camel case will still be used for clases)
# Classes are kind of like a blueprint for a thing - uses camel case
# Can do single or double quotes but you can't do backticks
# Colon signifies you're starting a new scope
# In python 2 things denote a new scope:
# 1 - colon
# 2 - indentation
# Python cares so much about indentation
# Lack of indentation essentially closes the function
# Technically you're supposed to do four spaces, but one space is still valid indentation -- everything inside the scope just needs to have the same indent
# if you just hit tab, it defaults to four spaces
# To do string interpolation, you use "f" and {} instead of backticks and ${}
# f stands for format

# "return" allows you to get a value back that can be used elsewhere, where as console.log just prints to the console
# console.log doesn't resolve anything, doesn't save any info or have info come back -- but return does

# can give variables default values
# def whatever_name_we_want(param1, param2="g'day") :
    # new_var = f"hello {param1} {param2}"
    # new_var = "hello" + param1 + param2 #concatonation
    # return new_var
# if you add a second return, it'd just get ignored
    # return new_var + "bonjour" 

# If you tried to pass too many arugments, then it would throw a TypeError
# In JavaScript, it would just accept the number of arguments that it was expecting and ignore the rest
# Python is more strict that JavaScript
# result = whatever_name_we_want("howdy", "bonjour")

# Can also assign the variables (and not pass them in in order)
# This is important for object oriented programming
# result = whatever_name_we_want(param2 = "bonjour", param1 = "howdy")

# print(result)


# Conditionals:
# def is_it_true(item):
    # I want to return "yes" if something is truthy
    # if item:
        # return "yes"
    # Return "no" if something is falsey
#     else:
#         return "no"
    
# result = is_it_true(None)
# print(result)

# .strip() removes spaces from front and end of string
# In JavaScript an empty array is truthy
# In Python, an empty list is falsey

# empty_list = []
# empty_list.append("hello")

# Python has tuples!
# Looks like a list... but....
# my_tuple = (1,2,3,4,5,6)
# You can't mutate the tuple -- it's immutable
# tuples also take up less space in memory -- will see a lot of these in phase 4

# no .map() in python (which iterates through an array - and do something to each item in the array and add it to a new array)
# Instead you have list comprehension -- doe sthe same thing as .map() but has weird syntax
# greetings = ["hello", "hi","sup"]
# result = [ item.title() for item in greetings ]
# print( result )

# Btw, when declaring a variable, you don't have to use let, const, or var
# result = "pizza"
# result = "not pizza"
# If you want something to be a constant, technically you would make it uppercase, but actually it still lets you do it (but it can signal to other developers that it shouldn't be changed)
# MY_RESULT = "I'm a constant"
# MY_RESULT = "but like not really"
# aka there are no true constants in python

# typing "python" in the terminal is the equivalent to typing "node" for javascript

# SCOPE
# basketball = 'Shaq'
# def add_last_name() :
#     basketball += "O'Neil"
# UnBoundLocalError can happen when python is unable to grab something -- an issue with scope
# You can fix this with the "global" key word...
# def add_last_name() :
#     global basketball
#     basketball += "O'Neil"

# DICTIONARIES (the equivalent to JavaScript objects)
# keys should all be strings in general
# my_dictionary = {
#     "key" : "value",
#     "key-two" : "value two",
#     "key3" : "value 3"
# }
# Can't use dot notation to access keys, must use bracket notation
# my_dictionary["key-two"] #will return the value for key-two
# If you wanted to add something to your dictionary...
# my_dictionary["new_thing"] = "hello"
# key goes in the brackets, new value goes after =

# You can make errors... and fire them like you would a function
# def make_error():
#     raise Exception("I AM AN ERROR")

# make_error()

# pytest -x will just go through the tests until you hit your first failed test

# import ipdb
# ipdb is the debugger in python
# "ipdb.set_trace()" will initiate it

# "with" keyword with pytest (with pytest.raises(TYpeError))... it basically says it expects it to raise a TypeError for that scenario

def make_error():
    try:
        "hello" + 1
    # "except" is same idea as "catch" in JavaScript
    # instead of erroring out, it will print out this message..
    # Also nice bc you can make the error message more specific
    except ZeroDivisionError:
        print("you may not do this")
    except TypeError:
        print("Got a type error")

make_error()