# Contoh 1: Menggunakan iterable dan iterator bawaan (tuple)
print("Contoh 1: Menggunakan iterable dan iterator bawaan (tuple)")
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))  # Menampilkan nilai pertama
print(next(myit))  # Menampilkan nilai kedua
print(next(myit))  # Menampilkan nilai ketiga

print("\n")

# Contoh 2: Menggunakan iterable dan iterator bawaan (string)
print("Contoh 2: Menggunakan iterable dan iterator bawaan (string)")
mystr = "banana"

for x in mystr:
    print(x)  # Menampilkan setiap karakter dalam string

print("\n")

# Contoh 3: Membuat iterator custom
print("Contoh 3: Membuat iterator custom")
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 5:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

# Menggunakan try-except untuk menangani StopIteration
try:
    while True:
        print(next(myiter))
except StopIteration:
    pass

print("\n")

# Contoh 4: Membatasi iterasi custom hingga 20
print("Contoh 4: Membatasi iterasi custom hingga 20")
class MyNumbersLimited:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbersLimited()
myiter = iter(myclass)

for x in myiter:
    print(x)
