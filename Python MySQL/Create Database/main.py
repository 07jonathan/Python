import mysql.connector

# Fungsi untuk membuat database baru
def create_database():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword"
        )
        mycursor = mydb.cursor()
        mycursor.execute("CREATE DATABASE mydatabase")
        print("Database 'mydatabase' berhasil dibuat.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Fungsi untuk menampilkan daftar semua database
def show_databases():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SHOW DATABASES")
        print("Daftar Database:")
        for db in mycursor:
            print(db[0])
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Fungsi untuk mencoba menghubungkan ke database yang ada
def check_database_exists(database_name):
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword",
            database=database_name
        )
        print(f"Database '{database_name}' ditemukan.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Panggil fungsi untuk membuat database baru
create_database()

# Panggil fungsi untuk menampilkan daftar semua database
show_databases()

# Panggil fungsi untuk memeriksa apakah database 'mydatabase' ada
check_database_exists('mydatabase')
