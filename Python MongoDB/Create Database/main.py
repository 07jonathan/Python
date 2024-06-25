import pymongo

# Langkah 1: Membuat objek MongoClient
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# Langkah 2: Menentukan nama database
mydb = myclient["mydatabase"]

# Langkah 3: Membuat koleksi dan memasukkan dokumen
mycollection = mydb["customers"]
mydocument = {"name": "John", "address": "Highway 37"}

# Memasukkan dokumen ke dalam koleksi
mycollection.insert_one(mydocument)

# Langkah 4: Memeriksa apakah database ada dengan mencantumkan semua database
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("Database tersebut ada.")
else:
    print("Database tersebut tidak ada.")
