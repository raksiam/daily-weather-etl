# 🌤️ Daily Weather ETL Pipeline

An end-to-end data engineering pipeline that:
- Extracts weather data from OpenWeatherMap API
- Loads it into Snowflake
- Transforms it using dbt
- Orchestrates using Airflow

---

## 📁 Project Setup

```bash
git clone https://github.com/raksiam/daily-weather-etl.git
cd daily-weather-etl
```

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

---

## 🔑 Configuration

- Set OpenWeatherMap API Key in `config/config.yaml`
- Export Snowflake credentials as environment variables

---

## 🧪 Scripts

- `fetch_weather.py`: Extracts & saves weather data
- `load_to_snowflake.py`: Loads data into Snowflake

---

## 🧊 Snowflake Setup

```sql
CREATE WAREHOUSE IF NOT EXISTS COMPUTE_WH;
CREATE DATABASE IF NOT EXISTS WEATHER_DB;
CREATE SCHEMA IF NOT EXISTS WEATHER_SCHEMA;
```

---

## 🛠️ dbt Setup

```bash
cd dbt
dbt init weather_dbt
dbt run
```

---

## ☁️ Airflow

```bash
airflow db migrate
airflow scheduler
airflow webserver --port 8080
```

DAG: `weather_dag.py`

---

## ✅ Result

- Weather data loaded daily
- Transformations handled via dbt
- Automated with Airflow