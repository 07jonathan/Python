# Membuat variabel dan mengassign nilai
x = 5          # integer
y = "John"     # string

# Menampilkan nilai variabel
print(x)        # output: 5
print(y)        # output: John

# Mengubah tipe variabel
x = "Sally"     # sekarang x menjadi string
print(x)         # output: Sally

# Casting tipe data
x_str = str(3)     # x_str akan menjadi '3'
y_int = int(3)     # y_int akan menjadi 3
z_float = float(3) # z_float akan menjadi 3.0

print(x_str)    # output: '3'
print(y_int)    # output: 3
print(z_float)  # output: 3.0

# Mengecek tipe data variabel
print(type(x))   # output: <class 'str'>
print(type(y))   # output: <class 'str'>

# String Representation dengan Single atau Double Quotes
x = "John"
x = 'John'

# Menyusun nama variabel yang legal
myVar = "John"
_myVar = "John"
my_var = "John"

# Menyusun nama variabel yang ilegal
# 2myVar = "John"  # Error: nama variabel tidak boleh dimulai dengan angka
# my-var = "John"   # Error: tanda "-" tidak diizinkan dalam nama variabel
# my var = "John"   # Error: spasi tidak diizinkan dalam nama variabel

# Menggunakan multi-word variable names dalam Camel Case
myVariableName = "John"

# Menggunakan multi-word variable names dalam Pascal Case
MyVariableName = "John"

# Menggunakan multi-word variable names dalam Snake Case
my_variable_name = "John"

# Assigning multiple variables in one line
x, y, z = "Orange", "Banana", "Cherry"

# Print multiple variables
print(x)
print(y)
print(z)

# Assigning the same value to multiple variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpacking a list into multiple variables
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# Output with print function
x = "Python is awesome"
print(x)

# Output with multiple variables using a comma separator
x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

# Output with concatenation using + operator
x = "Python " + "is " + "awesome"
print(x)

# Output sum of two numbers
x = 5
y = 10
print(x + y)  # Output: 15

# Global and Local variables
x = "awesome"

def myfunc():
    global x
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)  # output: Python is fantastic

def myfunc_local():
    x = "fantastic"
    print("Python is " + x)

myfunc_local()

print("Python is " + x)  # output: Python is awesome
