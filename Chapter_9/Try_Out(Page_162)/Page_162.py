# 9-1. Restaurant:

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

# Create an instance
restaurant = Restaurant("Sunny Bistro", "Italian")

# Print attributes individually
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Call methods
restaurant.describe_restaurant()
restaurant.open_restaurant()
print()
print("*"*50) 
# 9-2. Three Restaurants:

restaurant1 = Restaurant("Sunny Bistro", "Italian")
restaurant2 = Restaurant("Ocean Delight", "Seafood")
restaurant3 = Restaurant("Spice Heaven", "Indian")

# Describe each restaurant
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# 9-3. Users:

class User:
    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")

# Create users
user1 = User("John", "Wick", 56, "john@example.com")
user2 = User("Lena", "Brown", 34, "lena@example.com")

# Call methods for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

# 

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