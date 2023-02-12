import pandas as pd
from pandas import DataFrame


def read_disease_and_serve(fname: str, disease: str):
    df = pd.read_csv(fname)
    return serve(df, disease)


def serve(df: DataFrame, disease: str):
    disease = disease.lower()
    df["Disease"] = df["Disease"].map(lambda s: s.lower())

    matched_rows = str(df[df["Disease"] == disease].to_records()[0][2])
    return [s.strip() for s in matched_rows.split(",")]


if __name__ == "__main__":
    print(
        read_disease_and_serve(
            fname="./data/disease_ingredient.csv", disease="infection"
        )
    )
