Explanation
- create_connection: Establishes a connection to the MySQL database using the provided credentials.
- create_table: Creates the customers table with a primary key if it doesn't already exist.
- check_table_exists: Checks if the customers table exists in the database.
- add_primary_key: Adds a primary key to the customers table. If the table already has a primary key, it will catch the error and print it.
- main: The main function that orchestrates the process by calling the other functions.
