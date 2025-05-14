import pandas as pd

# Load the weather data from the CSV file
weather_df = pd.read_csv('weather_data.csv')

# Convert timestamp to datetime format for better handling
weather_df['timestamp'] = pd.to_datetime(weather_df['timestamp'])

# Handle missing values (if any)
weather_df = weather_df.dropna()

# Save cleaned data
weather_df.to_csv('cleaned_weather_data.csv', index=False)
print("✅ Cleaned data saved as 'cleaned_weather_data.csv'")
