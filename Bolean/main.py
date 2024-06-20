# Evaluating Expressions
print("Evaluating Expressions:")
print(10 > 9)   # True
print(10 == 9)  # False
print(10 < 9)   # False
print()

# Using Booleans in Conditions
print("Using Booleans in Conditions:")
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
print()

# The bool() Function
print("The bool() Function:")
print(bool("Hello"))  # True
print(bool(15))       # True
print()

# Evaluating Variables
print("Evaluating Variables:")
x = "Hello"
y = 15

print(bool(x))  # True
print(bool(y))  # True
print()

# Most Values are True
print("Most Values are True:")
print(bool("abc"))               # True
print(bool(123))                 # True
print(bool(["apple", "cherry", "banana"]))  # True
print()

# Values that Evaluate to False
print("Values that Evaluate to False:")
print(bool(False))  # False
print(bool(None))   # False
print(bool(0))      # False
print(bool(""))     # False
print(bool(()))     # False
print(bool([]))     # False
print(bool({}))     # False
print()

# Custom Objects and __len__
print("Custom Objects and __len__:")
class MyClass:
  def __len__(self):
    return 0

myobj = MyClass()
print(bool(myobj))  # False
print()

# Functions Returning Boolean Values
print("Functions Returning Boolean Values:")

def myFunction():
  return True

print(myFunction())  # True

if myFunction():
  print("YES!")
else:
  print("NO!")
print()

# Built-in Functions that Return Boolean Values
print("Built-in Functions that Return Boolean Values:")
x = 200
print(isinstance(x, int))  # True
