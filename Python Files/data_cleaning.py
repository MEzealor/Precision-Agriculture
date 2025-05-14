import pandas as pd

# Load the data
data = pd.read_csv('weather_data.csv', delimiter='\t')

# Check and convert date format if needed (ensure it's in datetime format)
data['Date'] = pd.to_datetime(data['Date'], errors='coerce')

# Remove rows with invalid or missing date
data = data.dropna(subset=['Date'])

# Remove any duplicate rows
data = data.drop_duplicates()

# Reset index after cleaning
data = data.reset_index(drop=True)

# Save the cleaned data to a new file
data.to_csv('cleaned_weather_data.csv', index=False)

# Preview the cleaned data
print(data.head())
