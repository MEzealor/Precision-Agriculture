import pandas as pd
import matplotlib.pyplot as plt

# Load the weather data from the CSV file
weather_df = pd.read_csv('weather_data.csv')

# Convert timestamp to datetime format for better handling in plots
weather_df['timestamp'] = pd.to_datetime(weather_df['timestamp'])

# Plot Temperature over Time
plt.figure(figsize=(10, 6))
plt.plot(weather_df['timestamp'], weather_df['temperature_c'], label='Temperature (°C)', color='tab:red')
plt.xlabel('Timestamp')
plt.ylabel('Temperature (°C)')
plt.title('Temperature Over Time')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()

# Plot Humidity over Time
plt.figure(figsize=(10, 6))
plt.plot(weather_df['timestamp'], weather_df['humidity'], label='Humidity (%)', color='tab:blue')
plt.xlabel('Timestamp')
plt.ylabel('Humidity (%)')
plt.title('Humidity Over Time')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()

# Plot Wind Speed over Time
plt.figure(figsize=(10, 6))
plt.plot(weather_df['timestamp'], weather_df['wind_speed'], label='Wind Speed (m/s)', color='tab:green')
plt.xlabel('Timestamp')
plt.ylabel('Wind Speed (m/s)')
plt.title('Wind Speed Over Time')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()

# Plot Soil Moisture over Time
plt.figure(figsize=(10, 6))
plt.plot(weather_df['timestamp'], weather_df['soil_moisture'], label='Soil Moisture (%)', color='tab:orange')
plt.xlabel('Timestamp')
plt.ylabel('Soil Moisture (%)')
plt.title('Soil Moisture Over Time')
plt.xticks(rotation=45)
plt.grid(True)
plt.legend()
plt.tight_layout()

# Show all the plots
plt.show()
