# JSON Practice Program
# Demonstrates saving and loading data using JSON

import json  # Import the JSON module to work with JSON files

# 10-12. Favorite Number Remembered

filename = "favorite_number.json"  # File where the favorite number will be stored

try:
    # Try to open and read the file
    with open(filename) as file:
        number = json.load(file)  # Load the number from the JSON file
        print(f"I know your favorite number! It's {number}.")  # Display it

except FileNotFoundError:
    # If the file does not exist, ask the user for their favorite number
    number = input("What is your favorite number? ")

    # Save the number to the file
    with open(filename, "w") as file:
        json.dump(number, file)

    print("I'll remember your favorite number!")  # Confirm saving

# Print a separator line for better output readability
print("\n" + "*" * 50)

# 10-13. User Dictionary

# Create a dictionary with user input
user = {
    "name": input("What is your name? "),
    "age": input("What is your age? "),
    "city": input("What city do you live in? ")
}

# Save the dictionary to a JSON file
with open("user.json", "w") as file:
    json.dump(user, file)

# Read the data back from the file
with open("user.json") as file:
    saved_user = json.load(file)

# Display the stored user information
print("\nHere is what I know about you:")
for key, value in saved_user.items():  # Loop through dictionary items
    print(f"{key}: {value}")  # Print each key-value pair

# Print another separator line
print("\n" + "*" * 50)

# 10-14. Verify User

filename = "username.json"  # File where the username will be stored


def get_stored_username():
    """Retrieve the stored username if it exists."""
    try:
        with open(filename) as file:
            return json.load(file)  # Return the stored username
    except FileNotFoundError:
        return None  # Return None if file does not exist


def get_new_username():
    """Ask for a new username and save it."""
    username = input("What is your username? ")

    # Save the new username to the file
    with open(filename, "w") as file:
        json.dump(username, file)

    return username  # Return the new username


def greet_user():
    """Greet the user and verify their identity."""
    username = get_stored_username()  # Get stored username if available

    if username:
        # Ask user to confirm their username
        correct = input(f"Is this your username: {username}? (yes/no): ")

        if correct.lower() == "yes":
            print(f"Welcome back, {username}!")  # Greet returning user
        else:
            # If incorrect, get and save a new username
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    else:
        # If no username is stored, ask for a new one
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")


# Call the function to run the program
greet_user()
