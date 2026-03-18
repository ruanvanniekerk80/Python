# 4-1. Pizzas:

# Define a list of favorite pizza names
favorite_pizzas = ["Regina", "Three Cheese", "avo and feta"]

# Use a for loop to iterate through each pizza in the list
for pizza in favorite_pizzas:
    # Print a personalized message for each pizza type
    print(f"I love {pizza} pizza")

# This print statement is outside the loop, so it only runs once at the end
print("I really love Pizza")


# 4-2. Animals:

# Create a list of animals that share a common characteristic
animals = ["cat", "dog", "bird"]

# Print a blank line for better visual separation in the console
print()

# Loop through the animals list to describe each one
for animal in animals:
    # Use an f-string to insert the current animal into a sentence
    print(f"a {animal} would make a great pet")

# Print a final concluding statement outside the loop
print("Any of these animals would make a great pet!")
