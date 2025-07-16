from fastapi import FastAPI
from app import services

app = FastAPI()

@app.get("/health")
def health_check():
    return {"status": "ok"}

@app.get("/deportes")
def obtener_datos_deportivos():
    datos = services.cargar_csv()
    return {"datos": datos}
