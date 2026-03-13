# 3-1. Names:

# Create a list containing three names
names = ["joe", "jane", "john"]

# Print the entire list
print(names)

# Access the first name in the list (index 0) and store it in a variable
name = names[0]
print(name)  # Print the first name

# Access the second name in the list (index 1)
name = names[1]
print(name)  # Print the second name

# Access the second name again (index 1)
# NOTE: This was probably meant to be names[2] for the third name
name = names[1]
print(name)

print()  # Print an empty line for spacing


# 3-2. Greetings:

# Get the first name from the list
name = names[0]
# Print a greeting using an f-string
print(f"Good morning {name}")

# Get the second name from the list
name = names[1]
# Print a greeting message
print(f"Good to see you {name}")

# Get the second name again
# NOTE: This might also have been intended to be names[2]
name = names[1]
# Print another greeting message
print(f"How are you doing {name}")

print()  # Empty line for spacing


# 3-3. Your Own List:

# Create a list of car models
cars = ["BMW", "Ford Rangers", "Mustang GT"]

# Print a sentence using the first car in the list
print(f"I would really like to own a {cars[0]}")

# Print a sentence about the second car
print(f"a {cars[1]} is nice bakkie for offroad")

# Print a sentence about the third car
print(f"a {cars[2]} features a 4th-generation 5.0L Coyote V8 engine")
