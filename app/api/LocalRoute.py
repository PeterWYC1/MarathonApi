from fastapi import APIRouter
from app.Services.LocalService import cargar_csv

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.get("/deportes")
def obtener_datos_deportivos():
    datos = cargar_csv()
    return {"datos": datos}
