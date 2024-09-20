"""
car service
"""

# pylint: disable=import-error
from database import CarModel

# pylint: disable=import-error
from models.car import Car


# Obtener todos los coches
def get_all_cars():
    """
    Obtiene todos los coches de la base de datos.

    Retorna:
        Listado de todos los coches.
    """
    cars = CarModel.select().dicts()
    return list(cars)


# Obtener un coche por su ID
def get_car_by_id(car_id: int):
    """
    Obtiene un coche por su ID.

    Parámetros:
        id (int): ID del coche a obtener.

    Retorna:
        El coche correspondiente o un mensaje de error si no se encuentra.
    """
    try:
        car = CarModel.get(CarModel.id == car_id)
        return car
    except CarModel.DoesNotExist:
        return {"error": "Car not found"}


# Crear un nuevo coche
def create_car(car: Car):
    """
    Crea un nuevo coche en la base de datos.

    Parámetros:
        car (Car): Información del coche a crear.

    Retorna:
        El coche creado.
    """
    CarModel.create(
        brand=car.brand,
        fuel_type=car.fuel_type,
        transmission=car.transmission,
        color=car.color,
    )
    return car


# Actualizar los datos de un coche existente
def update_car(car_id: int, car: Car):
    """
    Actualiza los datos de un coche existente.

    Parámetros:
        id (int): ID del coche a actualizar.
        car (Car): Información actualizada del coche.

    Retorna:
        Mensaje de éxito o error si no se encuentra el coche.
    """
    updated_rows = (
        CarModel.update(
            {
                CarModel.brand: car.brand,
                CarModel.fuel_type: car.fuel_type,
                CarModel.transmission: car.transmission,
                CarModel.color: car.color,
            }
        )
        .where(CarModel.id == car_id)
        .execute()
    )

    if updated_rows == 0:
        return {"error": "Car not found"}
    return {"message": "Car updated successfully"}


# Eliminar un coche por su ID
def delete_car(car_id: int):
    """
    Elimina un coche por su ID.

    Parámetros:
        id (int): ID del coche a eliminar.

    Retorna:
        Mensaje de éxito o error si no se encuentra el coche.
    """
    try:
        car = CarModel.get(CarModel.id == car_id)
        car.delete_instance()
    except CarModel.DoesNotExist:
        return {"error": "Car not found"}
    return {"message": "Car deleted successfully"}
