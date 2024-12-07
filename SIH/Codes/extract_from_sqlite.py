import sqlite3

# Establish connection to the SQLite database
connection = sqlite3.connect("predictive_maintenance.db")  # Replace with your SQLite database file name
cursor = connection.cursor()

# Function to view the data
def view_data():
    try:
        # Query to fetch all data from the sensor_data table
        select_query = "SELECT * FROM sensor_data"
        cursor.execute(select_query)

        # Fetch all rows from the result of the query
        rows = cursor.fetchall()

        # Print the data
        print("Data from sensor_data table:")
        for row in rows:
            print(row)  # Each row is a tuple (timestamp, temperature, rpm, pressure)

    except Exception as e:
        print(f"An error occurred: {e}")

# Function to extract specific data based on a condition (e.g., temperature > 50)
def extract_data():
    try:
        # Query to fetch data where temperature is greater than 50 (example condition)
        select_query = "SELECT * FROM sensor_data WHERE temperature > 50"
        cursor.execute(select_query)

        # Fetch all rows from the result of the query
        rows = cursor.fetchall()

        # Print the extracted data
        print("Extracted data (temperature > 50):")
        for row in rows:
            print(row)  # Each row is a tuple (timestamp, temperature, rpm, pressure)

    except Exception as e:
        print(f"An error occurred: {e}")

# Call the function to view the data
view_data()

# Call the function to extract and print data based on a condition
extract_data()

# Close the connection
cursor.close()
connection.close()
