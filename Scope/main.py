# Contoh Local Scope
def local_scope_example():
    x = 300  # Variabel lokal
    print("Dalam local_scope_example:", x)

local_scope_example()
# print(x)  # Ini akan mengakibatkan error karena x tidak dikenal di luar local_scope_example

# Contoh Function Inside Function
def function_inside_function_example():
    x = 300
    def inner_function():
        print("Dalam inner_function:", x)
    inner_function()

function_inside_function_example()

# Contoh Global Scope
x = 300

def global_scope_example():
    print("Dalam global_scope_example:", x)

global_scope_example()
print("Di luar fungsi:", x)

# Contoh Naming Variables
x = 300

def naming_variables_example():
    x = 200  # Variabel lokal dengan nama yang sama
    print("Dalam naming_variables_example:", x)

naming_variables_example()
print("Di luar fungsi:", x)

# Contoh Global Keyword
x = 300

def global_keyword_example():
    global x  # Gunakan global keyword untuk mengakses variabel global
    x = 200

global_keyword_example()
print("Setelah menggunakan global keyword:", x)

# Contoh Nonlocal Keyword
def nonlocal_keyword_example():
    x = "Jane"
    def inner_function():
        nonlocal x  # Gunakan nonlocal keyword untuk mengakses variabel dalam lingkup luar
        x = "hello"
    inner_function()
    return x

result = nonlocal_keyword_example()
print("Hasil nonlocal_keyword_example:", result)
