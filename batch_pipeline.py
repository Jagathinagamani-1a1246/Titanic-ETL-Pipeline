
import argparse
from extract import extract
from transform import transform
from validate import validate
from load import load


def run_batch_pipeline(batch_size=100, table_name="passengers_batch"):
    print("\n========== BATCH PIPELINE STARTED ==========\n")

    raw = extract()
    total_rows = len(raw)

    batch_number = 0

    for start in range(0, total_rows, batch_size):
        batch_number += 1
        end = min(start + batch_size, total_rows)

        print(
            f"Processing batch {batch_number}: "
            f"rows {start + 1} to {end}"
        )

        batch = raw.iloc[start:end].copy()

        clean = transform(batch)
        validate(clean)

        if batch_number == 1:
            load(clean, table_name, if_exists="replace")
        else:
            load(clean, table_name, if_exists="append")

    print(f"\nTotal rows processed: {total_rows}")
    print(f"Total batches: {batch_number}")
    print("\n========== BATCH PIPELINE COMPLETED ==========")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--batch-size",
        type=int,
        default=100
    )

    parser.add_argument(
        "--table",
        default="passengers_batch"
    )

    args = parser.parse_args()

    if args.batch_size <= 0:
        parser.error("--batch-size must be greater than zero")

    run_batch_pipeline(args.batch_size, args.table)
