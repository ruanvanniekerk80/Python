users = {
    'bsnow': {   # Username as the key
        'first_name': 'Bob',
        'last_name': 'snow',
        'gender': "Male",
        'color_eyes': "blue",
        'location': 'Brazil'
    },
    'nsmith': {  # Another user
        'first_name': 'Natalie',
        'last_name': 'Smith',
        'gender': 'female',
        'color_eyes': 'brown',
        'location': 'London'
    },

    'jwick': {
        'first_name': 'John',
        'last_name': 'Wick',
        'gender': 'male',
        'color_eyes': 'green',
        'location': 'New York'
    }
}


# Loop through the outer dictionary
# 'username' holds the key, 'user_info' holds the inner dictionary
for username, user_info in users.items():
    print(f"\nUsername: {username}")

    # Combine first and last name from the inner dictionary
    full_name = f"{user_info['first_name']} {user_info['last_name']}"

    # Retrieve other user details
    gender = user_info['gender']
    eye_color = user_info['color_eyes']
    location = user_info['location']

    # Display formatted user information
    print(f"Full Name: {full_name}")
    print(f"Gender: {gender}")
    print(f"Eye Color: {eye_color}")
    print(f"Location: {location}")
    print()

    print(f"My name is {full_name}")

    print(5+5)