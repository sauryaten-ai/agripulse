import pandas as pd


def parse_csv(file):

    df = pd.read_csv(file)

    required_columns = [
        "soil_id",
        "nitrogen",
        "phosphorus",
        "potassium",
        "ph_level"
    ]

    for col in required_columns:
        if col not in df.columns:
            raise ValueError("Invalid CSV format")

    return df