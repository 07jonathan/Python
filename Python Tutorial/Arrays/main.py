# Membuat daftar mobil (array of cars)
cars = ["Ford", "Volvo", "BMW"]

# Mengakses elemen array dengan indeks
# Menampilkan elemen pertama
print("Mobil pertama:", cars[0])  # Output: "Ford"

# Mengakses elemen array dengan slicing
# Menampilkan dua elemen pertama
print("Dua mobil pertama:", cars[:2])  # Output: ["Ford", "Volvo"]

# Mengubah elemen pertama dalam array
cars[0] = "Toyota"

# Menampilkan elemen array setelah perubahan
print("Daftar mobil setelah perubahan:", cars)  # Output: ["Toyota", "Volvo", "BMW"]

# Menentukan panjang array (jumlah elemen)
print("Jumlah mobil:", len(cars))  # Output: 3

# Looping melalui array dan mencetak setiap elemen
print("Daftar mobil:")
for car in cars:
    print(car)

# Menambahkan elemen baru pada array
cars.append("Honda")
print("Daftar mobil setelah penambahan:", cars)  # Output: ["Toyota", "Volvo", "BMW", "Honda"]

# Menghapus elemen dari array dengan indeks
cars.pop(1)  # Hapus elemen kedua
print("Daftar mobil setelah penghapusan dengan indeks:", cars)  # Output: ["Toyota", "BMW", "Honda"]

# Menghapus elemen dari array dengan nilai
cars.remove("BMW")
print("Daftar mobil setelah penghapusan dengan nilai:", cars)  # Output: ["Toyota", "Honda"]

# Menyalin array ke dalam array baru
cars_copy = cars.copy()
print("Salinan daftar mobil:", cars_copy)  # Output: ["Toyota", "Honda"]

# Menyusun array dalam urutan alfabet
cars_copy.sort()
print("Daftar mobil setelah disortir:", cars_copy)  # Output: ["Honda", "Toyota"]

# Membalik urutan array
cars_copy.reverse()
print("Daftar mobil setelah dibalik:", cars_copy)  # Output: ["Toyota", "Honda"]

# Menghitung jumlah elemen dengan nilai tertentu
count_toyota = cars_copy.count("Toyota")
print("Jumlah mobil dengan nilai 'Toyota':", count_toyota)  # Output: 1

# Menampilkan indeks elemen pertama dengan nilai tertentu
index_honda = cars_copy.index("Honda")
print("Indeks elemen dengan nilai 'Honda':", index_honda)  # Output: 1
