import pymongo

# Membuat koneksi ke server MongoDB (pastikan MongoDB sudah berjalan)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# Memilih database yang digunakan
mydb = myclient["mydatabase"]

# Memilih koleksi yang digunakan
mycol = mydb["customers"]

# Menambahkan beberapa data ke koleksi customers (opsional)
# mycol.insert_many([
#     {"name": "John", "age": 30},
#     {"name": "Jane", "age": 25},
#     {"name": "Doe", "age": 35},
# ])

# Mengambil data dari koleksi dan mengurutkannya secara ascending
print("Ascending Order:")
mydoc_asc = mycol.find().sort("name")
for x in mydoc_asc:
    print(x)

# Mengambil data dari koleksi dan mengurutkannya secara descending
print("\nDescending Order:")
mydoc_desc = mycol.find().sort("name", -1)
for x in mydoc_desc:
    print(x)
