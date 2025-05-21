<<<<<<< HEAD

DAILY WEATHER ETL - COMMAND REFERENCE
--------------------------------------

1. Clone Repository & Setup

git clone https://github.com/<your-username>/daily-weather-etl.git
cd daily-weather-etl

mkdir -p dags dbt/models/{staging,marts} scripts config

touch dags/weather_dag.py \
      scripts/fetch_weather.py \
      scripts/load_to_snowflake.py \
      config/config.yaml \
      requirements.txt \
      .gitignore

2. Python Environment (Mac M1/M2)

brew install pyenv
pyenv install 3.10.13
pyenv local 3.10.13

python3 -m venv venv
source venv/bin/activate

3. Add Requirements

Contents of requirements.txt:

requests
pandas
pyyaml
snowflake-connector-python
dbt-core
apache-airflow==2.7.3
Flask-Session==0.4.0

Then install:
pip install -r requirements.txt

4. API Key Config

Create config/config.yaml with:

api_key: "YOUR_API_KEY"
=======
# 🌤️ Daily Weather ETL Pipeline

This project is an end-to-end data engineering pipeline that extracts weather data daily from the OpenWeatherMap API, loads it into Snowflake, transforms it using dbt, and orchestrates everything using Airflow. It's designed for hands-on learning and to demonstrate real-world data engineering skills.

---

## 📁 Project Initialization

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/daily-weather-etl.git
cd daily-weather-etl
```

### 2. Create Folder Structure

```bash
mkdir -p dags dbt/models/{staging,marts} scripts config
touch dags/weather_dag.py scripts/fetch_weather.py config/config.yaml requirements.txt .gitignore
```

This creates:

* `dags/` – Airflow DAGs
* `scripts/` – Python script for API extraction
* `dbt/models/` – dbt transformations (staging + marts)
* `config/` – API key and city list
* `requirements.txt` – Python dependencies
* `.gitignore` – for ignoring venv, .env files, etc.

---

## 🐍 Python Environment Setup (Mac M1/M2 Compatible)

### 3. Install `pyenv` and Python 3.10

```bash
brew install pyenv
pyenv install 3.10.13
pyenv local 3.10.13
```

### 4. Create and Activate Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

You should now see `(venv)` in your terminal. You're ready to install packages!

---

## 📦 Install Python Dependencies

Add the following to your `requirements.txt` file:

```txt
requests
pandas
snowflake-connector-python
dbt-core
apache-airflow==2.7.3
```

> 🗓️ Note:
>
> * `apache-airflow==2.7.3` is tested and compatible with Python 3.10 and M2 Mac.
> * You may later add `apache-airflow-providers-snowflake` when integrating Airflow with Snowflake.

### 🚀 Install the Dependencies

```bash
pip install -r requirements.txt
```

This will install all necessary libraries into your virtual environment.

---

## 🔢 Step 6: Extract Weather Data using Python

We'll create a Python script that:

* Reads city names and API key from `config/config.yaml`
* Calls the OpenWeatherMap API
* Extracts relevant fields (e.g., city, temperature, humidity, weather description)
* Saves data as a Pandas DataFrame or JSON (for loading to Snowflake later)

### Example: `scripts/fetch_weather.py`

```python
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
weather_df.to_csv("weather_output.csv", index=False)
```

### Example: `config/config.yaml`

```yaml
api_key: "YOUR_OPENWEATHER_API_KEY"
>>>>>>> a798d51 (Update DAGs and supporting files)
cities:
  - Mumbai
  - Delhi
  - Bengaluru
  - Pune
  - Nagpur
<<<<<<< HEAD

5. Update Script Paths

In fetch_weather.py:

with open("/Users/yourname/Desktop/daily-weather-etl/config/config.yaml", "r") as f:
    config = yaml.safe_load(f)

weather_df.to_csv("/Users/yourname/Desktop/daily-weather-etl/weather_output.csv", index=False)

In load_to_snowflake.py:

df = pd.read_csv("/Users/yourname/Desktop/daily-weather-etl/weather_output.csv")

6. Snowflake Setup

CREATE WAREHOUSE IF NOT EXISTS COMPUTE_WH;
CREATE DATABASE IF NOT EXISTS WEATHER_DB;
CREATE SCHEMA IF NOT EXISTS WEATHER_SCHEMA;

Switch to SYSADMIN and grant access:

GRANT USAGE ON WAREHOUSE COMPUTE_WH TO ROLE SYSADMIN;

7. Export Snowflake Env Vars

export SNOWFLAKE_USER="your_username"
export SNOWFLAKE_PASSWORD="your_password"
export SNOWFLAKE_ACCOUNT="your_account_id"
export SNOWFLAKE_WAREHOUSE="COMPUTE_WH"
export SNOWFLAKE_DATABASE="WEATHER_DB"
export SNOWFLAKE_SCHEMA="WEATHER_SCHEMA"

Run:

python scripts/load_to_snowflake.py

8. dbt Project

cd dbt
dbt init weather_dbt

Edit ~/.dbt/profiles.yml

cd weather_dbt
dbt run

9. Airflow Setup

airflow db migrate

# Terminal 1
airflow scheduler

# Terminal 2
airflow webserver --port 8080

Open http://localhost:8080

Username: admin
Password: admin

10. DAG Script Notes

Use absolute paths in subprocess calls.

Use which python and which dbt to confirm paths.

11. Final Check

- Trigger DAG
- All tasks green
- Check Snowflake data
=======
```

> Replace `YOUR_OPENWEATHER_API_KEY` with your actual API key.
>
> #### How to generate your API key:
>
> 1. Visit [OpenWeatherMap](https://openweathermap.org/api)
> 2. Sign up or log in
> 3. Go to your account > "My API Keys"
> 4. Click "Create" to generate a new key
> 5. Copy and paste it into your `config.yaml` file wrapped in quotes

---


>>>>>>> a798d51 (Update DAGs and supporting files)
