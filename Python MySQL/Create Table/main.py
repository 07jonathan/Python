import mysql.connector

def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword",
        database="mydatabase"
    )

def create_table(mydb):
    mycursor = mydb.cursor()
    mycursor.execute("""
    CREATE TABLE IF NOT EXISTS customers (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        address VARCHAR(255)
    )
    """)
    print("Table 'customers' created or already exists.")
    mycursor.close()

def check_table_exists(mydb):
    mycursor = mydb.cursor()
    mycursor.execute("SHOW TABLES LIKE 'customers'")
    result = mycursor.fetchone()
    if result:
        print("Table 'customers' exists.")
    else:
        print("Table 'customers' does not exist.")
    mycursor.close()

def add_primary_key(mydb):
    mycursor = mydb.cursor()
    try:
        mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
        print("Primary key added to the 'customers' table.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    mycursor.close()

def main():
    mydb = create_connection()
    
    # Step 1: Create the table
    create_table(mydb)
    
    # Step 2: Check if the table exists
    check_table_exists(mydb)
    
    # Step 3: Add primary key if not already present
    add_primary_key(mydb)
    
    # Closing the connection
    mydb.close()

if __name__ == "__main__":
    main()
