import pymongo

# Fungsi untuk menghapus koleksi customers
def delete_customers_collection():
    # Menghubungkan ke server MongoDB (default: localhost, port: 27017)
    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    
    # Memilih database yang akan digunakan
    mydb = myclient["mydatabase"]
    
    # Memilih koleksi yang akan dihapus
    mycol = mydb["customers"]
    
    # Menghapus koleksi menggunakan metode drop()
    drop_result = mycol.drop()
    
    # Memeriksa apakah koleksi berhasil dihapus
    if drop_result:
        print("Koleksi 'customers' berhasil dihapus.")
    else:
        print("Koleksi 'customers' tidak ada.")
        
# Memanggil fungsi untuk menghapus koleksi customers
delete_customers_collection()
