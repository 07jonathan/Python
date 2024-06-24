import mysql.connector

# Fungsi untuk melakukan koneksi ke database
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

# Fungsi untuk melakukan SELECT dan menampilkan semua data
def select_all_from_customers():
    db = connect_to_database()
    if db:
        try:
            mycursor = db.cursor()
            mycursor.execute("SELECT * FROM customers")
            myresult = mycursor.fetchall()
            
            print("Showing all records from customers table:")
            for x in myresult:
                print(x)
            
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if db.is_connected():
                db.close()
                print("Database connection closed.")

# Fungsi untuk melakukan SELECT dan menampilkan kolom name dan address saja
def select_name_and_address():
    db = connect_to_database()
    if db:
        try:
            mycursor = db.cursor()
            mycursor.execute("SELECT name, address FROM customers")
            myresult = mycursor.fetchall()
            
            print("Showing names and addresses from customers table:")
            for x in myresult:
                print(x)
            
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if db.is_connected():
                db.close()
                print("Database connection closed.")

# Fungsi untuk melakukan SELECT dan menampilkan hanya satu baris pertama
def select_one_customer():
    db = connect_to_database()
    if db:
        try:
            mycursor = db.cursor()
            mycursor.execute("SELECT * FROM customers")
            myresult = mycursor.fetchone()
            
            print("Showing the first customer:")
            print(myresult)
            
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            if db.is_connected():
                db.close()
                print("Database connection closed.")

# Main program
if __name__ == "__main__":
    select_all_from_customers()
    print()
    select_name_and_address()
    print()
    select_one_customer()
