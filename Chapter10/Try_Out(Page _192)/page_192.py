# 10-4. Guest:

name = input("what is your name? Ruan:")

with open("guest.txt","w") as file:
    file.write(name)

# 10-5. Guest Book:

with open("guest_book.txt", "w") as file:
    while True:
        name = input("Enter your name (or type 'q' to quit): ")
        
        if name == 'q':
            break
        
        file.write(name + "\n")