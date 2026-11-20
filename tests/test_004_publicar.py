import pytest

VALIDO = {
    "titulo": "Apartamento nuevo en el centro",
    "tipo": "apartamento",
    "operacion": "venta",
    "ciudad": "Pereira",
    "precio": 250000000,
    "habitaciones": 3,
    "banos": 2,
    "area_m2": 80,
}


def test_ca1_publica_y_asigna_id_9(cliente_limpio):
    respuesta = cliente_limpio.post("/inmuebles", json=VALIDO)
    assert respuesta.status_code == 201
    assert respuesta.json() == {"id": 9, **VALIDO}


def test_ca2_el_publicado_aparece_en_detalle_y_lista(cliente_limpio):
    assert cliente_limpio.post("/inmuebles", json=VALIDO).status_code == 201

    detalle = cliente_limpio.get("/inmuebles/9")
    assert detalle.status_code == 200
    assert detalle.json() == {"id": 9, **VALIDO}

    lista = cliente_limpio.get("/inmuebles")
    assert lista.status_code == 200
    ids = [i["id"] for i in lista.json()]
    assert len(ids) == 9
    assert 9 in ids


@pytest.mark.parametrize("precio", [0, -1, -500000])
def test_ca3_precio_cero_o_negativo_422(cliente_limpio, precio):
    respuesta = cliente_limpio.post("/inmuebles", json={**VALIDO, "precio": precio})
    assert respuesta.status_code == 422
    assert cliente_limpio.get("/inmuebles/9").status_code == 404


def test_ca4_tipo_invalido_422(cliente_limpio):
    respuesta = cliente_limpio.post("/inmuebles", json={**VALIDO, "tipo": "castillo"})
    assert respuesta.status_code == 422
    assert cliente_limpio.get("/inmuebles/9").status_code == 404


def test_ca5_titulo_corto_422(cliente_limpio):
    respuesta = cliente_limpio.post("/inmuebles", json={**VALIDO, "titulo": "Casa"})
    assert respuesta.status_code == 422
    assert cliente_limpio.get("/inmuebles/9").status_code == 404


def test_ca5_titulo_de_5_caracteres_es_valido(cliente_limpio):
    respuesta = cliente_limpio.post("/inmuebles", json={**VALIDO, "titulo": "Casas"})
    assert respuesta.status_code == 201
    assert respuesta.json()["titulo"] == "Casas"


def test_ca6_falta_campo_422(cliente_limpio):
    sin_ciudad = {k: v for k, v in VALIDO.items() if k != "ciudad"}
    respuesta = cliente_limpio.post("/inmuebles", json=sin_ciudad)
    assert respuesta.status_code == 422
    assert cliente_limpio.get("/inmuebles/9").status_code == 404
