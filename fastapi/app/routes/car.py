"""
car route
"""

# pylint: disable=import-error
from models.car import Car

# pylint: disable=import-error
from services.car import get_all_cars, get_car_by_id, create_car, update_car, delete_car

from fastapi import APIRouter, Body

# Crear una instancia del enrutador
car_router = APIRouter()


# Obtener todos los coches
@car_router.get("/")
def get_cars():
    """
    Obtiene todos los coches.

    Retorna:
        Listado de todos los coches.
    """
    return get_all_cars()


# Obtener un coche por su ID
@car_router.get("/{id}")
def get_car(car_id: int):
    """
    Obtiene un coche por su ID.

    Parámetros:
        id (int): ID del coche a obtener.

    Retorna:
        El coche con el ID especificado.
    """
    return get_car_by_id(car_id)


# Registrar un nuevo coche
@car_router.post("/")
def register_car(car: Car = Body(...)):
    """
    Registra un nuevo coche.

    Parámetros:
        car (Car): Información del coche a registrar.

    Retorna:
        El coche registrado.
    """
    return create_car(car)


# Actualizar los datos de un coche existente
@car_router.put("/{id}")
def update_car_data(car_id: int, car: Car = Body(...)):
    """
    Actualiza los datos de un coche existente.

    Parámetros:
        id (int): ID del coche a actualizar.
        car (Car): Información actualizada del coche.

    Retorna:
        El coche actualizado.
    """
    return update_car(car_id, car)


# Eliminar un coche por su ID
@car_router.delete("/{id}")
def remove_car(car_id: int):
    """
    Elimina un coche por su ID.

    Parámetros:
        id (int): ID del coche a eliminar.

    Retorna:
        Mensaje de confirmación de eliminación.
    """
    return delete_car(car_id)
