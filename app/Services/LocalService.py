import os
import pandas as pd

def cargar_csv():
    # __file__ apunta a app/services/services.py
    base_dir = os.path.dirname(os.path.abspath(__file__))  # app/services
    project_root = os.path.dirname(os.path.dirname(base_dir))  # subimos dos veces: app/services -> app -> raíz proyecto

    csv_path = os.path.join(project_root, 'data', 'world_marathon_majors.csv')

    try:
        df = pd.read_csv(csv_path, encoding="latin-1")
        return df.to_dict(orient='records')
    except Exception as e:
        return {"error": str(e)}
