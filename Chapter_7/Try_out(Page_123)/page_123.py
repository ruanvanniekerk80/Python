# 7-4. Pizza Toppings:

while True:
    topping = input("Enter a pizza topping(or 'quit' to exit):")
    if topping == 'quit':
        break
    else:
        print(f"I'll add {topping} to your pizza.")


# 7-5. Movie Tickets:

while True:
    age = input("Enter your age (or 'quit' to exit): ")

    if age == 'quit':
        break

    age = int(age)

    if age < 3:
        print("Your ticket is free.")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")

# 7-6. Three Exits:

########### 1. Using a condition in the while statement #######

topping = ""

while topping != "quit":
    topping = input("Enter a topping:")

    if topping != "quit":
        print(f"adding {topping}.")

########### 2. Using an active variable #######
active = True

while active:
    topping = input("Enter a topping: ")

    if topping == 'quit':
        active = False
    else:
        print(f"Adding {topping}.")

# 3. Using break
while True:
    topping = input("Enter a topping: ")

    if topping == 'quit':
        break

    print(f"Adding {topping}.")


# 7-7. Infinity:
while True:
    print("This loop will run forever!")
