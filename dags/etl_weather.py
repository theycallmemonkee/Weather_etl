from airflow import DAG
from airflow.decorators import task
from datetime import datetime
import requests
import pandas as pd

from airflow.providers.http.hooks.http import HttpHook
from airflow.providers.postgres.hooks.postgres import PostgresHook

LATITUDE = "20.5937"
LONGITUDE = "78.9629"

POSTGRES_CONN_ID = "postgres_default"
API_CONN_ID = "open_meteo_api"
with DAG(
    dag_id="weather_etl_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule='@daily',  
    catchup=False
) as dag:

    # ---------------- EXTRACT ----------------
    @task()
    def extract_weather_data():
        http_hook = HttpHook(http_conn_id=API_CONN_ID, method='GET')

        endpoint = f'/v1/forecast?latitude={LATITUDE}&longitude={LONGITUDE}&current_weather=true'

        response = http_hook.run(endpoint)

        if response.status_code == 200:
            return response.json()
        else:
            raise Exception(f"Failed to fetch: {response.status_code}")

    # ---------------- TRANSFORM ----------------
    @task()
    def transform_weather_data(weather_data):
        current_weather = weather_data['current_weather']

        return {
            'latitude': float(LATITUDE),
            'longitude': float(LONGITUDE),
            'temperature': current_weather['temperature'],
            'windspeed': current_weather['windspeed'],
            'winddirection': current_weather['winddirection'],
            'weathercode': current_weather['weathercode']
        }

    # ---------------- LOAD ----------------
    @task()
    def load_weather_data(transformed_data):
        pg_hook = PostgresHook(postgres_conn_id=POSTGRES_CONN_ID)

        conn = pg_hook.get_conn()
        cursor = conn.cursor()

        cursor.execute("""
        CREATE TABLE IF NOT EXISTS weather_data (
            latitude FLOAT,
            longitude FLOAT,
            temperature FLOAT,
            windspeed FLOAT,
            winddirection FLOAT,
            weathercode INT,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

        cursor.execute("""
        INSERT INTO weather_data (latitude, longitude, temperature, windspeed, winddirection, weathercode)
        VALUES (%s, %s, %s, %s, %s, %s)
        """, (
            transformed_data['latitude'],
            transformed_data['longitude'],
            transformed_data['temperature'],
            transformed_data['windspeed'],
            transformed_data['winddirection'],
            transformed_data['weathercode']
        ))

        conn.commit()
        cursor.close()

    # ---------------- PIPELINE ----------------
    weather_data = extract_weather_data()
    transformed_data = transform_weather_data(weather_data)
    load_weather_data(transformed_data)