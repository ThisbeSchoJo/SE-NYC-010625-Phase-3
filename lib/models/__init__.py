import sqlite3

# same as if we were going to manually go into the sqlite3 enviroment
# connects sqlite3 to the database:
CONN = sqlite3.connect('hotel_reviews.db') #you should store you connection in a variable so you're always working with the same object
# next line allows you to execute code
# the connection is used to commit/persist the changes to the database
CURSOR = CONN.cursor()

EXAMPLE_CONN = sqlite3.connect('pizzas.db')
EXAMPLE_CURSOR = EXAMPLE_CONN.cursor()