# 2-3. Personal Message:
# Create a variable that stores a person's name
person_name = " Ruan"

# Print a greeting message to that person
# \n moves the text to a new line
print("Hello" + person_name + "\ndo you want to learn Python.")
print()  # prints a blank line for spacing


# 2-4. Name Cases:
# Store a name in a variable
person_name = "joe"

# .upper() converts the name to uppercase letters
print(f" {person_name.upper()}")
print()

# .lower() converts the name to lowercase letters
print(f" {person_name.lower()}")
print()

# .title() capitalizes the first letter of each word
print(f" {person_name.title()}")


# 2-5. Famous Quote:
# Print a famous quote directly
print('Napoleon Bonaparte - "Impossible is a word to be found only in the dictionary of fools"')
print()


# 2-6. Famous Quote 2:
# Store the famous person's name in a variable
famous_person = "Napoleon Bonaparte"

# Store the quote in another variable
message = '"Impossible is a word to be found only in the dictionary of fools."'

# Combine the variables and print the full quote
print(famous_person + " once said, " + message)


# 2-7. Stripping Names:
# Store a name with extra whitespace using \n (new line) and \t (tab)
person_name = "\n\t Napoleon Bonaparte \t\n"

# Print the name with whitespace so we can see the extra spacing
print("Name with whitespace:")
print(person_name)

# lstrip() removes whitespace from the left side of the string
print("\nUsing lstrip():")
print(person_name.lstrip())

# rstrip() removes whitespace from the right side of the string
print("\nUsing rstrip():")
print(person_name.rstrip())

# strip() removes whitespace from both sides of the string
print("\nUsing strip():")
print(person_name.strip())
print()


# 2-8. File Extensions:
# Store a filename with an extension
filename = "python_notes.txt"

# removesuffix() removes the specified ending from the string
print(filename.removesuffix(".txt"))
