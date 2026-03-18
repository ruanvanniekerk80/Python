from pizza import make_pizza
from makePizza import *
from pizza import *
import pizza as p
from pizza import make_pizza as mp
import pizza  # Importing the pizza module

# Calling the make_pizza function from the pizza module
# Making a 16-inch pizza with pepperoni
pizza.make_pizza(16, 'pepperoni')

# Making a 12-inch pizza with mushrooms, green peppers, and extra cheese
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#####################################################################################
# The making_pizzas.py example would look like this if we want to import just the function we’re going to use:
# Importing the make_pizza function directly from the pizza module

# Calling the make_pizza function
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

#############################################################################################
# Here we give the function make_pizza() an alias, mp(), by importing make_pizza as mp.
# The as keyword renames a function using the alias you provide:

mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')
##############################################################################################
# You can also provide an alias for a module name. Giving a module a short alias,
# like p for pizza, allows you to call the module’s functions more quickly.
# Calling p.make_pizza() is more concise than calling pizza.make_pizza():

p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
#############################################################################################
# You can tell Python to import every function in a module by using the asterisk (*) operator:

make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')

make_pizza2(18, 'cheese')
make_pizza2(15, 'pepperoni', 'green peppers', 'extra cheese')

my_pizza(18, "mushroom", "avo", "ham", "cheese")
