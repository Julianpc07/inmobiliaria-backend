import json
from pathlib import Path

from app.models import Inmueble, InmuebleNuevo

RUTA_DATOS = Path(__file__).resolve().parent.parent / "data" / "inmuebles.json"


def _cargar() -> list[Inmueble]:
    with RUTA_DATOS.open(encoding="utf-8") as archivo:
        return [Inmueble(**item) for item in json.load(archivo)]


_inmuebles: list[Inmueble] = _cargar()


def buscar(
    tipo: str | None = None,
    operacion: str | None = None,
    ciudad: str | None = None,
    precio_min: int | None = None,
    precio_max: int | None = None,
) -> list[Inmueble]:
    resultado = []
    for inmueble in sorted(_inmuebles, key=lambda i: i.id):
        if tipo is not None and inmueble.tipo != tipo:
            continue
        if operacion is not None and inmueble.operacion != operacion:
            continue
        if ciudad is not None and inmueble.ciudad.lower() != ciudad.lower():
            continue
        if precio_min is not None and inmueble.precio < precio_min:
            continue
        if precio_max is not None and inmueble.precio > precio_max:
            continue
        resultado.append(inmueble)
    return resultado


def obtener(id: int) -> Inmueble | None:
    for inmueble in _inmuebles:
        if inmueble.id == id:
            return inmueble
    return None


def listar() -> list[Inmueble]:
    return buscar()


def crear(nuevo: InmuebleNuevo) -> Inmueble:
    siguiente = max((i.id for i in _inmuebles), default=0) + 1
    inmueble = Inmueble(id=siguiente, **nuevo.model_dump())
    _inmuebles.append(inmueble)
    return inmueble


def reiniciar() -> None:
    _inmuebles[:] = _cargar()
