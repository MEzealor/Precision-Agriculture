import requests
import pandas as pd
import os
from datetime import datetime

# === GET WEATHER DATA ===
def get_weather_data(api_key, latitude, longitude):
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'
    response = requests.get(url)
    return response.json()

# === GET SOIL MOISTURE DATA (Placeholder) ===
def get_soil_moisture_data():
    return 50  # Replace with real sensor/API value later

# === CONFIG: Wamba, Nigeria ===
api_key = '26b7e670dabfee41b920d721c33d03c0'
latitude = 9.0820
longitude = 8.6753

# === FETCH WEATHER DATA ===
weather_data = get_weather_data(api_key, latitude, longitude)

if weather_data:
    print("✅ Weather data retrieved successfully.")

    # === STANDARDIZED WEATHER STRUCTURE ===
    weather_info = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # ISO format
        "temperature_c": round(weather_data['main']['temp'] - 273.15, 2),
        "humidity": weather_data['main']['humidity'],
        "wind_speed": weather_data['wind']['speed'],
        "weather_description": weather_data['weather'][0]['description'],
        "pressure": weather_data['main']['pressure'],
        "soil_moisture": get_soil_moisture_data()
    }

    # === SAVE TO CSV ===
    weather_df = pd.DataFrame([weather_info])
    print("📋 Weather Data:")
    print(weather_df)

    filename = 'weather_data.csv'
    file_exists = os.path.isfile(filename)
    weather_df.to_csv(filename, mode='a', index=False, header=not file_exists)
    print(f"✅ Weather data appended to '{filename}'")

else:
    print("❌ Failed to retrieve weather data.")
