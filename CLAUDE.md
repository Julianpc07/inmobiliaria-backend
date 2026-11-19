# CLAUDE.md · inmobiliaria-backend

## Proyecto
API de una plataforma inmobiliaria: los visitantes buscan casas, apartamentos y locales en venta o arriendo, y la inmobiliaria publica sus inmuebles. El frontend está en el repo `inmobiliaria-frontend` y consume esta API.

## Comandos
- Instalar: `uv sync`
- Pruebas: `uv run pytest`
- Cobertura: `uv run pytest --cov=app --cov-report=term-missing --cov-fail-under=80`
- Servidor: `uv run uvicorn app.main:app --reload` (http://localhost:8000, documentación en /docs)

## Organización
- `app/main.py`: crea la app de FastAPI, el CORS para `http://localhost:5173` e incluye los routers.
- `app/models.py`: modelos Pydantic (`Inmueble`, `InmuebleNuevo`).
- `app/repository.py`: único lugar que lee `data/inmuebles.json` y filtra. Los datos se cargan en memoria.
- `app/routers/`: un archivo por recurso. Solo reciben la petición y llaman al repositorio. Sin lógica.
- `tests/`: una prueba por criterio de aceptación, con `TestClient`.
- `specs/NNN-nombre/`: spec.md, plan.md y tasks.md de cada funcionalidad.

## Convenciones
- Nombres en español (inmueble, operacion, ciudad). Sin tildes en el código.
- Valores permitidos: tipo = casa | apartamento | local; operacion = venta | arriendo.
- Respuestas de error con `HTTPException` (404 si no existe, 422 si los datos no son válidos).

## Lo que el agente NO debe hacer
- Modificar una prueba para que pase.
- Tocar `data/inmuebles.json` o `pyproject.toml`, o agregar dependencias.
- Hacer commit o push (los hace Julián).
- Seguir más de 2 vueltas en el mismo punto de control sin preguntar.

## Flujo de trabajo
Cada funcionalidad es una spec en `specs/`. Se trabaja con `claude --agent orquestador-api` en una rama `NNN-nombre`, primero pruebas (Red), después código (Green), revisión y PR a main.
