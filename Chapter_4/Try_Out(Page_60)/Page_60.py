# 4-3 Counting to Twenty

for number in range(1, 21):
    print(number)
print()
# 4-5 Summing a Million
numbers = list(range(1, 1000001))

for number in numbers:
    print(number)

print()
# Create a list of numbers from one to one million
numbers = list(range(1, 1000001))

# Verify the list starts at 1
print(f"Minimum: {min(numbers)}")

# Verify the list ends at 1,000,000
print(f"Maximum: {max(numbers)}")

# Calculate the sum of all numbers in the list
print(f"Sum: {sum(numbers)}")
print()
# 4-6. Odd Numbers:

odd_numbers = list(range(1, 21, 2))

for number in odd_numbers:
    print(number)

print()
# 4-7. Threes:

threes = list(range(3, 31, 3))
for number_threes in threes:
    print(number_threes)
print()

# 4-8. Cubes:

cubes = []

for number_cubes in range(1, 11):
    cubes.append(number_cubes ** 3)
for cube in cubes:
    print(cube)
print()
   
# 4-9. Cube Comprehension: 

cubes = [number_cubes ** 3 for number in range(1, 11)]
print(cubes)