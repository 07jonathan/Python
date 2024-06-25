import pymongo

# Koneksi ke server MongoDB (pastikan MongoDB berjalan di localhost)
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# Pilih database yang akan digunakan
mydb = myclient["mydatabase"]

# Pilih koleksi (collection) yang akan digunakan
mycol = mydb["customers"]

# Kriteria untuk menghapus dokumen
myquery = { "address": "Mountain 21" }

# Hapus satu dokumen yang sesuai kriteria
result = mycol.delete_one(myquery)

# Menampilkan pesan jika dokumen berhasil dihapus
print(f"{result.deleted_count} dokumen berhasil dihapus.")

# Hapus semua dokumen yang memenuhi kriteria
result = mycol.delete_many(myquery)

# Menampilkan jumlah dokumen yang berhasil dihapus
print(f"{result.deleted_count} dokumen berhasil dihapus.")

# Hapus semua dokumen dalam koleksi
result = mycol.delete_many({})

# Menampilkan jumlah dokumen yang berhasil dihapus
print(f"{result.deleted_count} dokumen berhasil dihapus.")