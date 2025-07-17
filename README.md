1. Descripción general del proyecto
 - Nombre del código: MarathonApi
 - Explicación general: API para obtener datos deportivos, combinando datos locales con una conexión a RapidAPI para información olímpica.
 - Problema resuelto: Facilita el acceso a datos de maratones y eventos olímpicos a través de una interfaz unificada.

2.  Visión general del sistema
 - Arquitectura del sistema:
 ```mermaid
 graph LR
    A[Cliente] --> B(FastAPI App);
    B --> C{Rutas};
    C --> D[Datos locales];
    C --> E[RapidAPI];
    D --> F(CSV);
    E --> G(Olympic API);
 ```
 - Tecnologías utilizadas:
  - FastAPI
  - Uvicorn
  - httpx
  - Pandas
 - Dependencias:
  - fastapi
  - uvicorn[standard]
  - httpx
  - pandas
  - numpy
  - scipy
  - matplotlib
  - seaborn
  - scikit-learn
  - pydantic
  - pytest
  - jupyterlab
  - statsmodels
  - plotly
  - python-dotenv
 - Requisitos del sistema:
  - Python 3.12
  - Docker (opcional para la ejecución en contenedor)
 - Prerrequisitos:
  - Tener instalado Python 3.12.
  - Haber instalado las dependencias listadas en `requirements.txt`.
  - Para la API de Olympics, se requiere una clave de RapidAPI.

3. 📦 Guía de uso
 - Cómo usarlo: La API se puede ejecutar localmente o en un contenedor Docker. Para ejecutarla localmente, instalar las dependencias y ejecutar `uvicorn app.main:app --host 0.0.0.0 --port 8000`.  Para Docker, construir y ejecutar el contenedor usando el `Dockerfile` provisto.
 - Explicación de los pasos:
  - Entrada: Las rutas `/local/deportes` no requieren parámetros. La ruta `/external/olympics/list` requiere un objeto JSON con el parámetro `page`.
  - Salida: La ruta `/local/deportes` devuelve un JSON con datos de maratones. La ruta `/external/olympics/list` devuelve un JSON con datos de eventos olímpicos.
  - Parámetros: La ruta `/external/olympics/list` acepta un parámetro `page` (entero) para la paginación de resultados.
 - Caso de uso de ejemplo:
 ```python
 import httpx
 import asyncio

 async def obtener_datos_olimpicos(page_number: int = 1):
     async with httpx.AsyncClient() as client:
         response = await client.post(
             "http://localhost:8000/external/olympics/list",
             json={"page": page_number}
         )
         return response.json()

 async def main():
     data = await obtener_datos_olimpicos(page_number=2)
     print(data)

 if __name__ == "__main__":
     asyncio.run(main())
 ```

4. 🔐 Documentación de la API
 - Endpoints:
  - `/local/health`: GET -  Verifica el estado de salud de la API local.
  - `/local/deportes`: GET -  Obtiene datos de maratones desde un archivo CSV local.
  - `/external/olympics/list`: POST -  Obtiene una lista de eventos olímpicos paginada desde RapidAPI.
 - Formatos de solicitud y respuesta:
  - `/local/health`:
   - Solicitud: Ninguna.
   - Respuesta: `{"status": "ok"}`
  - `/local/deportes`:
   - Solicitud: Ninguna.
   - Respuesta: `{"datos": [...]}` (lista de diccionarios con datos de maratones)
  - `/external/olympics/list`:
   - Solicitud: `{"page": int}`
   - Respuesta: `{"total_events": int, "events": [...]}` (total de eventos y lista de eventos olímpicos)
 - Autenticación y autorización:
  - La API de Olympics requiere una clave de RapidAPI, que se debe configurar como una variable de entorno. La API local no requiere autenticación.

5. 📚 Referencias
  - FastAPI: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
  - Uvicorn: [https://www.uvicorn.org/](https://www.uvicorn.org/)
  - httpx: [https://www.python-httpx.org/](https://www.python-httpx.org/)
  - RapidAPI: [https://www.rapidapi.com/](https://www.rapidapi.com/)
  - Pydantic: [https://docs.pydantic.dev/](https://docs.pydantic.dev/)
  - Docker: [https://www.docker.com/](https://www.docker.com/)
