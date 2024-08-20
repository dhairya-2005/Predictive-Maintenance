import numpy as np
import pandas as pd
import random
import datetime as dt


# Simulating time series data for elevator operations
def simulate_elevator_data(num_records):
    data = []
    current_time = dt.datetime.now()

    for i in range(num_records):
        record = {}
        record['timestamp'] = current_time
        record['floor'] = random.randint(1, 10)  # Random floor between 1 and 10
        record['door_time'] = np.random.normal(5, 1)  # Door open/close time (normal operation)
        record['vibration'] = np.random.normal(0.1, 0.01)  # Normal vibration level
        record['motor_temp'] = np.random.normal(60, 5)  # Motor temperature in Celsius
        record['power'] = np.random.normal(50, 10)  # Power usage in kW

        # Simulate fault with 5% probability
        if random.random() < 0.05:
            record['fault'] = True
            record['vibration'] += np.random.normal(1, 0.5)  # Increased vibration during fault
            record['motor_temp'] += np.random.normal(20, 5)  # Increased temperature during fault
        else:
            record['fault'] = False

        data.append(record)
        current_time += dt.timedelta(seconds=random.randint(10, 60))  # Next record time

    return pd.DataFrame(data)


# Generating 1000 records of synthetic elevator data
elevator_data = simulate_elevator_data(1000)

with pd.ExcelWriter('output.xlsx') as writer:
    elevator_data.to_excel(writer, sheet_name='Sheet1', index=False)

