import mysql.connector

# Menghubungkan ke database MySQL
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

# Membuat objek cursor untuk melakukan query
mycursor = mydb.cursor()

try:
    # Query untuk mengambil 5 record pertama dari tabel customers
    mycursor.execute("SELECT * FROM customers LIMIT 5")
    
    # Mengambil hasil query
    myresult = mycursor.fetchall()
    
    # Menampilkan hasil
    print("5 Customers Pertama:")
    for x in myresult:
        print(x)

    # Query untuk mengambil 5 record, dimulai dari record ke-3
    mycursor.execute("SELECT * FROM customers LIMIT 5 OFFSET 2")
    
    # Mengambil hasil query
    myresult_offset = mycursor.fetchall()
    
    # Menampilkan hasil
    print("\n5 Customers Mulai dari Record ke-3:")
    for x in myresult_offset:
        print(x)

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Menutup cursor dan koneksi ke database
    mycursor.close()
    mydb.close()
