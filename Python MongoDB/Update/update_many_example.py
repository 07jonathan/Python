import pymongo

# Koneksi ke MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# Query untuk mencari dokumen yang akan diupdate
myquery = { "address": { "$regex": "^S" } }

# Nilai baru yang akan diupdate
newvalues = { "$set": { "name": "Minnie" } }

# Melakukan update untuk semua dokumen yang memenuhi kriteria
x = mycol.update_many(myquery, newvalues)

# Menampilkan jumlah dokumen yang berhasil diupdate
print(x.modified_count, "dokumen telah diupdate.")

# Menampilkan semua dokumen setelah update
print("Setelah update:")
for x in mycol.find():
    print(x)
