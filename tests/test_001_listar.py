import pytest
from fastapi.testclient import TestClient

CAMPOS = {"id", "titulo", "tipo", "operacion", "ciudad", "precio", "habitaciones", "banos", "area_m2"}


@pytest.fixture
def cliente():
    from app.main import app

    return TestClient(app)


def test_ca1_lista_los_8_inmuebles(cliente):
    respuesta = cliente.get("/inmuebles")
    assert respuesta.status_code == 200
    cuerpo = respuesta.json()
    assert isinstance(cuerpo, list)
    assert len(cuerpo) == 8


def test_ca2_cada_inmueble_tiene_todos_los_campos(cliente):
    respuesta = cliente.get("/inmuebles")
    assert respuesta.status_code == 200
    inmuebles = respuesta.json()
    assert len(inmuebles) == 8
    for inmueble in inmuebles:
        faltan = CAMPOS - set(inmueble)
        assert not faltan, f"inmueble {inmueble.get('id')} sin campos: {faltan}"


def test_ca3_ordenados_por_id(cliente, monkeypatch):
    from app import repository
    from app.models import Inmueble

    def crear(id_):
        return Inmueble(
            id=id_, titulo=f"Inmueble {id_}", tipo="casa", operacion="venta",
            ciudad="Bogota", precio=100, habitaciones=1, banos=1, area_m2=50,
        )

    # Lista en memoria desordenada a proposito (el JSON no se toca).
    monkeypatch.setattr(repository, "_inmuebles", [crear(5), crear(2), crear(9), crear(1), crear(7)])

    respuesta = cliente.get("/inmuebles")
    assert respuesta.status_code == 200
    ids = [i["id"] for i in respuesta.json()]
    assert ids == [1, 2, 5, 7, 9]


def test_ca4_cors_para_el_frontend(cliente):
    origen = "http://localhost:5173"
    respuesta = cliente.get("/inmuebles", headers={"Origin": origen})
    assert respuesta.status_code == 200
    assert respuesta.headers.get("access-control-allow-origin") == origen


def test_ca4_cors_no_permite_otros_origenes(cliente):
    respuesta = cliente.get("/inmuebles", headers={"Origin": "http://evil.com"})
    assert respuesta.status_code == 200
    assert "access-control-allow-origin" not in respuesta.headers
