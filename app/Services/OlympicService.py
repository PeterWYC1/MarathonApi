from app.Clients.OlympicClient import get_olympics_list

async def fetchAndProcessOlympic(page=1):
    """
    Servicio que llama al cliente y procesa la data.
    Aquí podrías combinar con datos locales si quieres.
    """
    data = await get_olympics_list(page)

    # Ejemplo de procesamiento simple: contar eventos
    processed_data = {
        "total_events": len(data.get("events", [])),
        "events": data.get("events", [])
    }

    return processed_data