FROM python:3.12

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copia el código de la aplicación al contenedor
COPY ./app ./app
COPY ./data ./data

#  Expone el puerto 8000 (por defecto en FastAPI/Uvicorn)
EXPOSE 8000

#  Comando para correr la aplicación usando uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]