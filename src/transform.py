import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:

    df["data"] = pd.to_datetime(df["data"], dayfirst=True)


    df["valor"] = pd.to_numeric(df["valor"], errors="coerce")


    df = df.dropna(subset=["valor"])


    df = df.sort_values("data")

    df = df.reset_index(drop=True)

    return df
