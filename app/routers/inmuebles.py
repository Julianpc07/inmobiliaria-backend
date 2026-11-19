from fastapi import APIRouter

from app import repository
from app.models import Inmueble

router = APIRouter(prefix="/inmuebles", tags=["inmuebles"])


@router.get("", response_model=list[Inmueble], status_code=200)
def listar_inmuebles():
    return repository.listar()
