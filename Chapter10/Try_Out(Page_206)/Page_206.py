# 10-11. Favorite Number:

import json
number =input("What is your favorite number? :")

with open("favorite_number.json","w") as file:
    json.dump(number,file)


with open("favorite_number.json") as file:
    number =json.load(file)
print(f"I know yur favorite number! it's {number} ")

# 10-12. Favorite Number Remembered:

filename = "favorite_number.json"

try:
    with open(filename) as file:
        number = json.load(file)
        print(f"I know your favorite number! It's {number}.")

except FileNotFoundError:
    number = json.load(file)
    print(f"I know your favorite number?")
    with open (filename,"w") as file:
        json.dump(number,file)
        print("I'ill remember your favorite number!")

#  10-13. User Dictionary:

import json

user = {
    "name": input("What is your name? "),
    "age": input("What is your age? "),
    "city": input("What city do you live in? ")
}

with open("user.json", "w") as file:
    json.dump(user, file)

# Read it back
with open("user.json") as file:
    saved_user = json.load(file)

print("\nHere is what I know about you:")
for key, value in saved_user.items():
    print(f"{key}: {value}")


# 10-14. Verify User:

import json

filename = "username.json"

def get_stored_username():
    try:
        with open(filename) as file:
            return json.load(file)
    except FileNotFoundError:
        return None

def get_new_username():
    username = input("What is your username? ")
    with open(filename, "w") as file:
        json.dump(username, file)
    return username

def greet_user():
    username = get_stored_username()
    
    if username:
        correct = input(f"Is this your username: {username}? (yes/no): ")
        
        if correct.lower() == "yes":
            print(f"Welcome back, {username}!")
        else:
            username = get_new_username()
            print(f"We'll remember you when you come back, {username}!")
    
    else:
        username = get_new_username()
        print(f"We'll remember you when you come back, {username}!")

greet_user()