from typing import Literal

from fastapi import APIRouter, HTTPException, Query

from app import repository
from app.models import Inmueble

router = APIRouter(prefix="/inmuebles", tags=["inmuebles"])


@router.get("", response_model=list[Inmueble], status_code=200)
def listar_inmuebles(
    tipo: Literal["casa", "apartamento", "local"] | None = Query(None),
    operacion: Literal["venta", "arriendo"] | None = Query(None),
    ciudad: str | None = Query(None),
    precio_min: int | None = Query(None, ge=0),
    precio_max: int | None = Query(None, ge=0),
):
    if precio_min is not None and precio_max is not None and precio_min > precio_max:
        raise HTTPException(422, "precio_min no puede ser mayor que precio_max")
    return repository.buscar(tipo, operacion, ciudad, precio_min, precio_max)
