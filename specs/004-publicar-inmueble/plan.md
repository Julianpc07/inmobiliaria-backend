# Plan 004 · Publicar un inmueble

## Decisiones técnicas
- Modelo `InmuebleNuevo` (sin `id`) con `precio: int = Field(gt=0)`, `titulo: str = Field(min_length=5)` y `habitaciones`, `banos`, `area_m2` ≥ 0. `Inmueble` hereda de él y agrega `id`.
- `repository.crear(nuevo)` asigna `id = máximo actual + 1` y lo agrega a la lista en memoria. No escribe el JSON.
- `repository.reiniciar()` vuelve a cargar el JSON. Las pruebas lo usan en una fixture de `tests/conftest.py` para no depender del orden.

## Archivos que se tocan
| Archivo | Cambio |
| --- | --- |
| `app/models.py` | `InmuebleNuevo` y validaciones |
| `app/repository.py` | `crear()` y `reiniciar()` |
| `app/routers/inmuebles.py` | `POST /inmuebles` con `status_code=201` |
| `tests/conftest.py` | fixture que reinicia el repositorio |
| `tests/test_004_publicar.py` | nuevo |

## Pruebas
| Criterio | Prueba |
| --- | --- |
| CA1 | `test_ca1_publica_y_asigna_id_9` |
| CA2 | `test_ca2_el_publicado_aparece_en_detalle_y_lista` |
| CA3 | `test_ca3_precio_cero_o_negativo_422` |
| CA4 | `test_ca4_tipo_invalido_422` |
| CA5 | `test_ca5_titulo_corto_422` |
| CA6 | `test_ca6_falta_campo_422` |
