import pymongo

# Koneksi ke MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# Query untuk mencari dokumen yang akan diupdate
myquery = { "address": "Valley 345" }

# Nilai baru yang akan diupdate
newvalues = { "$set": { "address": "Canyon 123" } }

# Melakukan update satu dokumen yang pertama ditemukan
mycol.update_one(myquery, newvalues)

# Menampilkan semua dokumen setelah update
print("Setelah update:")
for x in mycol.find():
    print(x)
