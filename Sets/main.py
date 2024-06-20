# Membuat Set
thisset = {"apple", "banana", "cherry"}
print("Set awal:", thisset)

# Menambahkan item ke Set
thisset.add("orange")
print("Set setelah menambahkan 'orange':", thisset)

# Menambahkan beberapa item dari iterable
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print("Set setelah menambahkan dari list:", thisset)

# Menghapus item dari Set
thisset.remove("banana")
print("Set setelah menghapus 'banana':", thisset)

# Menggunakan discard untuk menghapus item yang mungkin tidak ada
thisset.discard("banana")
print("Set setelah mencoba menghapus 'banana' dengan discard:", thisset)

# Menggunakan pop untuk menghapus item secara acak
popped_item = thisset.pop()
print("Item yang dihapus dengan pop:", popped_item)
print("Set setelah pop:", thisset)

# Mengosongkan Set
thisset.clear()
print("Set setelah clear:", thisset)

# Menggunakan union untuk menggabungkan Set
set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print("Hasil union dari set1 dan set2:", set3)

# Menggunakan intersection untuk mendapatkan elemen yang sama
set4 = {"apple", "banana", "cherry"}
set5 = {"google", "microsoft", "apple"}
set6 = set4.intersection(set5)
print("Hasil intersection dari set4 dan set5:", set6)

# Menggunakan difference untuk mendapatkan elemen yang unik di set pertama
set7 = set4.difference(set5)
print("Hasil difference dari set4 dan set5:", set7)

# Menggunakan symmetric_difference untuk mendapatkan elemen yang tidak sama di kedua set
set8 = set4.symmetric_difference(set5)
print("Hasil symmetric_difference dari set4 dan set5:", set8)

# Looping melalui Set
for item in set1:
    print("Item dalam set1:", item)

# Memeriksa keanggotaan
print("Apakah 'a' ada dalam set1?", 'a' in set1)
print("Apakah 'z' tidak ada dalam set1?", 'z' not in set1)

# Menggunakan metode isdisjoint
print("Apakah set1 dan set2 tidak memiliki elemen yang sama?", set1.isdisjoint(set2))

# Menggunakan metode issubset
set9 = {"a", "b"}
print("Apakah set9 adalah subset dari set1?", set9.issubset(set1))

# Menggunakan metode issuperset
print("Apakah set1 adalah superset dari set9?", set1.issuperset(set9))
