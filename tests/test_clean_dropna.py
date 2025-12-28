import pandas as pd
from pathlib import Path


DATA = Path(__file__).resolve().parents[1] / "data_files" / "sample_data.csv"


def load_df():
    # read the CSV created in the repo; pandas will treat empty fields as NaN by default
    return pd.read_csv(DATA)


def test_dropna_subset_email():
    df = load_df()
    # drop rows missing email
    cleaned = df.dropna(subset=["email"]) if "email" in df.columns else df
    # no email nulls remain
    assert cleaned["email"].isnull().sum() == 0
    # based on sample_data.csv, one row has missing email -> 7 total rows -> expect 6
    assert len(cleaned) == 6


def test_dropna_any():
    df = load_df()
    # drop rows with any NaN
    cleaned = df.dropna()
    # cleaned should have no nulls
    assert cleaned.isnull().sum().sum() == 0
    # based on sample_data.csv, rows with any NaN are 4 rows (including 'N/A' parsed as NaN) -> expect 3 remaining
    assert len(cleaned) == 3


def test_dropna_axis1():
    df = load_df()
    # drop any column that contains at least one NaN
    df_dropcols = df.dropna(axis=1)
    # remaining columns must contain no NaNs
    assert df_dropcols.isnull().sum().sum() == 0
    # number of columns should be <= original
    assert df_dropcols.shape[1] <= df.shape[1]
