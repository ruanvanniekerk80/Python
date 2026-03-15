# 3-4. Guest List:

# Create a list containing the names of three guests
guest_list = ["Jane", "Joe", "John"]

# Print a title for the list
print("Guest List for my Dinner:")

# Print an invitation message for the first guest (index 0)
print(
    f"1.Dear {guest_list[0]}, you are invite to a dinner next week Tuesday")

# Print an invitation message for the second guest (index 1)
print(
    f"2.To my friend {guest_list[1]}, you are invited to a dinner")

# Print an invitation message for the third guest (index 2)
print(
    f"3.To {guest_list[2]}, you are being invited to a dinner, hope you can make it")


# 3-5. Changing Guest List:

# Print a message saying that one guest cannot attend
print(f"\nUnable to attend: Sorry,{guest_list[1]} can't make the dinner.")

# Replace the guest who can't attend with a new guest
# Here we replace "Joe" with "Mike"
guest_list[1] = "Mike"

# Print a message showing the updated guest list
print("\nNew updated list with replaced guest:")

# Send new invitations to the updated list
print(
    f"1.Dear {guest_list[0]}, you are invited to a dinner")

print(
    f"2.Dear {guest_list[1]}, you are invited to a dinner")

print(
    f"3.Dear {guest_list[2]}, you are being invited to a dinner")


# 3-6. More Guests:

# Print a message saying a bigger table was found
print("\nFound bigger table, adding more guest to the list:")

# Add a new guest to the beginning of the list
guest_list.insert(0, "Anna")

# Add a new guest to the middle of the list
guest_list.insert(2, "David")

# Add a new guest to the end of the list
guest_list.append("sarah")

# Loop through the list and send invitations to everyone
for guest in guest_list:
    print(f"- Dear {guest}, you are invided to dinner ")


# 3-7. Shrinking Guest List:

# Print a message saying only two guests can be invited
print("\nSorry I can only ivite two people to dinner:")

# Remove guests one at a time using pop()
# pop() removes the last person from the list and returns their name
remove_guest1 = guest_list.pop()
remove_guest2 = guest_list.pop()
remove_guest3 = guest_list.pop()
remove_guest4 = guest_list.pop()

# Print apology messages to the removed guests
print(f"1.Sorry {remove_guest1} I can't invite you to dinner.")
print(f"2.Sorry {remove_guest2} I can't invite you to dinner.")
print(f"3.Sorry {remove_guest3} I can't invite you to dinner.")
print(f"4.Sorry {remove_guest4} I can't invite you to dinner.")


# Print a message for the remaining guests
print("\nThe remaining Guest still invited:")

# Loop through the remaining guests and confirm they are still invited
for guest in guest_list:
    print(f"{guest}, you are still invited to dinner")


# Remove the last two remaining guests using del
# After the first deletion, the second guest moves to index 0
del guest_list[0]
del guest_list[0]

# Print the list to confirm it is empty
print(f"\n Empty dinner list:{guest_list}")