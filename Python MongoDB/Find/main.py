import pymongo

# Menghubungkan ke server MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# Memilih database
mydb = myclient["mydatabase"]

# Memilih koleksi
mycol = mydb["customers"]

# Menggunakan find_one() untuk mengambil dokumen pertama
print("Menggunakan find_one() untuk mengambil dokumen pertama:")
first_doc = mycol.find_one()
print(first_doc)
print()

# Menggunakan find() untuk mengambil semua dokumen
print("Menggunakan find() untuk mengambil semua dokumen:")
all_docs = mycol.find()
for doc in all_docs:
    print(doc)
print()

# Menggunakan find() dengan parameter untuk hanya mengambil kolom 'name' dan 'address', tanpa '_id'
print("Menggunakan find() dengan hanya kolom 'name' dan 'address', tanpa '_id':")
selected_fields_docs = mycol.find({}, { "_id": 0, "name": 1, "address": 1 })
for doc in selected_fields_docs:
    print(doc)
print()

# Menggunakan find() dengan parameter untuk mengecualikan kolom 'address'
print("Menggunakan find() dengan mengecualikan kolom 'address':")
excluded_field_docs = mycol.find({}, { "address": 0 })
for doc in excluded_field_docs:
    print(doc)
print()

# Contoh kesalahan: Mencoba menggabungkan kolom yang diambil dan diabaikan dalam objek yang sama
print("Contoh kesalahan: Menggabungkan kolom yang diambil dan diabaikan:")
try:
    error_docs = mycol.find({}, { "name": 1, "address": 0 })
    for doc in error_docs:
        print(doc)
except Exception as e:
    print("Terjadi kesalahan:", e)
