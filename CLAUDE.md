# CLAUDE.md · inmobiliaria-backend

## Proyecto
API de una plataforma inmobiliaria: los visitantes buscan casas, apartamentos y locales en venta o arriendo con filtros, y la inmobiliaria administra sus publicaciones.

## Stack y comandos
- Python con uv. Instalar: `uv sync`. Pruebas: `uv run pytest`. Servidor: `uv run uvicorn app.main:app --reload`.
- FastAPI + Pydantic. Por ahora los datos están en `data/inmuebles.json` (después MongoDB).

## Arquitectura (capas)
- `app/routers/`: solo reciben la petición y llaman al servicio. Sin lógica.
- `app/services/`: reglas de negocio.
- `app/repository.py`: único lugar que lee los datos y filtra.
- `app/models.py`: modelos Pydantic.

## Reglas
- Primero la prueba, después el código (TDD). Ninguna prueba se modifica para que pase.
- Cobertura mínima 80 % (`--cov-fail-under=80`), la revisa el CI.
- Nada de dependencias nuevas sin que yo lo apruebe.
- Los agentes no hacen commit ni push. Máximo 2 vueltas por punto de control; si no se resuelve, se me pregunta.
