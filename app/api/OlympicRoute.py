from fastapi import APIRouter
from app.Services.OlympicService import fetchAndProcessOlympic
from app.schemas import PageRequest

router = APIRouter()

@router.post("/olympics/list")
async def olympics_list(request: PageRequest):
    """
    Endpoint que devuelve los eventos olímpicos desde RapidAPI.
    """
    return await fetchAndProcessOlympic(request.page)
