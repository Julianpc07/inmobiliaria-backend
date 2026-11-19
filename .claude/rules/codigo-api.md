---
paths:
  - "app/**/*.py"
---

# Reglas para el código de la API

- Los routers no filtran ni recorren listas: llaman a una función de `app/repository.py`.
- Los parámetros de búsqueda se declaran con `Query` y sus tipos, para que FastAPI devuelva 422 solo.
- Los modelos van en `app/models.py`. Nada de diccionarios sueltos como respuesta.
- No se agregan librerías. Si algo no se puede hacer con FastAPI, Pydantic o la librería estándar, se pregunta.
