#8-3. T-Shirt:

def make_shirt(size,message):
    """Summarizes the shirt size and the printed message"""
    print(f"\nI'm making a {size} shirt.")
    print(f"It will say: '{message}'")


make_shirt('medium', 'Code is Life')
make_shirt(message="Python Pro", size="large")
print("*"*100)
#  8-4. Large Shirts:

def make_shirt(size='large', message='I love Python'):
    """Summarizes shirt details with default values."""
    print(f"\nOrder: {size.upper()} shirt.")
    print(f"Message: {message}")
    


make_shirt()
make_shirt('medium')
make_shirt('small', 'Keep Coding')

print("*"*100)
# 8-5. Cities:

def describe_city(city, country='South Africa'):
    """Prints a simple sentence about a city and its country."""
    print(f"{city.title()} is in {country.title()}.")

# 1. City in the default country
describe_city('Johannesburg')

# 2. Another city in the default country
describe_city('Cape Town')

# 3. A city in a different country (must provide the second argument)
describe_city('Reykjavik', 'Iceland')