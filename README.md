Data Pipeline Development

Company Name : CODTECH IT SOLUTIONS

Name : Geebu Pavani

ID : CT04DH2208

Domain : Data science

Duration : July 10th,2025 to August 10th,2025

Mentor : Neela Santhosh kumar

Project Description :

This repository contains the solution for Task 1: ETL Pipeline Development as part of the CodTech Internship. The objective of this task was to develop a fully functional ETL (Extract, Transform, Load) pipeline in Python to clean and preprocess a dataset containing details about Android games.

The dataset (android-games.csv) includes various columns like game title, category, total ratings, average rating, number of installs, growth over 30/60 days, price, and star ratings (1 to 5 stars). However, the raw dataset contains inconsistencies, non-numeric formats, and unstructured fields that need to be cleaned and transformed for further analysis or machine learning applications.

🔧 ETL Pipeline Workflow:
✅ 1. Extract:
The pipeline starts by importing the dataset using Pandas.

The CSV file is read into a DataFrame, and its structure is examined.

✅ 2. Transform:
Cleaning the 'installs' column: String formats like '1M', '500K', and '3B' are converted into numerical values like 1000000, 500000, and 3000000000.

Dropping irrelevant columns: Columns like 'rank' and 'title' are removed since they are not useful for modeling or data analysis.

Separating features:

Numerical Features: Scaled using StandardScaler to standardize values.

Categorical Features: Encoded using OneHotEncoder to convert categories into binary vectors.

A ColumnTransformer is used to apply the above transformations in a pipeline format for modularity and clarity.

✅ 3. Load:
The cleaned and transformed data is saved as android_games_cleaned.csv.

The output is a numeric, well-structured dataset suitable for analysis, visualization, or training machine learning models.

📂 Files Included:
android-games (1).csv – Raw input dataset

task1_etl_pipeline_fixed.py – Python script for the ETL process

android_games_cleaned.csv – Final transformed output dataset

🧠 Key Concepts Practiced:
ETL pipeline creation with real-world data

Data cleaning and transformation using Pandas and scikit-learn

One-hot encoding for categorical variables

Feature scaling using standardization

Code modularity with pipelines and transformers

🛠 Tools & Libraries Used:
Python 3.12

Pandas

NumPy

Scikit-learn (StandardScaler, OneHotEncoder, Pipeline, ColumnTransformer)

Visual Studio Code

Git & GitHub

🚀 Outcome:
This task demonstrates the ability to build a scalable and reusable data pipeline for preprocessing real-world datasets. The resulting data is now ready for further use in analytics, reporting, or modeling pipelines. It shows proficiency in using modern Python libraries for efficient data manipulation and transformation.
