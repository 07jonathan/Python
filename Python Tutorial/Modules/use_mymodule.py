# use_mymodule.py

# Mengimpor modul mymodule
import mymodule

# Menggunakan fungsi greeting
mymodule.greeting("Alice")

# Mengakses dictionary
age = mymodule.person1["age"]
print("Age:", age)

# Menggunakan fungsi add_numbers
result = mymodule.add_numbers(5, 7)
print("Sum:", result)

# Mengimpor dengan alias
import mymodule as mx
age = mx.person1["age"]
print("Age using alias:", age)

# Mengimpor item tertentu menggunakan from
from mymodule import add_numbers
result = add_numbers(10, 3)
print("Sum using from import:", result)
