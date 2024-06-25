import pymongo

# Fungsi untuk menampilkan hasil dari kueri
def print_results(mydoc):
    for x in mydoc:
        print(x)

# Koneksi ke server MongoDB
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# Pilih database dan koleksi
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

# 1. Kueri Sederhana: Temukan dokumen dengan alamat "Park Lane 38"
print("Dokumen dengan alamat 'Park Lane 38':")
myquery1 = { "address": "Park Lane 38" }
mydoc1 = mycol.find(myquery1)
print_results(mydoc1)

# 2. Kueri Lanjutan: Temukan dokumen dimana alamat dimulai dengan huruf "S" atau lebih besar
print("\nDokumen dengan alamat dimulai dengan huruf 'S' atau lebih besar:")
myquery2 = { "address": { "$gt": "S" } }
mydoc2 = mycol.find(myquery2)
print_results(mydoc2)

# 3. Filter dengan Ekspresi Reguler: Temukan dokumen dimana alamat dimulai dengan huruf "S"
print("\nDokumen dengan alamat dimulai dengan huruf 'S':")
myquery3 = { "address": { "$regex": "^S" } }
mydoc3 = mycol.find(myquery3)
print_results(mydoc3)
