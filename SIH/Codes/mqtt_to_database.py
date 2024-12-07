import paho.mqtt.client as mqtt
import sqlite3
import json

# SQLite database setup
def insert_data_to_db(timestamp, temperature, rpm, pressure):
    conn = sqlite3.connect('sensor_data.db')
    cursor = conn.cursor()

    # Insert the received data into the database
    cursor.execute('''
    INSERT INTO sensor_data (timestamp, temperature, rpm, pressure)
    VALUES (?, ?, ?, ?)''', (timestamp, temperature, rpm, pressure))

    # Commit and close
    conn.commit()
    conn.close()

# MQTT Setup
MQTT_BROKER = "mqtt.eclipse.org"  # Replace with your MQTT broker's address
MQTT_PORT = 1883
MQTT_TOPIC = "esp32/sensors"

# Callback function when a message is received
def on_message(client, userdata, message):
    try:
        # Assuming the message payload is in JSON format
        data = json.loads(message.payload.decode("utf-8"))
        timestamp = data['timestamp']
        temperature = data['temperature']
        rpm = data['rpm']
        pressure = data['pressure']
        
        # Insert the data into the SQLite database
        insert_data_to_db(timestamp, temperature, rpm, pressure)
        print(f"Data received and stored: {data}")
    except Exception as e:
        print(f"Error processing message: {e}")

# Set up the MQTT client
client = mqtt.Client()

# Attach the message callback
client.on_message = on_message

# Connect to the MQTT broker
client.connect(MQTT_BROKER, MQTT_PORT, 60)

# Subscribe to the relevant topic
client.subscribe(MQTT_TOPIC)

# Start the MQTT client loop to continuously receive messages
client.loop_forever()
