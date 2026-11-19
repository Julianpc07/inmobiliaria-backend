---
name: criterios-a-pruebas
description: Convierte los criterios de aceptación de una spec en pruebas pytest con TestClient y entrega la matriz criterio → prueba. La usa el probador-api antes de que exista el código.
---

# De criterios de aceptación a pruebas

1. Lee `specs/NNN-*/spec.md` y lista los criterios CA1, CA2...
2. Por cada criterio escribe al menos una prueba en `tests/test_NNN_*.py`:
   - Nombre: `test_caN_<lo_que_verifica>`.
   - Estructura: preparar → llamar al endpoint con `TestClient` → `assert` del código de estado **y** del contenido.
3. Agrega los casos borde que el criterio deja implícitos (lista vacía, precio igual al límite, id que no existe).
4. Corre `uv run pytest tests/test_NNN_*.py` y comprueba que **fallan por el motivo correcto** (404 porque la ruta no existe, ImportError del módulo nuevo). Si falla por un error de sintaxis de la prueba, corrígelo.
5. Entrega la matriz:

| Criterio | Prueba | Estado en rojo |
| --- | --- | --- |
| CA1 | test_ca1_... | falla: 404 |

## Pruebas que no sirven (no las escribas)
- Sin `assert`, o con `assert True`.
- Que solo revisan `len(lista) > 0`.
- Que comparan el resultado con el mismo dato que prepararon sin pasar por la API.
