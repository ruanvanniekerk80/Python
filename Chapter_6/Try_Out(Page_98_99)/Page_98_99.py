# 6-1. Person:

person = {
    "first_name": "John",
    "last_name": "Smith",
    "age": 30,
    "city": "London"
}

for name, value in person.items():
    print(f"{name}: {value}")
print()
# 6-2. Favorite Numbers:

favorite_number = {
    "John": 7,
    "Sarah": 12,
    "Mike": 3,
    "Anna": 9,
    "David": 21
}
for name, number in favorite_number.items():
    print(f"{name}'s favorite number is {number}")
print()

# 6-3. Glossary:
glossary = {
    "variable": "a Container that stores a value.",
    "string": "s Sequence of characters inside quotes.",
    "list": "a Collection of items stored in a particular order.",
    "dictionary": "a Collection of key-value pairs.",
    "loop": "a Structure that repeats a block of code."
}

for word, meaning in glossary.items():
    print(f"{word}: {meaning}\n")
