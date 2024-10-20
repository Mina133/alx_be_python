import mysql.connector

# Database connection details (replace with your own)
hostname = "localhost"
username = "root"
password = "Mina1332002!"

try:
  
  # Connect to the MySQL server
  conn = mysql.connector.connect(host=hostname, user=username, password=password
  )

  # Create a cursor object
  cursor = conn.cursor()

  # Create the database (ignore if it already exists)
  sql = "CREATE DATABASE IF NOT EXISTS alx_book_store"
  cursor.execute(sql)

  # Commit the changes
  conn.commit()

  print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
  print(f"Error creating database: {err}")

finally:
  if conn.is_connected():
        conn.close()
        print("Database connection closed.")