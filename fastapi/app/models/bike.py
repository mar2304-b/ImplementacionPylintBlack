"""
Bike model
"""

# pylint: disable=import-error
from pydantic import BaseModel, validator


class Bike(BaseModel):
    """
    Modelo de datos para una bicicleta.

    Atributos:
        model (str): Modelo de la bicicleta.
        type (str): Tipo de bicicleta ("mountain", "electric" o "bmx").
        material (str): Material de la bicicleta.
        color (str): Color de la bicicleta.
    """

    model: str
    type: str
    material: str
    color: str

    class Config:
        """Strips leading/trailing whitespace."""

        # pylint: disable=too-few-public-methods
        anystr_strip_whitespace = True

    @validator("type")
    # pylint: disable=no-self-argument
    def type_must_be_bike(cls, v):
        """
        Valida que el tipo de bicicleta sea "mountain", "electric" o "bmx".
        """
        if v in {"mountain", "electric", "bmx"}:
            return v
        raise ValueError("please, enter a valid type")
