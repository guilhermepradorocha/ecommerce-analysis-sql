# Brazilian E-Commerce Data Analysis with SQL, Python, and dbt

![Status](https://img.shields.io/badge/Status-Work_In_Progress-yellow)

## 1. Introduction

This project aims to perform an in-depth analysis of the Brazilian E-commerce Public Dataset by Olist. The primary goal is to build a modern, scalable data pipeline to transform raw, multi-table data into a clean, well-structured analytical database. 

From this transformed data, the project will extract actionable business insights related to customer behavior, product performance, sales trends, and logistics efficiency.

## 2. Tech Stack

* **Data Storage/Engine:** SQLite
* **Data Ingestion (EL):** Python (`pandas`, `SQLAlchemy`)
* **Data Transformation (T):** dbt (Data Build Tool)
* **IDE & Version Control:** VS Code, Git, & GitHub
* **Future Analysis & Visualization:** Python (`Jupyter`, `pandas`, `matplotlib`, `seaborn`)

## 3. Project Goals & Key Questions

The main objective is to build a robust and automated ELT pipeline. This pipeline will support analytics to answer key business questions, such as:

* What are the top-selling product categories?
* What is the geographic distribution of customers across Brazil?
* How does seasonality affect sales volume throughout the year?
* What is the average order value?
* What are the average shipping times and are there regional differences?

## 4. Data Source

This project uses the [Brazilian E-commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) available on Kaggle. It contains real, anonymized data from over 100,000 orders between 2016 and 2018.

## 5. Repository Structure

* `├── data/`: Contains the raw `.csv` files from the Kaggle dataset.
* `├── scripts/`: Holds the Python script for the initial data ingestion into SQLite.
* `├── dbt_project/`: The core dbt project for all data transformation models.
* `└── README.md`: This project overview and documentation.

## 6. Current Status

* [x] Project repository and local environment setup.
* [ ] **Next Step:** Develop the Python script for initial data ingestion (EL part).