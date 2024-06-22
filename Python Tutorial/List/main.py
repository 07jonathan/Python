# Membuat daftar
thislist = ["apple", "banana", "cherry", "kiwi", "mango"]

# Akses item berdasarkan indeks
print("Item pertama:", thislist[0])         # Mengakses item pertama
print("Item terakhir:", thislist[-1])      # Mengakses item terakhir

# Mengubah item
thislist[1] = "blackcurrant"
print("Daftar setelah diubah:", thislist)

# Menambah item
thislist.append("orange")
print("Daftar setelah menambahkan item:", thislist)

# Mengubah rentang item
thislist[2:4] = ["watermelon", "pear"]
print("Daftar setelah mengubah rentang item:", thislist)

# Menghapus item berdasarkan nilai
thislist.remove("pear")
print("Daftar setelah menghapus item:", thislist)

# Loop melalui daftar
print("Loop melalui daftar:")
for item in thislist:
    print(item)

# Loop melalui daftar menggunakan indeks
print("Loop melalui indeks:")
for i in range(len(thislist)):
    print(thislist[i])

# Loop melalui daftar dengan while
i = 0
print("Loop melalui indeks menggunakan while:")
while i < len(thislist):
    print(thislist[i])
    i += 1

# Loop melalui daftar dengan list comprehension
print("List comprehension:")
[print(item) for item in thislist]

# Menyusun daftar secara alfabetis
thislist.sort()
print("Daftar setelah disortir:", thislist)

# Membalik urutan daftar
thislist.reverse()
print("Daftar setelah dibalik:", thislist)

# Menyalin daftar
mylist = thislist.copy()
print("Salinan daftar:", mylist)

# Menyambung dua daftar
tropical = ["pineapple", "papaya"]
thislist.extend(tropical)
print("Daftar setelah menyambung dua daftar:", thislist)

# Menghitung jumlah item
count = thislist.count("apple")
print("Jumlah item 'apple':", count)

# Menghitung indeks item
index = thislist.index("cherry")
print("Indeks item 'cherry':", index)
