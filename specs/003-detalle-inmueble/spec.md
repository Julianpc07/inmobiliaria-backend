# Spec 003 · Detalle de un inmueble

## Qué y por qué
Cuando el visitante da clic en un inmueble del catálogo, el frontend necesita pedir solo ese inmueble por su id.

## Criterios de aceptación
- **CA1:** `GET /inmuebles/4` devuelve 200 y el inmueble con `titulo` «Casa campestre en vía a Rivera».
- **CA2:** `GET /inmuebles/99` devuelve 404 con `{"detail": "Inmueble no encontrado"}`.
- **CA3:** `GET /inmuebles/abc` devuelve 422.

## Fuera de alcance
Fotos del inmueble e inmuebles relacionados.
