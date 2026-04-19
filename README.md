# 🌦️ Weather ETL Pipeline using Apache Airflow

This project implements an end-to-end ETL (Extract, Transform, Load) pipeline using Apache Airflow.  
It fetches real-time weather data from the Open-Meteo API, processes it, and stores it in a PostgreSQL database.

---

## 🚀 Features

- Automated ETL pipeline using Apache Airflow  
- Real-time weather data extraction via REST API (Open-Meteo)  
- Data transformation using Python  
- Data loading into PostgreSQL  
- Fully containerized using Docker  
- Airflow UI for monitoring and scheduling  

---

## 🏗️ Tech Stack

- Apache Airflow  
- Python  
- PostgreSQL  
- Docker  
- Open-Meteo API  

---

## 📂 Project Structure

Weather_etl/
│── dags/
│   └── etl_weather.py
│── docker-compose.yml
│── requirements.txt
│── README.md

---

## ⚙️ Setup Instructions

### 1. Clone the repository

git clone https://github.com/YOUR_USERNAME/Weather_etl.git  
cd Weather_etl  

---

### 2. Start services using Docker

docker-compose up --build  

---

### 3. Access Airflow UI

http://localhost:8080  

Login:  
Username: admin  
Password: admin  

---

## 🔌 Airflow Connections Setup

### HTTP Connection (API)

Conn Id: open_meteo_api  
Conn Type: HTTP  
Host: https://api.open-meteo.com  

---

### Postgres Connection

Conn Id: postgres_default  
Host: postgres  
User: airflow  
Password: airflow  
Database: airflow  
Port: 5432  

---

## 🔄 Pipeline Workflow

1. Extract  
   Fetches weather data from Open-Meteo API  

2. Transform  
   Processes and structures the data  

3. Load  
   Stores processed data into PostgreSQL  

---

## ▶️ Running the DAG

- Open Airflow UI  
- Enable weather_etl_pipeline  
- Click "Trigger DAG"  

---

## 📊 Output

A table named weather_data is created in PostgreSQL containing:

- Latitude  
- Longitude  
- Temperature  
- Wind Speed  
- Wind Direction  
- Weather Code  
- Timestamp  

---

## 🧠 Use Case

This project demonstrates a real-world data engineering workflow including:

- API integration  
- Data transformation  
- Workflow orchestration  
- Database loading  

---

## 📌 Future Improvements

- Add retry mechanisms and error handling  
- Integrate cloud storage (AWS S3)  
- Implement data validation  
- Use advanced scheduling and monitoring  

---

## 👨‍💻 Author

Yogesh Mehta
