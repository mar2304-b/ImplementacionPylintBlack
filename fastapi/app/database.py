"""
database config
"""

# pylint: disable=import-error
import os

# pylint: disable=import-error
from dotenv import load_dotenv

# pylint: disable=import-error
from peewee import Model, AutoField, CharField, IntegerField, MySQLDatabase

# Cargar variables de entorno desde un archivo .env
load_dotenv()

# Configuración de la base de datos MySQL
database = MySQLDatabase(
    os.getenv("MYSQL_DATABASE"),
    user=os.getenv("MYSQL_USER"),
    password=os.getenv("MYSQL_PASSWORD"),
    host=os.getenv("MYSQL_HOST"),
    port=int(os.getenv("MYSQL_PORT")),
)


# Modelo de datos para los coches
class CarModel(Model):
    """
    Modelo que representa la tabla de coches en la base de datos.
    """

    id = AutoField()  # Campo auto incremental para el ID
    brand = CharField()  # Campo para la marca del coche
    fuel_type = CharField()  # Campo para el tipo de combustible
    color = CharField()  # Campo para el color del coche

    class Meta:
        """model meta"""

        # pylint: disable=too-few-public-methods
        database = database  # Base de datos asociada
        table_name = "cars"  # Nombre de la tabla en la base de datos


# Modelo de datos para las bicicletas
class BikeModel(Model):
    """
    Modelo que representa la tabla de bicicletas en la base de datos.
    """

    id = AutoField()  # Campo auto incremental para el ID
    model = CharField()  # Campo para el modelo de la bicicleta
    type = CharField()  # Campo para el tipo de bicicleta
    material = IntegerField()  # Campo para el material (debe ser un entero)
    color = IntegerField()  # Campo para el color (debe ser un entero)

    class Meta:
        """model meta"""

        # pylint: disable=too-few-public-methods
        database = database  # Base de datos asociada
        table_name = "bikes"  # Nombre de la tabla en la base de datos
