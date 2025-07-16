import pandas as pd

def cargar_csv():
    df = pd.read_csv("data/world_marathon_majors.csv")
    return df.to_dict(orient="records")
