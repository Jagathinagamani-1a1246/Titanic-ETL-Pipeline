
def validate(df):
    # Check for missing values
    assert (
        df.isnull().sum().sum() == 0
    ), "Nulls still present!"

    # Check whether sex contains only 0 or 1
    assert (
        df["sex"].isin([0, 1]).all()
    ), "Sex not fully encoded!"

    print("Validation passed")
