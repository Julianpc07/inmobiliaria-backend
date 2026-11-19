# Plan 003 · Detalle de un inmueble

## Decisiones técnicas
- `GET /inmuebles/{id}` con `id: int`, así FastAPI responde 422 si no es número (CA3).
- `repository.obtener(id)` devuelve el `Inmueble` o `None`; el router convierte `None` en 404.

## Archivos que se tocan
| Archivo | Cambio |
| --- | --- |
| `app/repository.py` | nueva función `obtener(id)` |
| `app/routers/inmuebles.py` | nueva ruta `GET /inmuebles/{id}` |
| `tests/test_003_detalle.py` | nuevo |

## Pruebas
| Criterio | Prueba |
| --- | --- |
| CA1 | `test_ca1_detalle_de_un_inmueble_existente` |
| CA2 | `test_ca2_id_inexistente_404` |
| CA3 | `test_ca3_id_no_numerico_422` |
