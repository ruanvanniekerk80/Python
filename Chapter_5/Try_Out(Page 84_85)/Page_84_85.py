# 5-3. Alien Colors #1:

alien_color = "green"
if alien_color == "green":
    print("You have earned 5 points!")

alien_color = 'red'
if alien_color == 'green':
    print("You just earned 5 points!")  # This will NOT print

# 5-4. Alien Colors #2:
alien_color = "yellow"
if alien_color == "green":
    print("You just earned 5 points for shooting the alien!")
else:
    print("you just earned 10 points")

alien_color = "green"

if alien_color == "red":
    print("You earned 5 points!")
elif alien_color == "yellow":
    print("You earned 10 points!")
else:
    print("You earned 15 points")

print()
# 5-5 Alien Colors #3

alien_color = "green"

if alien_color == "green":
    print("You earned 5 points!")
elif alien_color == "yellow":
    print("You earned 10 points!")
else:
    print("You earned 15 points!")

print()

age = 25
if age < 2:
    print("You are a baby.")
elif age < 4:
    print("You are a toddler.")
elif age < 13:
    print("You are a kid.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    print("You are an adult.")
else:
    print("The person is an elder")
print()

#  5-7. Favorite Fruit:

favorite_fruits = ['apple', 'banana', 'mango']

if 'apple' in favorite_fruits:
    print("You really like apple!")
if "banana" in favorite_fruits:
    print("You really lek bananas!")
if "orange" in favorite_fruits:
    print("You really like oranges!")
if "mango" in favorite_fruits:
    print("You really like mangoes!")
if "grape" in favorite_fruits:
    print("You really like grapes!")
