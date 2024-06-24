import mysql.connector

# Buat koneksi ke database
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)

# Buat objek cursor untuk menjalankan perintah SQL
mycursor = mydb.cursor()

# Contoh 1: Memilih record dengan alamat "Park Lane 38"
def select_specific_address():
    sql = "SELECT * FROM customers WHERE address = 'Park Lane 38'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    print("Hasil query 1:")
    for x in myresult:
        print(x)

# Contoh 2: Memilih record dengan alamat yang mengandung kata "way"
def select_address_with_wildcard():
    sql = "SELECT * FROM customers WHERE address LIKE '%way%'"
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    print("\nHasil query 2:")
    for x in myresult:
        print(x)

# Contoh 3: Memilih record berdasarkan input pengguna dengan parameterisasi
def select_address_with_input(input_address):
    sql = "SELECT * FROM customers WHERE address = %s"
    adr = (input_address, )
    mycursor.execute(sql, adr)
    myresult = mycursor.fetchall()
    print("\nHasil query 3:")
    for x in myresult:
        print(x)

# Tes fungsi-fungsi query
if __name__ == "__main__":
    select_specific_address()
    select_address_with_wildcard()

    # Meminta input pengguna untuk query 3
    input_address = input("\nMasukkan alamat yang ingin dicari: ")
    select_address_with_input(input_address)

# Tutup koneksi setelah selesai
mycursor.close()
mydb.close()
