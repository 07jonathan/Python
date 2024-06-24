import mysql.connector

# Fungsi untuk menghapus tabel
def drop_table(hostname, username, password, database, table_name):
    try:
        # Membuat koneksi ke database
        mydb = mysql.connector.connect(
            host=hostname,
            user=username,
            password=password,
            database=database
        )

        # Membuat cursor
        mycursor = mydb.cursor()

        # SQL statement untuk menghapus tabel
        sql = f"DROP TABLE IF EXISTS {table_name}"

        # Eksekusi perintah SQL
        mycursor.execute(sql)

        # Commit perubahan ke database
        mydb.commit()

        print(f"Tabel {table_name} berhasil dihapus jika ada.")
    
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    finally:
        # Menutup koneksi
        if mydb.is_connected():
            mycursor.close()
            mydb.close()
            print("Koneksi ke database ditutup.")

# Contoh penggunaan
if __name__ == "__main__":
    hostname = "localhost"
    username = "yourusername"
    password = "yourpassword"
    database = "mydatabase"
    table_name = "customers"

    drop_table(hostname, username, password, database, table_name)
