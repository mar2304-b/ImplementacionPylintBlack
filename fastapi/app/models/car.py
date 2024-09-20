"""
Car model
"""

# pylint: disable=import-error
from pydantic import BaseModel, validator


class Car(BaseModel):
    """
    Modelo de datos para un coche.

    Atributos:
        brand (str): Marca del coche.
        fuel_type (str): Tipo de combustible ("gasoline", "diesel" o "electric").
        transmission (str): Tipo de transmisión.
        color (str): Color del coche.
    """

    brand: str
    fuel_type: str
    transmission: str
    color: str

    class Config:
        """Strips leading/trailing whitespace."""

        # pylint: disable=too-few-public-methods
        anystr_strip_whitespace = True

    @validator("fuel_type")
    # pylint: disable=no-self-argument
    def fuel_type_must_be_gasoline(cls, v):
        """
        Valida que el tipo de combustible sea "gasoline", "diesel" o "electric".
        """
        if v in {"gasoline", "diesel", "electric"}:
            return v
        raise ValueError("please, enter a valid fuel type")
