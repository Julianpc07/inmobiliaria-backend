from typing import Literal

from pydantic import BaseModel, Field


class InmuebleNuevo(BaseModel):
    titulo: str = Field(min_length=5)
    tipo: Literal["casa", "apartamento", "local"]
    operacion: Literal["venta", "arriendo"]
    ciudad: str
    precio: int = Field(gt=0)
    habitaciones: int = Field(ge=0)
    banos: int = Field(ge=0)
    area_m2: int = Field(ge=0)


class Inmueble(InmuebleNuevo):
    id: int
