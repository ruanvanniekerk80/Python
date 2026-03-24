# 5-3. Alien Colors #1: Basic 'if' statement
alien_color = "green"

# A single 'if' only runs if the condition is True.
if alien_color == "green":
    print("You have earned 5 points!") 

alien_color = 'red'

# This block is ignored because 'red' == 'green' is False.
if alien_color == 'green':
    print("You just earned 5 points!") 


# 5-4. Alien Colors #2: The 'if-else' chain
alien_color = "yellow"

# 'else' acts as a catch-all for anything that isn't 'green'.
if alien_color == "green":
    print("You just earned 5 points for shooting the alien!")
else:
    # Since 'yellow' != 'green', this block is triggered.
    print("you just earned 10 points")

# --- LOGIC NOTE ON 5-4 BELOW ---
alien_color = "green"

# NOTE: In this specific block, because you check for red and yellow first, 
# 'green' falls into the 'else' block, resulting in 15 points.
if alien_color == "red":
    print("You earned 5 points!")
elif alien_color == "yellow":
    print("You earned 10 points!")
else:
    print("You earned 15 points") 


# 5-5. Alien Colors #3: The 'if-elif-else' chain
alien_color = "green"

# This is the most efficient way to check multiple specific options.
if alien_color == "green":
    print("You earned 5 points!")  # Python finds a match here and skips the rest.
elif alien_color == "yellow":
    print("You earned 10 points!")
else:
    print("You earned 15 points!")


# 5-6. Stages of Life: Range Testing
age = 25

# In an elif chain, order matters! Python stops at the FIRST True condition.
if age < 2:
    print("You are a baby.")
elif age < 4:
    print("You are a toddler.")
elif age < 13:
    print("You are a kid.")
elif age < 20:
    print("You are a teenager.")
elif age < 65:
    # Even though 25 is also < 100, this is the first block that satisfies the age.
    print("You are an adult.")
else:
    print("The person is an elder")


# 5-7. Favorite Fruit: Independent 'if' statements
favorite_fruits = ['apple', 'banana', 'mango']

# We use separate 'if' statements (not elif) because we want to check 
# EVERY fruit. An 'elif' would stop after finding the first match.
if 'apple' in favorite_fruits:
    print("You really like apple!")

if "banana" in favorite_fruits:
    print("You really like bananas!") 

if "orange" in favorite_fruits:
    print("You really like oranges!")

if "mango" in favorite_fruits:
    print("You really like mangoes!")

if "grape" in favorite_fruits:
    print("You really like grapes!")