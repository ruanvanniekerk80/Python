# 9-13. Dice: 
import random

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        return random.randint(1, self.sides)

# 6-sided die
die6 = Die()
print("6-sided die:")
for _ in range(10):
    print(die6.roll_die())

# 10-sided die
die10 = Die(10)
print("\n10-sided die:")
for _ in range(10):
    print(die10.roll_die())

# 20-sided die
die20 = Die(20)
print("\n20-sided die:")
for _ in range(10):
    print(die20.roll_die())

# 9-14. Lottery:

import random

lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

winning_ticket = random.sample(lottery_pool, 4)

print(f"Winning ticket: {winning_ticket}")
print("If your ticket matches these, you win!")


# 9-15. Lottery Analysis: 

import random

lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

my_ticket = [1, 'a', 5, 'c']
attempts = 0

while True:
    attempts += 1
    current_ticket = random.sample(lottery_pool, 4)

    if current_ticket == my_ticket:
        break

print(f"It took {attempts} tries to win!")

# 9-16. Python Module of the Week:

import random

names = ["Alice", "Bob", "Charlie"]
print(random.choice(names))  # picks one randomly