import mysql.connector

# Replace 'your_username', 'your_password', and 'your_host' with your MySQL credentials
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'mysql',
}

# Connect to MySQL server
conn = mysql.connector.connect(**db_config)

# Create a cursor object to interact with the database
cursor = conn.cursor()

# Replace 'your_database' with the name you want for your database
database_name = 'crm_db'

# Create a new database
cursor.execute(f"CREATE DATABASE {database_name}")

print(f"Database '{database_name}' created successfully!")

# Close the cursor and connection
cursor.close()
conn.close()
