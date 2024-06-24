import mysql.connector

# Membuat koneksi ke database
mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

# Membuat objek cursor untuk melakukan query
mycursor = mydb.cursor()

# Contoh INNER JOIN: Menggabungkan tabel users dan products
def inner_join_example():
    sql = "SELECT \
      users.name AS user, \
      products.name AS favorite \
      FROM users \
      INNER JOIN products ON users.fav = products.id"
    
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    
    print("INNER JOIN Result:")
    for x in myresult:
        print(x)

# Contoh LEFT JOIN: Menggabungkan semua data dari tabel users dan cocokan dengan tabel products
def left_join_example():
    sql = "SELECT \
      users.name AS user, \
      products.name AS favorite \
      FROM users \
      LEFT JOIN products ON users.fav = products.id"
    
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    
    print("\nLEFT JOIN Result:")
    for x in myresult:
        print(x)

# Contoh RIGHT JOIN: Menggabungkan semua data dari tabel products dan cocokan dengan tabel users
def right_join_example():
    sql = "SELECT \
      users.name AS user, \
      products.name AS favorite \
      FROM users \
      RIGHT JOIN products ON users.fav = products.id"
    
    mycursor.execute(sql)
    myresult = mycursor.fetchall()
    
    print("\nRIGHT JOIN Result:")
    for x in myresult:
        print(x)

# Memanggil fungsi untuk menjalankan contoh JOIN
inner_join_example()
left_join_example()
right_join_example()

# Menutup koneksi database
mydb.close()
