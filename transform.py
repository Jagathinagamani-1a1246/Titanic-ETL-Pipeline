
def transform(df):
    df = df.copy()

    # Step 1: Fill missing ages with the median
    df["age"] = df["age"].fillna(df["age"].median())

    # Step 2: Fill missing embarked values with the mode
    df["embarked"] = df["embarked"].fillna(
        df["embarked"].mode()[0]
    )

    # Step 3: Drop columns with too many missing values
    df = df.drop(columns=["deck", "embark_town"])

    # Step 4: Convert sex into numeric values
    df["sex"] = df["sex"].map({
        "male": 0,
        "female": 1
    })

    print(f"Transformed shape: {df.shape}")

    return df
