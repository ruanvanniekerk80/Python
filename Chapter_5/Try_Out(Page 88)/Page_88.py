# 5-8. Hello Admin / 5-9. No Users:

usernames = ['admin', 'eric', 'sarah', 'jordan', 'maya']  # List of users

# Check if the list is NOT empty
if usernames:
    # Loop through each username in the list
    for username in usernames:

        # Special message for admin
        if username == 'admin':
            print("hello admin, would you like to see a status report")

        # Message for all other users
        else:
            print(f"Hello {username.title()}, thank you for logging in again")

# If the list is empty, this will run instead
else:
    print("We need to find some users!")

print()  # Blank line for spacing

# 5-10. Checking Usernames:

current_users = ['Admin', 'John', 'Sarah', 'Mike', 'BETH']  # Existing users
new_users = ['john', 'KEVIN', 'beth', 'Ryan', 'Zoe']        # New users trying to register

# Convert all current usernames to lowercase for case-insensitive comparison
current_users_lower = [user.lower() for user in current_users]

# Loop through each new user
for new_user in new_users:
    
    # Check if the lowercase version already exists
    if new_user.lower() in current_users_lower:
        print(
            f"The username '{new_user}' is already taken. Please enter a new username.")
    
    # Otherwise, it's available
    else:
        print(f"The username '{new_user}' is available!")

print()  # Blank line

# 5-11. Ordinal Numbers:

numbers = list(range(1, 10))  # Create a list from 1 to 9

# Loop through each number
for number in numbers:
    
    # Assign correct suffix based on the number
    if number == 1:
        suffix = "st"
    elif number == 2:
        suffix = "nd"
    elif number == 3:
        suffix = "rd"
    else:
        suffix = "th"  # Default for most numbers

    # Print number with its suffix (e.g., 1st, 2nd, 3rd)
    print(f"{number}{suffix}")