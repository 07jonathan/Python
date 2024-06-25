import pymongo

# Langkah 1: Koneksi ke MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

# Langkah 2: Membuat Koleksi dengan Menyisipkan Dokumen
mycol = mydb["customers"]
# Menyisipkan dokumen ke dalam koleksi "customers"
mycol.insert_one({"name": "John", "address": "Highway 37"})

# Langkah 3: Mengecek apakah Koleksi Ada
collist = mydb.list_collection_names()
if "customers" in collist:
    print("Koleksi 'customers' ada.")
else:
    print("Koleksi 'customers' tidak ada.")
