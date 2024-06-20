# Membuat tuple
mytuple = ("apple", "banana", "cherry")

# Menampilkan jumlah item dalam tuple
print("Panjang tuple:", len(mytuple))

# Mengakses item dengan indeks
print("Item pertama:", mytuple[0])
print("Item kedua dari akhir:", mytuple[-2])

# Mengakses range indeks
print("Dari indeks 1 sampai 2:", mytuple[1:3])

# Mengecek apakah item ada di dalam tuple
if "banana" in mytuple:
    print("'banana' ditemukan di dalam tuple")

# Mengubah nilai dalam tuple (konversi ke list dan ubah item)
x = list(mytuple)
x[1] = "kiwi"
mytuple = tuple(x)
print("Setelah diubah:", mytuple)

# Menambahkan item ke dalam tuple (konversi ke list dan append)
x = list(mytuple)
x.append("orange")
mytuple = tuple(x)
print("Setelah ditambahkan:", mytuple)

# Menghapus item dari tuple (konversi ke list, hapus item, konversi kembali)
x = list(mytuple)
x.remove("kiwi")
mytuple = tuple(x)
print("Setelah dihapus:", mytuple)

# Unpacking tuple
fruits = ("apple", "banana", "cherry")
green, yellow, red = fruits
print("Unpacking tuple:", green, yellow, red)

# Menggabungkan dua tuple
tuple1 = ("a", "b", "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print("Menggabungkan tuple:", tuple3)
