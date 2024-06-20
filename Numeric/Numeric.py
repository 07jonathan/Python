# Deklarasi berbagai tipe data numerik
x = 1    # int
y = 2.8  # float
z = 1j   # complex

# Menampilkan tipe data
print("Tipe data dari x:", type(x))   # Output: <class 'int'>
print("Tipe data dari y:", type(y))   # Output: <class 'float'>
print("Tipe data dari z:", type(z))   # Output: <class 'complex'>

# Contoh konversi tipe data
a = float(x)  # konversi int ke float
b = int(y)     # konversi float ke int
c = complex(x) # konversi int ke complex

# Menampilkan hasil konversi dan tipe data hasil konversi
print("Hasil konversi int ke float:", a)    # Output: 1.0
print("Tipe data dari a:", type(a))        # Output: <class 'float'>

print("Hasil konversi float ke int:", b)    # Output: 2
print("Tipe data dari b:", type(b))        # Output: <class 'int'>

print("Hasil konversi int ke complex:", c)  # Output: (1+0j)
print("Tipe data dari c:", type(c))        # Output: <class 'complex'>
