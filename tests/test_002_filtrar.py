import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def cliente():
    from app.main import app

    return TestClient(app)


def ids_de(respuesta):
    return [i["id"] for i in respuesta.json()]


def test_ca1_filtra_por_tipo(cliente):
    respuesta = cliente.get("/inmuebles", params={"tipo": "casa"})
    assert respuesta.status_code == 200
    assert ids_de(respuesta) == [1, 4, 6]
    assert all(i["tipo"] == "casa" for i in respuesta.json())


def test_ca2_filtra_por_operacion(cliente):
    respuesta = cliente.get("/inmuebles", params={"operacion": "arriendo"})
    assert respuesta.status_code == 200
    assert ids_de(respuesta) == [2, 3, 6, 8]
    assert all(i["operacion"] == "arriendo" for i in respuesta.json())


def test_ca3_ciudad_sin_importar_mayusculas(cliente):
    for ciudad in ("neiva", "NEIVA", "Neiva"):
        respuesta = cliente.get("/inmuebles", params={"ciudad": ciudad})
        assert respuesta.status_code == 200
        assert ids_de(respuesta) == [1, 2, 3, 5], f"ciudad={ciudad}"


def test_ca4_rango_de_precio_incluye_limites(cliente):
    respuesta = cliente.get(
        "/inmuebles", params={"precio_min": 1000000, "precio_max": 2000000}
    )
    assert respuesta.status_code == 200
    assert ids_de(respuesta) == [2, 6]

    # Limites exactos: 1.200.000 (id 2) y 1.500.000 (id 6) deben quedar dentro.
    respuesta = cliente.get(
        "/inmuebles", params={"precio_min": 1200000, "precio_max": 1500000}
    )
    assert respuesta.status_code == 200
    assert ids_de(respuesta) == [2, 6]


def test_ca5_combina_filtros(cliente):
    respuesta = cliente.get(
        "/inmuebles", params={"tipo": "apartamento", "operacion": "venta"}
    )
    assert respuesta.status_code == 200
    assert ids_de(respuesta) == [5]


def test_ca6_sin_resultados_lista_vacia(cliente):
    # No existe ningun local en Garzon.
    respuesta = cliente.get("/inmuebles", params={"tipo": "local", "ciudad": "Garzon"})
    assert respuesta.status_code == 200
    assert respuesta.json() == []


def test_ca7_tipo_invalido_422(cliente):
    respuesta = cliente.get("/inmuebles", params={"tipo": "finca"})
    assert respuesta.status_code == 422


def test_ca8_precio_min_mayor_que_max_422(cliente):
    respuesta = cliente.get(
        "/inmuebles", params={"precio_min": 2000000, "precio_max": 1000000}
    )
    assert respuesta.status_code == 422
