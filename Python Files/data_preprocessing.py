import pandas as pd

# Load your weather data CSV (Replace 'weather_data.csv' with your actual file name)
df = pd.read_csv('weather_data.csv')

# Check for missing values in the dataset
print(df.isnull().sum())

# Fill missing values (forward fill in this case)
df.fillna(method='ffill', inplace=True)

# If you want to drop rows with missing values, you can use:
# df.dropna(inplace=True)

# Convert timestamp column to datetime format (assuming your timestamp column is called 'timestamp')
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Optionally, you can extract additional time-related features like hour, day, month, year
df['hour'] = df['timestamp'].dt.hour
df['day'] = df['timestamp'].dt.day
df['month'] = df['timestamp'].dt.month
df['year'] = df['timestamp'].dt.year

# Check the first few rows to confirm the data is processed correctly
print(df.head())
