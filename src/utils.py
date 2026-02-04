import pandas as pd
from pathlib import Path


def load_dataset(path: str) -> pd.DataFrame:
    """
    Loads the breast cancer dataset using a robust project-root-safe path.
    Works in both scripts and Jupyter notebooks.
    """
    try:
        # Works when called from .py files
        project_root = Path(__file__).resolve().parents[1]
    except NameError:
        # Fallback for Jupyter notebooks
        project_root = Path.cwd().parent

    full_path = project_root / path

    if not full_path.exists():
        raise FileNotFoundError(f"Dataset not found at {full_path}")

    df = pd.read_csv(full_path)

    # Standardize column names
    df.columns = [c.strip().lower() for c in df.columns]

    # Sanity check
    assert "diagnosis" in df.columns, "Target column missing"

    return df

