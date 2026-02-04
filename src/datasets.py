import pandas as pd
from typing import Tuple


def encode_target(df: pd.DataFrame) -> pd.DataFrame:
    """
    Encodes diagnosis column:
    M -> 1 (malignant)
    B -> 0 (benign)
    """
    df = df.copy()
    df["target"] = df["diagnosis"].map({"M": 1, "B": 0})

    if df["target"].isnull().any():
        raise ValueError("Unexpected labels in diagnosis column")

    return df
def select_base_features(df: pd.DataFrame) -> pd.DataFrame:
    """
    Selects only mean-based geometric features used in this study.
    """
    columns = [
        "concavity_mean",
        "perimeter_mean",
        "radius_mean",
        "area_mean",
    ]

    missing = [c for c in columns if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    return df[columns + ["target"]]
