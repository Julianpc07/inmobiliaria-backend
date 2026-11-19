from typing import Literal

from pydantic import BaseModel


class Inmueble(BaseModel):
    id: int
    titulo: str
    tipo: Literal["casa", "apartamento", "local"]
    operacion: Literal["venta", "arriendo"]
    ciudad: str
    precio: int
    habitaciones: int
    banos: int
    area_m2: int
