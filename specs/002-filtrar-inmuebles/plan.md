# Plan 002 · Filtrar inmuebles

## Decisiones técnicas
- Los filtros son parámetros `Query` opcionales del mismo `GET /inmuebles` (no un endpoint nuevo), así el frontend usa una sola función.
- `tipo` y `operacion` con `Literal`, para que FastAPI devuelva 422 solo (CA7).
- El filtrado lo hace `repository.buscar(tipo, operacion, ciudad, precio_min, precio_max)`. `listar()` queda como `buscar()` sin filtros.
- CA8 se valida en el router con `HTTPException(422)` porque depende de dos parámetros.

## Archivos que se tocan
| Archivo | Cambio |
| --- | --- |
| `app/repository.py` | nueva función `buscar(...)` |
| `app/routers/inmuebles.py` | parámetros `Query` y validación de precios |
| `tests/test_002_filtrar.py` | nuevo |

## Pruebas
| Criterio | Prueba |
| --- | --- |
| CA1 | `test_ca1_filtra_por_tipo` |
| CA2 | `test_ca2_filtra_por_operacion` |
| CA3 | `test_ca3_ciudad_sin_importar_mayusculas` |
| CA4 | `test_ca4_rango_de_precio_incluye_limites` |
| CA5 | `test_ca5_combina_filtros` |
| CA6 | `test_ca6_sin_resultados_lista_vacia` |
| CA7 | `test_ca7_tipo_invalido_422` |
| CA8 | `test_ca8_precio_min_mayor_que_max_422` |
