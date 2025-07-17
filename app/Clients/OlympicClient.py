import os
import httpx 



RAPIDAPI_KEY = 'f04480b1a5msh7abf583cca0cd33p11fd99jsn81eafe521eeb'
RAPIDAPI_HOST = 'olympics-2024.p.rapidapi.com'

async def get_olympics_list(page=1):
    url = f"https://{RAPIDAPI_HOST}/list"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        "x-rapidapi-host": RAPIDAPI_HOST,
        "x-rapidapi-key": RAPIDAPI_KEY
    }
    data = {"page": page}
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(url, headers=headers, data=data)
            response.raise_for_status()
            return response.json()
    except httpx.HTTPStatusError as e:
        return {"error": f"HTTP error: {e.response.status_code} - {e.response.text}"}
    except Exception as e:
        return {"error": str(e)}
