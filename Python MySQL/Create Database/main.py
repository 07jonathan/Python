import mysql.connector

# Function to create a database
def create_database():
    mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword"
    )
    mycursor = mydb.cursor()
    mycursor.execute("CREATE DATABASE mydatabase")
    print("Database created successfully")

# Function to list all databases
def list_databases():
    mydb = mysql.connector.connect(
        host="localhost",
        user="yourusername",
        password="yourpassword"
    )
    mycursor = mydb.cursor()
    mycursor.execute("SHOW DATABASES")
    for x in mycursor:
        print(x)

# Function to check if the database exists by connecting to it
def check_database_exists():
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="yourusername",
            password="yourpassword",
            database="mydatabase"
        )
        print("Database exists!")
    except mysql.connector.Error as err:
        print(f"Error: {err}")

# Create the database
create_database()

# List all databases
list_databases()

# Check if the database exists
check_database_exists()
