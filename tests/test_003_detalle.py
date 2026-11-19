import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def cliente():
    from app.main import app

    return TestClient(app)


def test_ca1_detalle_de_un_inmueble_existente(cliente):
    respuesta = cliente.get("/inmuebles/4")
    assert respuesta.status_code == 200
    cuerpo = respuesta.json()
    assert cuerpo["id"] == 4
    assert cuerpo["titulo"] == "Casa campestre en vía a Rivera"


def test_ca2_id_inexistente_404(cliente):
    respuesta = cliente.get("/inmuebles/99")
    assert respuesta.status_code == 404
    assert respuesta.json() == {"detail": "Inmueble no encontrado"}


def test_ca3_id_no_numerico_422(cliente):
    respuesta = cliente.get("/inmuebles/abc")
    assert respuesta.status_code == 422
