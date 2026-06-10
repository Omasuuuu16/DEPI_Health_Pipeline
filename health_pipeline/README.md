# DEPI Health Data Pipeline

## Project Overview

This project was developed as part of the DEPI Data Engineering track. The goal is to build a complete ETL and analytics pipeline for student health data using Python, SQL Server, and dbt.

The pipeline performs:

* Data Extraction from CSV files
* Data Validation and Quality Checks
* Data Loading into SQL Server
* Data Transformation using dbt
* Feature Engineering
* Data Modeling for Analytics

---

## Project Architecture

```text
CSV Dataset
     |
     v
Extract & Validate (Python)
     |
     v
Load to SQL Server
     |
     v
Staging Layer (dbt)
     |
     v
Intermediate Layer (dbt)
     |
     v
Mart Layer (dbt)
     |
     v
Analytics & Reporting
```

---

## Technologies Used

* Python 3.10
* Pandas
* SQL Server
* dbt (Data Build Tool)
* Git & GitHub
* SQL

---

## Project Structure

```text
DEPI_Final_Project/
│
├── Load.py
├── extract_validate.py
├── .gitignore
│
├── health_pipeline/
│   ├── dbt_project.yml
│   ├── models/
│   │   ├── sources.yml
│   │   ├── stg_student_health.sql
│   │   ├── int_features.sql
│   │   ├── int_encoded.sql
│   │   └── mart_student_health.sql
│   │
│   ├── analyses/
│   ├── macros/
│   ├── seeds/
│   ├── snapshots/
│   └── tests/
│
└── logs/
```

---

## ETL Process

### 1. Extract

The raw student health dataset is loaded from CSV files.

### 2. Validate

Validation checks include:

* Schema validation
* Row count verification
* Null value detection
* Data type consistency checks
* Duplicate record detection

### 3. Load

Validated data is loaded into SQL Server database:

```text
DEPI_Health
```

---

## dbt Models

### Staging Layer

#### stg_student_health

* Cleans source data
* Standardizes column names
* Applies initial transformations

---

### Intermediate Layer

#### int_features

Creates derived business features.

Examples:

* Sleep quality indicators
* Lifestyle metrics
* Health score attributes

#### int_encoded

Encodes categorical variables for analytical use.

---

### Mart Layer

#### mart_student_health

Final analytical model containing:

* Student demographics
* Lifestyle information
* Health metrics
* Engineered features

This model serves as the reporting and analytics layer.

---

## Data Quality Checks

The project includes automated quality validation such as:

* Missing value detection
* Schema consistency checks
* Duplicate detection
* Record count validation

These checks help ensure data reliability before loading into SQL Server.

---

## Database Design

The project follows a layered architecture:

```text
Source Data
    |
    v
Staging
    |
    v
Intermediate
    |
    v
Mart
```

This design improves maintainability, scalability, and analytical performance.

---

## How to Run the Project

### 1. Clone Repository

```bash
git clone https://github.com/Omasuuuu16/DEPI_Health_Pipeline.git
cd DEPI_Health_Pipeline
```

### 2. Install Dependencies

```bash
pip install pandas
pip install dbt-sqlserver
```

### 3. Run Validation

```bash
python extract_validate.py
```

### 4. Load Data

```bash
python Load.py
```

### 5. Run dbt Models

```bash
cd health_pipeline

dbt debug
dbt run
dbt test
```

---

## Key Outcomes

* Built a complete ETL pipeline.
* Implemented data quality validation.
* Loaded data into SQL Server.
* Created transformation layers using dbt.
* Developed an analytics-ready mart model.
* Applied Data Engineering best practices.

---

## Author

Omar Mohamed Galal

DEPI Data Engineering Track
