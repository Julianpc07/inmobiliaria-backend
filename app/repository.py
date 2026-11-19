import json
from pathlib import Path

from app.models import Inmueble

RUTA_DATOS = Path(__file__).resolve().parent.parent / "data" / "inmuebles.json"


def _cargar() -> list[Inmueble]:
    with RUTA_DATOS.open(encoding="utf-8") as archivo:
        return [Inmueble(**item) for item in json.load(archivo)]


_inmuebles: list[Inmueble] = _cargar()


def listar() -> list[Inmueble]:
    return sorted(_inmuebles, key=lambda inmueble: inmueble.id)
