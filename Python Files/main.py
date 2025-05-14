import requests
import pandas as pd
import os
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns
import joblib
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor  # Import Random Forest

# === WEATHER DATA COLLECTION ===

def get_weather_data(api_key, latitude, longitude):
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'
    response = requests.get(url)
    return response.json()

# Wamba, Nigeria
api_key = '26b7e670dabfee41b920d721c33d03c0'
latitude = 9.0820
longitude = 8.6753

weather_data = get_weather_data(api_key, latitude, longitude)

if weather_data:
    print("Weather data retrieved successfully.")

    weather_info = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),  # ISO format
        "temperature_c": round(weather_data['main']['temp'] - 273.15, 2),
        "humidity": weather_data['main']['humidity'],
        "wind_speed": weather_data['wind']['speed'],
        "weather_description": weather_data['weather'][0]['description'],
        "pressure": weather_data['main']['pressure'],
        "cloud_cover": weather_data['clouds']['all']
    }

    weather_df = pd.DataFrame([weather_info])
    print("Weather Data:")
    print(weather_df)

    filename = 'weather_data.csv'
    file_exists = os.path.isfile(filename)
    weather_df.to_csv(filename, mode='a', index=False, header=not file_exists)
    print(f"Weather data appended to '{filename}'")

else:
    print("Failed to retrieve weather data.")

# === DATA PREPARATION ===
try:
    df = pd.read_csv('weather_data.csv')
    if df.columns[0] != "timestamp":
        df.columns = ["timestamp", "temperature_c", "humidity", "wind_speed", "weather_description", "pressure", "cloud_cover"]

    df.dropna(inplace=True)

    # Handle mixed timestamp formats
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='mixed', dayfirst=True, errors='coerce')
    df.dropna(subset=['timestamp'], inplace=True)

    df['hour'] = df['timestamp'].dt.hour
    df['day'] = df['timestamp'].dt.day
    df['month'] = df['timestamp'].dt.month

    df.to_csv('cleaned_weather_data.csv', index=False)
    print("\nCleaned data saved to 'cleaned_weather_data.csv'")
except Exception as e:
    print(f"Error during data preparation: {e}")

# === EDA ===
try:
    df = pd.read_csv('cleaned_weather_data.csv')
    df['timestamp'] = pd.to_datetime(df['timestamp'])

    plt.figure(figsize=(10, 6))
    plt.plot(df['timestamp'], df['temperature_c'], marker='o', label='Temperature (°C)')
    plt.plot(df['timestamp'], df['humidity'], marker='x', label='Humidity (%)')
    plt.plot(df['timestamp'], df['cloud_cover'], marker='s', label='Cloud Cover (%)')
    plt.xlabel('Timestamp')
    plt.ylabel('Value')
    plt.title('Weather Trends Over Time')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Correlation heatmap
    plt.figure(figsize=(8, 5))
    sns.heatmap(df[['temperature_c', 'humidity', 'wind_speed', 'pressure', 'cloud_cover']].corr(), annot=True, cmap='coolwarm')
    plt.title('Correlation Heatmap')
    plt.tight_layout()
    plt.show()

except Exception as e:
    print(f"Error during EDA: {e}")

# === MACHINE LEARNING (Prediction of Pressure) ===

try:
    # Load the cleaned weather data (the data used for predictions)
    cleaned_data = pd.read_csv('cleaned_weather_data.csv')

    # Features and target (Pressure as the target)
    features = ['temperature_c', 'humidity', 'wind_speed', 'cloud_cover']
    target = 'pressure'

    X = cleaned_data[features]
    y = cleaned_data[target]

    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Create and train the Random Forest Regressor model
    rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
    rf_model.fit(X_train, y_train)

    # Make predictions
    y_pred_rf = rf_model.predict(X_test)

    # Evaluate the model
    mse_rf = mean_squared_error(y_test, y_pred_rf)
    r2_rf = r2_score(y_test, y_pred_rf)

    print(f'Random Forest Model - Mean Squared Error: {mse_rf}')
    print(f'Random Forest Model - R² Score: {r2_rf}')

    # Visualize the results
    plt.figure(figsize=(10, 6))
    plt.scatter(y_test, y_pred_rf, color='blue')
    plt.xlabel('Actual Pressure')
    plt.ylabel('Predicted Pressure')
    plt.title('Random Forest - Actual vs Predicted Pressure')
    plt.show()

    # Save the trained model
    joblib.dump(rf_model, 'pressure_predictor_rf_model.pkl')

except Exception as e:
    print(f"Error during prediction and evaluation: {e}")
