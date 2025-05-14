# Precision Agriculture System
This project is a data-driven Precision Agriculture system designed to support sustainable farming practices in Nigeria. It leverages IoT sensors, remote sensing, and AI models to monitor soil health, optimize water usage, and predict crop yield — empowering farmers with real-time, actionable insights.

## 🌱 Problem Statement
Many farmers face challenges like poor land management, water scarcity, soil degradation, and low crop yields due to lack of data-driven decision tools. This project aims to solve that by building an intelligent system that ensures resources are used efficiently and farming practices are sustainable.

## 🌍 Location Focus
Wamba, Nigeria — chosen for its agricultural potential and relevance in local food systems.

## 📦 Tech Stack
- Python
- Pandas, Scikit-learn, Matplotlib
- FAO datasets
- Git & GitHub
- Task Scheduler (Windows)
- Jupyter Notebook / PyCharm

## Files
- **main.py**: Collects weather data from the OpenWeatherMap API and preprocesses it for analysis.
- **predict_yield.py**: Contains the code for evaluating the prediction model for crop yield.
- **save_model.py**: Saves the trained machine learning models for future use.
- **weather_data.py**: Fetches weather data from the OpenWeatherMap API.
- **analyze_weather.py**: Analyzes weather data and visualizes trends such as temperature, humidity, and wind speed over time.
- **clean_weather_data.py**: Cleans and preprocesses the raw weather data for further analysis.
- **data_processing.py**: Processes the weather data to extract features like the time of day, day, month, etc.
- **data_cleaning.py**: Cleans and prepares weather data by removing duplicates and handling missing values.

## Data Collection
Data is collected from:
- Weather stations (temperature, humidity, wind speed, pressure, etc.)
- Soil moisture sensors

## Data
The data used in this project includes weather data collected from Wamba, Nigeria. The data consists of:
- Temperature (°C)
- Humidity (%)
- Wind speed (m/s)
- Soil moisture (%)
- Pressure (hPa)

## 💡 Features
- Real-time monitoring of soil moisture, temperature, and weather.
- Predictive crop yield model using historical weather and soil data.
- Task scheduling for continuous data collection.
- Scalable and customizable for different locations.

The data is stored in CSV files, with a raw version (`weather_data.csv`) and a cleaned version (`cleaned_weather_data.csv`).

## Research Findings
- **Temperature**: The temperature has a significant impact on crop yield, affecting water evaporation and plant health.
- **Humidity**: High humidity can lead to fungal diseases, influencing the crop yield negatively.
- **Soil Moisture**: Soil moisture is directly related to irrigation needs, and managing this efficiently can reduce water waste.

## Findings
1. **Weather Trends**:
   - Temperature, humidity, wind speed, and cloud cover were observed to fluctuate over time.
   - Correlation analysis showed that certain weather factors, such as temperature and humidity, had strong correlations with crop yield potential.

2. **Machine Learning Model**:
   - A Random Forest Regressor model was trained to predict crop yield based on weather and soil data.
   - Model evaluation showed promising results, with an R² score indicating that the model can predict crop yield with reasonable accuracy.

## Conclusion
The precision agriculture system demonstrates the potential for using weather and soil data to predict crop yield. By leveraging machine learning models, farmers can make data-driven decisions to optimize crop production, improve land management, and ensure sustainable farming practices. 
This project can help farmers make data-driven decisions, optimizing irrigation, monitoring weather patterns, and improving soil health. It aims to increase crop yield while promoting sustainable farming practices.

### Benefits of the Project
- **Improved Yield Prediction**: The system predicts crop yield, allowing farmers to optimize resource usage and plan accordingly.
- **Data-Driven Decisions**: The model helps farmers make decisions based on actual weather and soil conditions rather than guesswork.
- **Sustainability**: Efficient use of resources, such as water and fertilizers, is encouraged, contributing to environmental sustainability.
- **Efficient Resource Use**: By using IoT sensors, farmers can better manage water and soil health.
- **Sustainability**: The project helps reduce water waste and soil degradation, which are critical for long-term farming success.
- **Data-Driven Decisions**: The model provides farmers with actionable insights, improving yield prediction and planning.

## 🚀 How to Run
1. Clone the repository.
2. Run `main.py` to start data processing or analysis.
3. Use the `weather.py` script for scheduled weather data collection.
4. Train or test ML models in `crop_yield_model.ipynb`.

## 📁 Directory Structure

