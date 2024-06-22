# Membuat Dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Menampilkan Dictionary
print("Dictionary:", thisdict)

# Mengakses Item Dictionary
print("Brand:", thisdict["brand"])

# Menambahkan Item ke Dictionary
thisdict["color"] = "red"
print("Setelah Menambah Warna:", thisdict)

# Mengupdate Item dalam Dictionary
thisdict.update({"year": 2020})
print("Setelah Mengupdate Tahun:", thisdict)

# Menghapus Item dari Dictionary dengan pop()
thisdict.pop("model")
print("Setelah Menghapus Model:", thisdict)

# Menghapus Item dengan popitem()
thisdict.popitem()
print("Setelah Menggunakan popitem():", thisdict)

# Menghapus Item dengan del
del thisdict["year"]
print("Setelah Menghapus Tahun dengan del:", thisdict)

# Mengosongkan Dictionary dengan clear()
thisdict.clear()
print("Setelah Mengosongkan Dictionary dengan clear():", thisdict)

# Membuat Dictionary Baru untuk Operasi Lain
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

# Loop Melalui Dictionary
print("Kunci dalam Dictionary:")
for key in thisdict:
    print(key)

print("Nilai dalam Dictionary:")
for value in thisdict.values():
    print(value)

print("Pasangan Kunci-Nilai dalam Dictionary:")
for key, value in thisdict.items():
    print(key, ":", value)

# Menyalin Dictionary
mydict_copy = thisdict.copy()
print("Salinan Dictionary:", mydict_copy)

# Nested Dictionary
child1 = {
    "name": "Emil",
    "year": 2004
}
child2 = {
    "name": "Tobias",
    "year": 2007
}
child3 = {
    "name": "Linus",
    "year": 2011
}

myfamily = {
    "child1": child1,
    "child2": child2,
    "child3": child3
}

print("Dictionary Bersarang (Nested Dictionary):", myfamily)

# Mengakses Item dalam Nested Dictionary
print("Nama Anak Kedua:", myfamily["child2"]["name"])

# Loop Melalui Nested Dictionary
print("Loop Melalui Nested Dictionary:")
for key, value in myfamily.items():
    print("Kunci:", key)
    for subkey, subvalue in value.items():
        print(subkey, ":", subvalue)

# Menggunakan Metode Dictionary
keys = thisdict.keys()
print("Keys:", keys)

values = thisdict.values()
print("Values:", values)

items = thisdict.items()
print("Items:", items)

# Menggunakan get() untuk Mengakses Item
model = thisdict.get("model")
print("Model:", model)

# Menggunakan setdefault() untuk Mendapatkan Nilai atau Menambahkan Item
year = thisdict.setdefault("year", 1964)
print("Tahun dengan setdefault():", year)

# Menggunakan fromkeys() untuk Membuat Dictionary Baru
keys = ('key1', 'key2', 'key3')
new_dict = dict.fromkeys(keys, 0)
print("Dictionary Baru dengan fromkeys():", new_dict)
