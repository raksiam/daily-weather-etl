import requests
import pandas as pd
import yaml
import os
from datetime import datetime

# Load config
with open("config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

API_KEY = config["api_key"]
cities = config["cities"]

results = []

for city in cities:
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        results.append({
            "city": city,
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "weather": data["weather"][0]["description"],
            "timestamp": datetime.utcnow().isoformat()
        })
    else:
        print(f"Failed to fetch data for {city}: {response.status_code}")

# Convert to DataFrame
weather_df = pd.DataFrame(results)
print(weather_df)

# Optional: Save to CSV or JSON
weather_df.to_csv("/Users/<your_name>/Desktop/daily-weather-etl/weather_output.csv", index=False)