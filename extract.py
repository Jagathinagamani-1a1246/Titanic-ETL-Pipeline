import seaborn as sns

def extract():
    df = sns.load_dataset("titanic")

    print(
        f"Extracted {len(df)} rows, "
        f"{len(df.columns)} columns"
    )

    return df
