# 5-3. Alien Colors #1:

alien_color = "green"  # Assign the color 'green' to the variable

# Check if the alien is green
if alien_color == "green":
    print("You have earned 5 points!")  # This WILL run because the condition is true


alien_color = 'red'  # Change the alien's color to 'red'

# Check again if the alien is green
if alien_color == 'green':
    print("You just earned 5 points!")  # This will NOT print because the condition is false


# 5-4. Alien Colors #2:

alien_color = "yellow"  # Set alien color to yellow

# If the alien is green → 5 points, otherwise → 10 points
if alien_color == "green":
    print("You just earned 5 points for shooting the alien!")
else:
    print("you just earned 10 points")  # This runs because alien is NOT green


alien_color = "green"  # Change color to green

# Multiple conditions using if-elif-else
if alien_color == "red":
    print("You earned 5 points!")
elif alien_color == "yellow":
    print("You earned 10 points!")
else:
    print("You earned 15 points")  # This runs because it's green (not red or yellow)


print()  # Prints a blank line for spacing


# 5-5 Alien Colors #3

alien_color = "green"  # Set alien color

# Check multiple conditions again
if alien_color == "green":
    print("You earned 5 points!")  # This runs
elif alien_color == "yellow":
    print("You earned 10 points!")
else:
    print("You earned 15 points!")


print()  # Blank line


# Age classification example

age = 25  # Assign an age

# Check age ranges from smallest to largest
if age < 2:
    print("You are a baby.")
elif age < 4:
    print("You are a toddler.")
elif age < 13:
    print("You are a kid.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")  # This runs because 25 is less than 65
else:
    print("The person is an elder")


print()  # Blank line


# 5-7. Favorite Fruit:

favorite_fruits = ['apple', 'banana', 'mango']  # Create a list of favorite fruits

# Each 'if' checks independently (not elif!)
if 'apple' in favorite_fruits:
    print("You really like apple!")  # Runs

if "banana" in favorite_fruits:
    print("You really lek bananas!")  # Runs (small typo: "lek" → "like")

if "orange" in favorite_fruits:
    print("You really like oranges!")  # Does NOT run (not in list)

if "mango" in favorite_fruits:
    print("You really like mangoes!")  # Runs

if "grape" in favorite_fruits:
    print("You really like grapes!")  # Does NOT run