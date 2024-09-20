"""
bike service
"""

# pylint: disable=import-error
from database import BikeModel

# pylint: disable=import-error
from models.bike import Bike


# Obtener todas las bicicletas
def get_all_bikes():
    """
    Obtiene todas las bicicletas de la base de datos.

    Retorna:
        Listado de todas las bicicletas.
    """
    bikes = BikeModel.select().dicts()
    return list(bikes)


# Obtener una bicicleta por su ID
def get_bike_by_id(bike_id: int):
    """
    Obtiene una bicicleta por su ID.

    Parámetros:
        id (int): ID de la bicicleta a obtener.

    Retorna:
        La bicicleta correspondiente o un mensaje de error si no se encuentra.
    """
    try:
        bike = BikeModel.get(BikeModel.id == bike_id)
        return bike
    except BikeModel.DoesNotExist:
        return {"error": "Bike not found"}


# Crear una nueva bicicleta
def create_bike(bike: Bike):
    """
    Crea una nueva bicicleta en la base de datos.

    Parámetros:
        bike (Bike): Información de la bicicleta a crear.

    Retorna:
        La bicicleta creada.
    """
    BikeModel.create(
        model=bike.model,
        type=bike.type,
        material=bike.material,
        color=bike.color,
    )
    return bike


# Actualizar los datos de una bicicleta existente
def update_bike(bike_id: int, bike: Bike):
    """
    Actualiza los datos de una bicicleta existente.

    Parámetros:
        id (int): ID de la bicicleta a actualizar.
        bike (Bike): Información actualizada de la bicicleta.

    Retorna:
        Mensaje de éxito o error si no se encuentra la bicicleta.
    """
    updated_rows = (
        BikeModel.update(
            {
                BikeModel.model: bike.model,
                BikeModel.type: bike.type,
                BikeModel.material: bike.material,
                BikeModel.color: bike.color,
            }
        )
        .where(BikeModel.id == bike_id)
        .execute()
    )

    if updated_rows == 0:
        return {"error": "Bike not found"}
    return {"message": "Bike updated successfully"}


# Eliminar una bicicleta por su ID
def delete_bike(bike_id: int):
    """
    Elimina una bicicleta por su ID.

    Parámetros:
        id (int): ID de la bicicleta a eliminar.

    Retorna:
        Mensaje de éxito o error si no se encuentra la bicicleta.
    """
    try:
        bike = BikeModel.get(BikeModel.id == bike_id)
        bike.delete_instance()
    except BikeModel.DoesNotExist:
        return {"error": "Bike not found"}
    return {"message": "Bike deleted successfully"}
