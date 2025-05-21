from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
from airflow.utils.dates import days_ago
import subprocess

# Replace with your actual file paths
FETCH_SCRIPT_PATH = "/Users/<your_name>/Desktop/daily-weather-etl/scripts/fetch_weather.py"
LOAD_SCRIPT_PATH = "/Users/<your_name>/Desktop/daily-weather-etl/scripts/load_to_snowflake.py"
DBT_PROJECT_PATH = "/Users/<your_name>/Desktop/daily-weather-etl/dbt/weather_dbt"

def run_fetch():
    subprocess.run(['/Users/<your_name>/Desktop/daily-weather-etl/venv/bin/python', FETCH_SCRIPT_PATH], check=True)

def run_dbt():
    subprocess.run([
        '/Users/<your_name>/Desktop/daily-weather-etl/venv/bin/dbt',
        'run',
        '--project-dir',
        DBT_PROJECT_PATH
    ], check=True)

default_args = {
    'owner': 'rakshanda',
    'start_date': days_ago(1),
    'retries': 1,
}

with DAG(
    dag_id='daily_weather_etl',
    default_args=default_args,
    description='Daily pipeline for weather ETL using Python, Snowflake, dbt, and Airflow',
    schedule_interval='@daily',
    catchup=False,
    tags=['weather', 'etl'],
) as dag:

    fetch_task = PythonOperator(
        task_id='fetch_weather',
        python_callable=run_fetch,
    )

    load_task = BashOperator(
        task_id='load_to_snowflake',
        bash_command=f"""
            export SNOWFLAKE_USER='raks254' && \
            export SNOWFLAKE_PASSWORD='Raks@123456789' && \
            export SNOWFLAKE_ACCOUNT='fkbvxmp-pq95496' && \
            export SNOWFLAKE_WAREHOUSE='COMPUTE_WH' && \
            export SNOWFLAKE_DATABASE='WEATHER_DB' && \
            export SNOWFLAKE_SCHEMA='WEATHER_SCHEMA' && \
            python {LOAD_SCRIPT_PATH}
        """
    )

    transform_task = PythonOperator(
        task_id='run_dbt_transformations',
        python_callable=run_dbt,
    )

    fetch_task >> load_task >> transform_task
