"""
main 
"""

# pylint: disable=import-error
from contextlib import asynccontextmanager

# pylint: disable=import-error
from starlette.responses import RedirectResponse

# pylint: disable=import-error
from database import database as connection

# pylint: disable=import-error
from routes.bike import bike_router

# pylint: disable=import-error
from routes.car import car_router

# pylint: disable=import-error
from fastapi import FastAPI


@asynccontextmanager
async def lifespan(_app: FastAPI):
    """
    Context manager para gestionar la conexión a la base de datos
    durante el ciclo de vida de la aplicación.

    Parámetros:
        app (FastAPI): Instancia de la aplicación FastAPI.
    """
    if connection.is_closed():
        connection.connect()  # Conectar a la base de datos si está cerrada
    try:
        yield  # Permite que la aplicación funcione
    finally:
        if not connection.is_closed():
            connection.close()  # Cerrar la conexión al finalizar


# Crear la instancia de la aplicación FastAPI
app = FastAPI(lifespan=lifespan)


@app.get("/")
async def read_root():
    """
    Redirige a la documentación de la API.

    Retorna:
        Redirección a la URL de la documentación.
    """
    return RedirectResponse(url="docs")


# Incluir los routers para bicicletas y coches
app.include_router(bike_router, prefix="/bikes", tags=["bikes"])
app.include_router(car_router, prefix="/cars", tags=["cars"])
