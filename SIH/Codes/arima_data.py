import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# Set parameters for synthetic data generation
num_samples = 30000  # Number of samples for 3 months of data
start_time = datetime(2024, 11, 1)  # Start from the beginning of 2024
start_time = start_time - timedelta(days=90)  # Subtract 3 months (approx 90 days)
time_interval = timedelta(minutes=5)  # 5-minute interval

# Generate timestamps for the past 3 months
timestamps = [start_time + i * time_interval for i in range(num_samples)]

# Generate synthetic sensor data
np.random.seed(42)  # For reproducibility
temperature = np.random.normal(45, 5, num_samples)  # Mean=45°C, Std=5°C
rpm = np.random.normal(1500, 200, num_samples)      # Mean=1500 RPM, Std=200 RPM
pressure = np.random.normal(1.2, 0.2, num_samples)  # Mean=1.2 Bar, Std=0.2 Bar

# Lifespan distribution for ventilation fan (in minutes)
initial_lifespan = 3 * 365 * 24 * 60  # 3 years in minutes

# Initialize the RUL with the initial lifespan
rul = np.full(num_samples, initial_lifespan)

# RPM, Temperature, Pressure threshold values for normal range
normal_rpm_range = (1300, 1700)
normal_temp_range = (40, 50)  # Normal temperature range in °C
normal_pressure_range = (1.0, 1.4)  # Normal pressure range in bar

# Simulate RUL based on deviations of RPM, temperature, and pressure (Non-linear variation)
for i in range(1, num_samples):
    # Initialize a decay factor
    decay_factor = 0

    # Check RPM deviation and apply exponential decay for larger deviations
    if rpm[i] < normal_rpm_range[0] or rpm[i] > normal_rpm_range[1]:
        rpm_deviation = np.abs(rpm[i] - np.mean(normal_rpm_range)) / np.mean(normal_rpm_range)
        decay_factor += np.exp(rpm_deviation * 2) * np.random.randint(5, 20)  # Exponential decay

    # Check temperature deviation and apply quadratic decay
    if temperature[i] < normal_temp_range[0] or temperature[i] > normal_temp_range[1]:
        temp_deviation = np.abs(temperature[i] - np.mean(normal_temp_range)) / np.mean(normal_temp_range)
        decay_factor += temp_deviation**2 * np.random.randint(10, 30)  # Quadratic decay

    # Check pressure deviation and apply exponential decay for larger deviations
    if pressure[i] < normal_pressure_range[0] or pressure[i] > normal_pressure_range[1]:
        pressure_deviation = np.abs(pressure[i] - np.mean(normal_pressure_range)) / np.mean(normal_pressure_range)
        decay_factor += np.exp(pressure_deviation * 2) * np.random.randint(5, 30)  # Exponential decay

    # Apply the decay factor to the RUL
    rul[i] = rul[i-1] - decay_factor
    rul[i] = max(rul[i], 0)  # Ensure RUL doesn't go below zero

# Create a DataFrame
synthetic_data = pd.DataFrame({
    "timestamp": timestamps,
    "temperature": temperature,
    "rpm": rpm,
    "pressure": pressure,
    "rul": rul
})

# Save to CSV
file_path = "../Datasets/arima_data.csv"
synthetic_data.to_csv(file_path, index=False)

print(f"Data saved to {file_path}")

# Plotting RUL variation over time
plt.figure(figsize=(12, 6))
plt.plot(synthetic_data["timestamp"], synthetic_data["rul"], label="RUL", color="b")
plt.title("Variation of Remaining Useful Life (RUL) over Time (Non-linear Decay)")
plt.xlabel("Timestamp")
plt.ylabel("Remaining Useful Life (minutes)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid(True)
plt.legend()
plt.show()
