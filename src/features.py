import pandas as pd


def add_irregularity_index(df: pd.DataFrame) -> pd.DataFrame:
    """
    Adds Irregularity Index = concavity_mean / (perimeter_mean^2)

    This feature is designed to capture boundary irregularity
    independent of tumor size.
    """
    df = df.copy()

    if "concavity_mean" not in df.columns or "perimeter_mean" not in df.columns:
        raise ValueError("Required columns missing for Irregularity Index")

    df["irregularity_index"] = (
        df["concavity_mean"] / (df["perimeter_mean"] ** 2)
    )

    return df
