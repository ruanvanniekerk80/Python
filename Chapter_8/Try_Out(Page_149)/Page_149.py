# 8-12. Sandwiches:

def make_sandwich(*items):
    print("\nMaking a sandwich with :")
    for item in items:
        print(f"-{item}")


make_sandwich("ham", "Cheese")
make_sandwich("chicken", "lettuce", "mayo")
make_sandwich("egg")
print()

# 8-13. User Profile:

def build_profile(first, last, **user_info):
    profile = {
        "first_name": first,
        "last_name": last
    }

    for key, value in user_info.items():
        profile[key] = value

    return profile


my_profile = build_profile(
    "Joe",
    "Smith"
)

print(f"\n {my_profile}")

# 8-14. Cars:

def make_car(manufacturer, model, **car_info):
    """Store information about a car in a dictionary."""
    car_info['manufacturer'] = manufacturer
    car_info['model'] = model
    return car_info

# Calling the function as requested
car = make_car('subaru', 'outback', color='blue', tow_package=True)

print(car)


