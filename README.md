
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
cities:
  - Mumbai
  - Delhi
  - Bengaluru
  - Pune
  - Nagpur

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
