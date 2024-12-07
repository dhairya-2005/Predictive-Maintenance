import mysql.connector
import pandas as pd

# Load the synthetic data (adjust file path if needed)
synthetic_data = pd.read_csv("synthetic_sensor_data.csv")

# Establish connection to MySQL
connection = mysql.connector.connect(
    host="localhost",        # Replace with your MySQL host
    user="root",             # Replace with your MySQL username
    password="#dhairya%05",     # Replace with your MySQL password
    database="predictive_maintenance"  # Replace with your database name
)

cursor = connection.cursor()

# Insert synthetic data into the MySQL table
insert_query = """
INSERT INTO sensor_data (timestamp, temperature, rpm, pressure)
VALUES (%s, %s, %s, %s)
"""

# Prepare a small sample of data to insert
sample_data = synthetic_data.head(10).values.tolist()

try:
    # Execute insert query in batches
    cursor.executemany(insert_query, sample_data)
    connection.commit()
    print("Data inserted successfully!")
except Exception as e:
    connection.rollback()
    print(f"An error occurred: {e}")
finally:
    cursor.close()
    connection.close()
