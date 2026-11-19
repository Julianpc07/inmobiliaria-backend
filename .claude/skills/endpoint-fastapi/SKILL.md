---
name: endpoint-fastapi
description: Pasos para agregar o cambiar un endpoint de FastAPI respetando las capas del proyecto (router → repository → models). La usa el desarrollador-api en el paso Green.
---

# Agregar un endpoint

1. **Modelo** (`app/models.py`): si la respuesta o el cuerpo es nuevo, crea el modelo Pydantic. Usa `Literal` para tipo y operacion.
2. **Repositorio** (`app/repository.py`): la función que lee o filtra los datos. Recibe parámetros simples y devuelve modelos.
3. **Router** (`app/routers/<recurso>.py`): declara la ruta, los `Query`/`Path`, el `response_model` y el `status_code`. Llama al repositorio y, si no hay resultado, `raise HTTPException(404, ...)`.
4. **main.py**: incluye el router si es nuevo.
5. Corre `uv run pytest` hasta que todo pase, sin tocar `tests/`.
6. Levanta `uv run uvicorn app.main:app` y prueba con curl el caso feliz y un caso de error. Pega la salida en EVIDENCIA.
7. Marca las tareas hechas en `specs/NNN-*/tasks.md`.
