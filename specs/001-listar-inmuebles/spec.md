# Spec 001 · Listar inmuebles

## Qué y por qué
Los visitantes necesitan ver todos los inmuebles que tiene la inmobiliaria. Es la base del catálogo del frontend, así que también hay que dejar habilitado el CORS para que el frontend (http://localhost:5173) pueda llamar a la API.

## Criterios de aceptación
- **CA1:** Dado que hay 8 inmuebles en `data/inmuebles.json`, cuando hago `GET /inmuebles`, entonces recibo 200 y una lista con 8 inmuebles.
- **CA2:** Cada inmueble trae `id`, `titulo`, `tipo`, `operacion`, `ciudad`, `precio`, `habitaciones`, `banos` y `area_m2`.
- **CA3:** La lista viene ordenada por `id` de menor a mayor.
- **CA4:** Cuando la petición viene con el encabezado `Origin: http://localhost:5173`, la respuesta trae `access-control-allow-origin: http://localhost:5173`.

## Fuera de alcance
Filtros (spec 002), paginación y base de datos.
