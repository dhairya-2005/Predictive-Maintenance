import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set parameters for synthetic data generation
num_samples = 100000
start_time = datetime.now() - timedelta(days=1000)  # Start 1000 days ago
time_interval = timedelta(minutes=1)  # 1-minute interval

# Generate timestamps
timestamps = [start_time + i * time_interval for i in range(num_samples)]

# Generate synthetic sensor data
np.random.seed(42)  # For reproducibility
temperature = np.random.normal(45, 5, num_samples)  # Mean=45°C, Std=5°C
rpm = np.random.normal(1500, 200, num_samples)      # Mean=1500 RPM, Std=200 RPM
pressure = np.random.normal(1.2, 0.2, num_samples)  # Mean=1.2 Bar, Std=0.2 Bar

# Create a DataFrame
synthetic_data = pd.DataFrame({
    "timestamp": timestamps,
    "temperature": temperature,
    "rpm": rpm,
    "pressure": pressure
})

# Save to CSV
file_path = "./synthetic_sensor_data.csv"
synthetic_data.to_csv(file_path, index=False)