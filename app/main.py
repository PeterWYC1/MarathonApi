from fastapi import FastAPI
from app.api.OlympicRoute import router as olympics_router
from app.api.LocalRoute import router as local_router

app = FastAPI(
    title="Olympics & Sports API",
    description="API con datos locales y conexión a RapidAPI",
    version="1.0.0"
)

app.include_router(olympics_router, prefix="/external", tags=["Olympics"])
app.include_router(local_router, prefix="/local", tags=["Local Data"])
