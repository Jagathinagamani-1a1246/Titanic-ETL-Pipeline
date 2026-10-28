# 🚢 Titanic Dataset ETL Pipeline | Python + MySQL

## 📌 Project Overview

This project demonstrates a hands-on **ETL (Extract, Transform, Load) pipeline** using the Titanic passenger dataset. It was developed to practice data extraction, data cleaning, validation, and database integration using Python in VS Code and MySQL.

The project also includes batch processing and testing modules to make the workflow more organized and reliable.

## 🎯 Objectives

- Extract the Titanic dataset using Python.
- Clean and transform missing values.
- Convert categorical data into numerical values.
- Validate the cleaned dataset.
- Load processed data into a MySQL database.
- Practice modular programming and batch processing.

## 🛠️ Technologies Used

- Python
- Pandas
- Seaborn
- SQLAlchemy
- MySQL
- MySQL Workbench
- VS Code
- Pytest

## 🔄 Project Workflow

**Extract → Transform → Validate → Load**

### 1. Extract

- Load the Titanic dataset using Seaborn.
- Inspect the dataset dimensions, columns, data types, and missing values.

### 2. Transform

- Fill missing `age` values using the median.
- Fill missing `embarked` values using the mode.
- Remove the `deck` and `embark_town` columns.
- Encode `sex` as numerical values: male = 0 and female = 1.

### 3. Validate

- Check whether missing values remain.
- Verify that the `sex` column contains only 0 and 1.
- Confirm that the transformed data satisfies the defined validation rules.

### 4. Load

- Connect Python to MySQL using SQLAlchemy.
- Load the cleaned dataset into the `Titanic_ETL` database.
- Manage the database connection and release resources after loading.

### 5. Batch Processing

- Process data in configurable batches.
- Validate each batch before loading.
- Support appending subsequent batches to the target table.

## 📂 Project Structure

```text
Titanic-ETL-Pipeline/
├── extract.py
├── transform.py
├── validate.py
├── load.py
├── pipeline.py
├── batch_pipeline.py
├── config.py
├── test_connection.py
├── test_extract.py
├── test_transform.py
├── test_validate.py
├── requirements.txt
├── .gitignore
└── README.md
```

## 🚀 How to Run

1. Install Python and MySQL.
2. Create the `Titanic_ETL` database in MySQL.
3. Configure database credentials securely using environment variables.
4. Install the required Python dependencies.
5. Run the ETL pipeline:

```bash
python pipeline.py
```

To run batch processing:

```bash
python batch_pipeline.py
```

To run tests:

```bash
python -m pytest -q
```

## 📚 Key Learnings

- Understanding the ETL process.
- Cleaning and transforming real-world data.
- Connecting Python applications to MySQL.
- Writing modular and reusable Python code.
- Implementing data validation and batch processing.
- Organizing a data engineering project using Git and GitHub.

## 👩‍💻 Project Status

Hands-on learning project — built to strengthen my Python, SQL, and data engineering fundamentals.

**Extract → Transform → Validate → Load → Learn 🚀**
