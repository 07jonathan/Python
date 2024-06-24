import mysql.connector

# Membuat koneksi ke database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

# Membuat objek cursor untuk eksekusi perintah SQL
mycursor = mydb.cursor()

try:
    # Contoh 1: Update menggunakan nilai langsung dalam query
    sql = "UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"
    mycursor.execute(sql)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")

    # Contoh 2: Update menggunakan placeholder %s
    sql = "UPDATE customers SET address = %s WHERE address = %s"
    val = ("Canyon 123", "Valley 345")
    mycursor.execute(sql, val)
    mydb.commit()
    print(mycursor.rowcount, "record(s) affected")

except mysql.connector.Error as err:
    print("Something went wrong:", err)

finally:
    # Menutup koneksi dan cursor
    mycursor.close()
    mydb.close()
