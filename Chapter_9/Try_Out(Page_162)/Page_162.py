# 9-1. Restaurant Class Definition
class Restaurant:
    """A simple model of a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print a summary of the restaurant."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Print a message indicating the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")

# Create an instance (object) of the Restaurant class
restaurant = Restaurant("Sunny Bistro", "Italian")

# Accessing attribute values directly
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Calling the methods defined in the class
restaurant.describe_restaurant()
restaurant.open_restaurant()

print()
print("*"*50) 

# 9-2. Creating Multiple Instances
# Creating three distinct restaurant objects from the same class
restaurant1 = Restaurant("Sunny Bistro", "Italian")
restaurant2 = Restaurant("Ocean Delight", "Seafood")
restaurant3 = Restaurant("Spice Heaven", "Indian")

# Calling describe_restaurant for each unique instance
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

# 9-3. User Class Definition
class User:
    """A class to represent a user profile."""
    
    def __init__(self, first_name, last_name, age, email):
        """Initialize the user's personal details."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        """Print a formatted summary of the user's information."""
        print(f"User: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")

    def greet_user(self):
        """Display a personalized greeting to the user."""
        print(f"Hello, {self.first_name}! Welcome back.")

# Creating instances of the User class
user1 = User("John", "Wick", 56, "john@example.com")
user2 = User("Lena", "Brown", 34, "lena@example.com")

# Demonstrating methods for user1
user1.describe_user()
user1.greet_user()

# Demonstrating methods for user2
user2.describe_user()
user2.greet_user()

# --- Lottery Simulation ---

import random

# Define a pool of possible numbers and letters
lottery_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

# The specific combination required to win
my_ticket = [1, 'a', 5, 'c']
attempts = 0

# Loop until the random sample matches the winning ticket
while True:
    attempts += 1
    # random.sample picks 4 unique elements from the pool
    current_ticket = random.sample(lottery_pool, 4)

    # Check if the generated ticket matches the target ticket
    if current_ticket == my_ticket:
        break  # Exit the loop if a match is found

print(f"It took {attempts} tries to win!")