import mysql.connector

# Membuat koneksi ke database
mydb = mysql.connector.connect(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="mydatabase"
)

# Membuat objek cursor untuk menjalankan perintah SQL
mycursor = mydb.cursor()

# Menjalankan query SQL untuk mengambil data dari tabel customers dan mengurutkannya secara ascending
sql = "SELECT * FROM customers ORDER BY name"
mycursor.execute(sql)

# Mengambil semua baris hasil query
myresult = mycursor.fetchall()

# Menampilkan hasil pengurutan secara ascending
print("Hasil pengurutan ascending berdasarkan nama:")
for x in myresult:
    print(x)

# Mengurutkan secara descending
sql_desc = "SELECT * FROM customers ORDER BY name DESC"
mycursor.execute(sql_desc)

# Mengambil hasil pengurutan descending
myresult_desc = mycursor.fetchall()

# Menampilkan hasil pengurutan secara descending
print("\nHasil pengurutan descending berdasarkan nama:")
for x in myresult_desc:
    print(x)

# Menutup koneksi database
mydb.close()
