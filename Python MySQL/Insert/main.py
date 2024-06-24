import mysql.connector

# Fungsi untuk memasukkan satu rekaman
def insert_single_record(name, address):
    mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="mydatabase"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = (name, address)

    mycursor.execute(sql, val)
    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    mycursor.close()
    mydb.close()

# Fungsi untuk memasukkan beberapa rekaman
def insert_multiple_records(values):
    mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="mydatabase"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"

    mycursor.executemany(sql, values)
    mydb.commit()

    print(mycursor.rowcount, "records inserted.")
    mycursor.close()
    mydb.close()

# Fungsi untuk memasukkan satu rekaman dan mendapatkan ID-nya
def insert_record_get_id(name, address):
    mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="mydatabase"
    )

    mycursor = mydb.cursor()

    sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
    val = (name, address)

    mycursor.execute(sql, val)
    mydb.commit()

    print("1 record inserted, ID:", mycursor.lastrowid)
    mycursor.close()
    mydb.close()

# Contoh penggunaan fungsi
if __name__ == "__main__":
    insert_single_record("John", "Highway 21")

    values = [
        ('Peter', 'Lowstreet 4'),
        ('Amy', 'Apple st 652'),
        ('Hannah', 'Mountain 21'),
        ('Michael', 'Valley 345'),
        ('Sandy', 'Ocean blvd 2'),
        ('Betty', 'Green Grass 1'),
        ('Richard', 'Sky st 331'),
        ('Susan', 'One way 98'),
        ('Vicky', 'Yellow Garden 2'),
        ('Ben', 'Park Lane 38'),
        ('William', 'Central st 954'),
        ('Chuck', 'Main Road 989'),
        ('Viola', 'Sideway 1633')
    ]
    insert_multiple_records(values)

    insert_record_get_id("Michelle", "Blue Village")
