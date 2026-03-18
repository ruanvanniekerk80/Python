active = True   # Flag to control the loop

while active:
    user_input = input("Enter a number (1-10) or 'quit' to exit: ")

    # Exit immediately if user types 'quit'
    if user_input == 'quit':
        break

    # Check if input is a number
    if not user_input.isdigit():
        print("Invalid input. Please enter a number.")
        continue   # Skip rest of loop

    number = int(user_input)

    # Check if number is in range
    if number < 1 or number > 10:
        print("Number must be between 1 and 10.")
        continue   # Skip rest of loop

    # Special condition: number is 5
    if number == 5:
        print("You entered 5, exiting the loop.")
        active = False   # Stop loop using flag
        break            # Exit immediately

    # Valid input
    print(f"You entered {number}.")
