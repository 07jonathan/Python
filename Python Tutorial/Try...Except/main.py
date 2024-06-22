# Contoh 1: Basic Exception Handling
try:
    print(x)  # Variabel x tidak didefinisikan
except:
    print("An exception occurred")

# Contoh 2: Multiple Exception Blocks
try:
    print(x)  # Variabel x tidak didefinisikan
except NameError:
    print("Variable x is not defined")
except:
    print("Something else went wrong")

# Contoh 3: Else Block
try:
    print("Hello")
except:
    print("Something went wrong")
else:
    print("Nothing went wrong")

# Contoh 4: Finally Block
try:
    print(x)  # Variabel x tidak didefinisikan
except:
    print("Something went wrong")
finally:
    print("The 'try except' is finished")

# Contoh 5: Raise an Exception
x = -1

try:
    if x < 0:
        raise Exception("Sorry, no numbers below zero")
except Exception as e:
    print(e)

# Contoh 6: Raise a Type Error
x = "hello"

try:
    if not isinstance(x, int):
        raise TypeError("Only integers are allowed")
except TypeError as e:
    print(e)
