
from extract import extract
from transform import transform
from validate import validate
from load import load


def run_pipeline():
    print("\n========== ETL PIPELINE STARTED ==========\n")

    # Stage 1: Extract
    print("STEP 1: Extracting data...")
    raw = extract()

    # Stage 2: Transform
    print("\nSTEP 2: Transforming data...")
    clean = transform(raw)

    # Stage 3: Validate
    print("\nSTEP 3: Validating data...")
    validate(clean)

    # Stage 4: Load
    print("\nSTEP 4: Loading data into MySQL...")
    load(clean)

    print("\n========== ETL PIPELINE COMPLETED ==========\n")


if __name__ == "__main__":
    run_pipeline()
