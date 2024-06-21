# Contoh 1: Menggunakan lambda function untuk penambahan
x = lambda a: a + 10
print("Penambahan 5 + 10 =", x(5))  # Output: 15

# Contoh 2: Menggunakan lambda function untuk perkalian
x = lambda a, b: a * b
print("Perkalian 5 * 6 =", x(5, 6))  # Output: 30

# Contoh 3: Menggunakan lambda function di dalam fungsi lain
def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print("11 * 2 =", mydoubler(11))  # Output: 22
print("11 * 3 =", mytripler(11))  # Output: 33

# Contoh 4: Menggunakan lambda function dengan map()
numbers = [1, 2, 3, 4, 5]
# Menggunakan lambda function untuk menggandakan setiap elemen dalam daftar
doubled_numbers = list(map(lambda x: x * 2, numbers))
print("Doubled numbers:", doubled_numbers)  # Output: [2, 4, 6, 8, 10]

# Contoh 5: Menggunakan lambda function dengan filter()
# Menggunakan lambda function untuk menyaring angka genap dari daftar
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("Even numbers:", even_numbers)  # Output: [2, 4]

# Contoh 6: Menggunakan lambda function untuk menyusun daftar berdasarkan kriteria
names = ['John', 'Jane', 'Alice', 'Bob']
# Menggunakan lambda function untuk menyortir berdasarkan panjang nama
sorted_names = sorted(names, key=lambda x: len(x))
print("Sorted names by length:", sorted_names)  # Output: ['Bob', 'John', 'Jane', 'Alice']
