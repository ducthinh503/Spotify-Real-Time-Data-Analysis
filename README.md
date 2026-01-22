# 🎧 Spotify Modern Data Stack Project

---

## 📌 Project Overview

This project demonstrates an **end-to-end real-time data engineering pipeline** for **Spotify music analytics** using the **Modern Data Stack (MDS)**.  
We simulate streaming music data — including **song plays, listeners, regions, and device types** — and build a fully automated pipeline from **data ingestion to visualization**.

Once the pipeline starts, **every component runs automatically**:  
data simulation → streaming via Kafka → storage in Snowflake → transformation with DBT → visualization in Power BI.

👉 Think of it as a **real-world Spotify analytics system** built on top of cutting-edge data tools.

---

## 🏗️ System Architecture

![System Architecture](docs/data_architecture.png)

**Pipeline Flow:**
1. **Data Simulator** → Generates fake Spotify streaming data (user, track, region, device).  
2. **Kafka Producer** → Streams the data to Kafka topics in real time.  
3. **Kafka Consumer** → Consumes and stores the raw data into **MinIO (S3-compatible storage)**.  
4. **Airflow** → Orchestrates data loading from MinIO → Snowflake (Bronze).  
5. **Snowflake** → Stores and manages data in **Bronze → Silver → Gold layers**.  
6. **DBT** → Cleans, transforms, and builds analytics-ready models directly inside Snowflake.  
7. **Power BI** → Connects to the Snowflake Gold tables for **interactive dashboards and insights**.  

---

## ⚡ Tech Stack

- **Python (Faker)** → Data simulation  
- **Apache Kafka** → Real-time data streaming  
- **MinIO** → Object storage (S3-compatible)  
- **Snowflake** → Cloud data warehouse  
- **DBT** → Transformations, tests, and models  
- **Apache Airflow** → Orchestration and DAG scheduling  
- **Power BI** → Business intelligence dashboard  
- **Docker & docker-compose** → Containerized environment  

---

## ✅ Key Features

- **Fully automated pipeline** — end-to-end from ingestion to insights  
- **Real-time streaming** using Kafka  
- **Medallion Architecture (Bronze → Silver → Gold)** implemented in Snowflake  
- **DBT for transformation and testing** (clean, modular SQL models)  
- **Power BI dashboard** showing region-wise plays, song trends, and listener insights  
- **Containerized deployment** for reproducibility  
- **CI/CD pipeline** with dbt test automation  

---

## 📊 Dashboard Overview

![Dashboard](docs/dashboard_final.png)

---

## 📊 Final Deliverables
- Real-time **Spotify data streaming pipeline**  
- Clean **Snowflake Medallion Architecture (Bronze → Silver → Gold)**  
- **DBT transformation project** (staging, marts, gold)  
- **Automated orchestration** via Airflow  
- **Interactive Power BI dashboard**  

---

## 🧠 Concepts Covered
- Real-time data ingestion (**Kafka**)  
- **Medallion architecture** (Bronze → Silver → Gold)  
- **Data modeling with DBT**  
- **Data warehousing in Snowflake**  
- **Workflow orchestration with Airflow**  
- **Visualization with Power BI**  

---
