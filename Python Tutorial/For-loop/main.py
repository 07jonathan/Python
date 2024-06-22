# Basic For Loop
print("Basic For Loop:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
print()

# Looping Through a String
print("Looping Through a String:")
for char in "banana":
    print(char)
print()

# The break Statement
print("The break Statement:")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)
    if fruit == "banana":
        break
print()

# The break Statement before print
print("The break Statement before print:")
for fruit in fruits:
    if fruit == "banana":
        break
    print(fruit)
print()

# The continue Statement
print("The continue Statement:")
for fruit in fruits:
    if fruit == "banana":
        continue
    print(fruit)
print()

# The range() Function
print("The range() Function:")
for number in range(6):
    print(number)
print()

# The range() Function with start and end
print("The range() Function with start and end:")
for number in range(2, 6):
    print(number)
print()

# The range() Function with a step
print("The range() Function with a step:")
for number in range(2, 30, 3):
    print(number)
print()

# Else in For Loop
print("Else in For Loop:")
for number in range(6):
    print(number)
else:
    print("Finally finished!")
print()

# Else in For Loop with break
print("Else in For Loop with break:")
for number in range(6):
    if number == 3:
        break
    print(number)
else:
    print("Finally finished!")
print()

# Nested Loops
print("Nested Loops:")
adjectives = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for adjective in adjectives:
    for fruit in fruits:
        print(adjective, fruit)
print()

# The pass Statement
print("The pass Statement:")
for number in [0, 1, 2]:
    pass  # This loop does nothing
print("Pass statement example complete.")
