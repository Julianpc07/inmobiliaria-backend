---
name: revision-pr
description: Lista de revisión y formato de hallazgos para revisar una rama antes del pull request. La usa el revisor-api.
---

# Revisión antes del PR

Revisa en este orden y no edites nada:

1. `git diff main...HEAD --stat` y después el diff completo.
2. **Spec contra código:** cada criterio de `spec.md` tiene prueba (matriz) y el código hace lo que dice, ni más ni menos.
3. **Pruebas:** sin pruebas vacías, tautológicas ni que dependan del orden.
4. **Capas:** routers sin lógica; filtrado solo en `repository.py`; modelos en `models.py`.
5. **Nada inventado:** cada import existe en las dependencias del pyproject.
6. **Cobertura:** `uv run pytest --cov=app --cov-report=term-missing --cov-fail-under=80`.

## Formato de cada hallazgo
`[SEVERIDAD] archivo:línea — qué pasa — lo corrige: probador-api | desarrollador-api`

Severidades: CRÍTICO (rompe un criterio), ALTO (prueba débil o capa rota), MEDIO, BAJO.
Al final: veredicto **APROBADO** o **CAMBIOS** y el porcentaje de cobertura. Este informe se pega como comentario en el PR.
