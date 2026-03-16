# 5-8. Hello Admin / 5-9. No Users: Add

usernames = ['admin', 'eric', 'sarah', 'jordan', 'maya']

if usernames:
    for username in usernames:
        if username == 'admin':
            print("hello admin, would you like to see a status report")
        else:
            print(f"Hello {username.title()},thank you for logging in again")
else:
    print("We need to find some users!")
print()

# 5-10. Checking Usernames:

current_users = ['Admin', 'John', 'Sarah', 'Mike', 'BETH']
new_users = ['john', 'KEVIN', 'beth', 'Ryan', 'Zoe']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(
            f"The username '{new_user}' is already taken. Please enter a new username.")
    else:
        print(f"The username '{new_user}' is available!")
print()

# 5-11. Ordinal Numbers:

numbers = list(range(1, 10))

for number in numbers:
    if number == 1:
        suffix = "st"
    elif number == 2:
        suffix = "nd"
    elif number == 3:
        suffix = "rd"
    else:
        suffix = "th"

    print(f"{number}{suffix}")
