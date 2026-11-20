import pytest
from fastapi.testclient import TestClient


@pytest.fixture
def cliente_limpio():
    """Cliente con el repositorio reiniciado antes y después de la prueba."""
    from app import repository
    from app.main import app

    repository.reiniciar()
    yield TestClient(app)
    repository.reiniciar()
