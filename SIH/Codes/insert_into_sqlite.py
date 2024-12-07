import sqlite3
import pandas as pd

# Load the synthetic data (adjust file path if needed)
synthetic_data = pd.read_csv("synthetic_sensor_data.csv")

# Establish connection to SQLite (this will create the database file if it doesn't exist)
connection = sqlite3.connect("predictive_maintenance.db")  # Replace with your SQLite database file name

cursor = connection.cursor()

# Create the table if it doesn't exist already
create_table_query = """
CREATE TABLE IF NOT EXISTS sensor_data (
    timestamp TEXT,
    temperature REAL,
    rpm REAL,
    pressure REAL
)
"""
cursor.execute(create_table_query)

# Insert synthetic data into the SQLite table
insert_query = """
INSERT INTO sensor_data (timestamp, temperature, rpm, pressure)
VALUES (?, ?, ?, ?)
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
