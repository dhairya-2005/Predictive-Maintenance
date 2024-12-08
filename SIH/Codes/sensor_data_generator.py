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

# Lifespan distribution for ventilation fan (in hours)
mean_lifespan = 3000  # Mean lifespan in hours
std_dev_lifespan = 500  # Std deviation of lifespan
lifespan_minutes = np.random.normal(mean_lifespan * 60, std_dev_lifespan * 60, num_samples)

# Generate RUL values
initial_lifespan = lifespan_minutes[0]  # Take the initial lifespan as the starting point
rul = np.clip(initial_lifespan - np.arange(num_samples), a_min=0, a_max=None)

# Create a DataFrame
synthetic_data = pd.DataFrame({
    "timestamp": timestamps,
    "temperature": temperature,
    "rpm": rpm,
    "pressure": pressure,
    "rul": rul
})

# Save to CSV
file_path = "../Datasets/synthetic_sensor_data_with_rul.csv"
synthetic_data.to_csv(file_path, index=False)

print(f"Data saved to {file_path}")
