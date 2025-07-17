from app.Clients.OlympicClient import get_olympics_list

async def fetchAndProcessOlympic(page=1):
    data = await get_olympics_list(page)
    return data