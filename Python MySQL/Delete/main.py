import mysql.connector

# Fungsi untuk menghubungkan ke database
def connect_to_database():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword",
            database="mydatabase"
        )
        return mydb
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

# Fungsi untuk menghapus record berdasarkan alamat
def delete_record_by_address(address):
    try:
        mydb = connect_to_database()
        if mydb:
            mycursor = mydb.cursor()

            # Query untuk menghapus record
            sql = "DELETE FROM customers WHERE address = %s"
            adr = (address, )

            # Melakukan execute query dengan parameter
            mycursor.execute(sql, adr)

            # Melakukan commit untuk menyimpan perubahan
            mydb.commit()

            # Menampilkan jumlah record yang terhapus
            print(mycursor.rowcount, "record(s) deleted")

            # Menutup cursor dan koneksi
            mycursor.close()
            mydb.close()
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Contoh penggunaan
if __name__ == "__main__":
    address_to_delete = "Yellow Garden 2"
    delete_record_by_address(address_to_delete)
