# Titanic_ETL

A beginner-friendly ETL project using the Titanic passenger dataset.

## Folder structure

```text
Titanic_ETL/
├── data/
│   └── train.csv
├── output/
├── config.py
├── extract.py
├── transform.py
├── validate.py
├── load.py
├── pipeline.py
├── batch_pipeline.py
├── test_connection.py
├── test_extract.py
├── test_transform.py
├── test_validate.py
├── requirements.txt
└── README.md
```

## 1. Setup

Use Python 3.9 or newer. Open a terminal in this folder and run:

```bash
python -m pip install -r requirements.txt
```

## 2. Add the dataset

Download the Titanic `train.csv` file from the Kaggle Titanic competition and place it in the `data/` folder.

Expected path:

```text
Titanic_ETL/data/train.csv
```

The standard Kaggle training file includes columns such as `PassengerId`, `Survived`, `Pclass`, `Name`, `Sex`, `Age`, and `Fare`.

## 3. Run the single-file pipeline

```bash
python pipeline.py
```

The pipeline extracts the CSV, validates it, cleans and standardizes values, validates the cleaned data, and writes the results to `output/`.

Outputs:
- `output/titanic_cleaned.csv`
- `output/validation_report.txt`

## 4. Run batch processing

Put one or more Titanic-format CSV files in `data/`, then run:

```bash
python batch_pipeline.py
```

Batch results are saved under `output/batch/`.

## 5. Run tests

```bash
python -m pytest -q
```

Or check the Python environment only:

```bash
python test_connection.py
```

## What each file does

- `config.py`: Stores file paths and required column names.
- `extract.py`: Reads data from the source CSV.
- `transform.py`: Cleans text, fills selected missing values, and removes duplicate passenger IDs.
- `validate.py`: Checks required columns and basic data rules.
- `load.py`: Saves cleaned data and a validation report.
- `pipeline.py`: Runs all ETL stages once.
- `batch_pipeline.py`: Processes all CSV files in the data folder.
- `test_connection.py`: Checks Python and pandas.
- `test_extract.py`: Tests extraction.
- `test_transform.py`: Tests transformation.
- `test_validate.py`: Tests validation.

## Notes

- This project does not include the Titanic dataset. Download it separately and put `train.csv` in `data/`.
- The transformation fills missing `Age` and `Fare` values with their column median, fills missing `Embarked` with its most common value, and labels missing `Cabin` values as `Unknown`.
- This is an educational example. For real production data, agree on validation rules with the data owner before dropping or filling values.
