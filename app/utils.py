# app/utils.py
import pandas as pd
import os

def load_country_data(country: str, data_dir: str):
    file_map = {
        "Benin": "benin_clean.csv",
        "Sierra Leone": "sierraleone_clean.csv",
        "Togo": "togo_clean.csv"
    }
    path = os.path.join(data_dir, file_map[country])
    return pd.read_csv(path)

def summary_statistics(df: pd.DataFrame, cols=None):
    if cols is None:
        cols = ["GHI", "DNI", "DHI"]
    summary = df[cols].agg(["mean", "median", "std"]).round(2)
    return summary

def get_country_metrics(data_dir: str):
    countries = ["Benin", "Sierra Leone", "Togo"]
    results = []
    for c in countries:
        df = load_country_data(c, data_dir)
        summary = df[["GHI", "DNI", "DHI"]].mean()
        summary["country"] = c
        results.append(summary)
    return pd.DataFrame(results)
