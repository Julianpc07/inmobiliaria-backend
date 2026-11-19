# Plan 001 · Listar inmuebles

## Decisiones técnicas
- `app/repository.py` carga `data/inmuebles.json` una vez en una lista en memoria y la expone con `listar()`.
- Modelo `Inmueble` en `app/models.py` con `tipo: Literal["casa","apartamento","local"]` y `operacion: Literal["venta","arriendo"]`.
- `CORSMiddleware` en `main.py` solo para `http://localhost:5173`.

## Archivos que se tocan
| Archivo | Cambio |
| --- | --- |
| `app/models.py` | nuevo: modelo `Inmueble` |
| `app/repository.py` | nuevo: carga del JSON y `listar()` |
| `app/routers/inmuebles.py` | nuevo: `GET /inmuebles` |
| `app/main.py` | nuevo: app, CORS e include del router |
| `tests/test_001_listar.py` | nuevo |

## Pruebas
| Criterio | Prueba |
| --- | --- |
| CA1 | `test_ca1_lista_los_8_inmuebles` |
| CA2 | `test_ca2_cada_inmueble_tiene_todos_los_campos` |
| CA3 | `test_ca3_ordenados_por_id` |
| CA4 | `test_ca4_cors_para_el_frontend` |
