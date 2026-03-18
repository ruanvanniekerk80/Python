# 4-3 Counting to Twenty
# Use range(1, 21) to generate numbers from 1 up to (but not including) 21
for number in range(1, 21):
    print(number)

print()

# 4-5 Summing a Million
# Create a list containing 1 million integers
numbers = list(range(1, 1000001))

# Printing 1 million lines can be very slow; usually, we just verify the data
# (If you run this, it might take a moment to finish scrolling!)
for number in numbers:
    print(number)

print()

# Verification of the million-item list
numbers = list(range(1, 1000001))

# Use min() to find the smallest value in the list
print(f"Minimum: {min(numbers)}")

# Use max() to find the largest value in the list
print(f"Maximum: {max(numbers)}")

# Use sum() to add every single number in the list together
print(f"Sum: {sum(numbers)}")

print()

# 4-6. Odd Numbers:
# range(start, stop, step) -> starts at 1, stops at 21, skips by 2
odd_numbers = list(range(1, 21, 2))

for number in odd_numbers:
    print(number)

print()

# 4-7. Threes:
# Generates a list of multiples of 3 from 3 to 30
threes = list(range(3, 31, 3))
for number_threes in threes:
    print(number_threes)

print()

# 4-8. Cubes:
cubes = []

# Loop through numbers 1 to 10
for number_cubes in range(1, 11):
    # The ** operator represents an exponent (power of 3)
    cubes.append(number_cubes ** 3)

# Loop through the newly created list to print each cube
for cube in cubes:
    print(cube)

print()
   
# 4-9. Cube Comprehension: 
# A list comprehension combines the for loop and the creation of new elements into one line
# Note: Changed 'for number' to 'for number_cubes' to match the expression
cubes = [number_cubes ** 3 for number_cubes in range(1, 11)]
print(cubes)