"""
Bike route
"""

# pylint: disable=import-error
from models.bike import Bike

# pylint: disable=import-error
from services.bike import (
    get_all_bikes,
    get_bike_by_id,
    create_bike,
    update_bike,
    delete_bike,
)

from fastapi import APIRouter, Body

# Crear una instancia del enrutador
bike_router = APIRouter()


# Obtener todas las bicicletas
@bike_router.get("/")
def get_bikes():
    """
    Obtiene todas las bicicletas.

    Retorna:
        Listado de todas las bicicletas.
    """
    return get_all_bikes()


# Obtener una bicicleta por su ID
@bike_router.get("/{id}")
def get_bike(bike_id: int):
    """
    Obtiene una bicicleta por su ID.

    Parámetros:
        id (int): ID de la bicicleta a obtener.

    Retorna:
        La bicicleta con el ID especificado.
    """
    return get_bike_by_id(bike_id)


# Registrar una nueva bicicleta
@bike_router.post("/")
def register_bike(bike: Bike = Body(...)):
    """
    Registra una nueva bicicleta.

    Parámetros:
        bike (Bike): Información de la bicicleta a registrar.

    Retorna:
        La bicicleta registrada.
    """
    return create_bike(bike)


# Actualizar los datos de una bicicleta existente
@bike_router.put("/{id}")
def update_bike_data(bike_id: int, bike: Bike = Body(...)):
    """
    Actualiza los datos de una bicicleta existente.

    Parámetros:
        id (int): ID de la bicicleta a actualizar.
        bike (Bike): Información actualizada de la bicicleta.

    Retorna:
        La bicicleta actualizada.
    """
    return update_bike(bike_id, bike)


# Eliminar una bicicleta por su ID
@bike_router.delete("/{id}")
def remove_bike(bike_id: int):
    """
    Elimina una bicicleta por su ID.

    Parámetros:
        id (int): ID de la bicicleta a eliminar.

    Retorna:
        Mensaje de confirmación de eliminación.
    """
    return delete_bike(bike_id)
