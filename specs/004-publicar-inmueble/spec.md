# Spec 004 · Publicar un inmueble

## Qué y por qué
La inmobiliaria necesita publicar inmuebles nuevos sin editar el JSON a mano. Por ahora se guardan en memoria mientras el servidor está prendido; la base de datos llega después.

## Criterios de aceptación
- **CA1:** `POST /inmuebles` con un inmueble válido (sin `id`) devuelve 201 y el inmueble con `id` 9.
- **CA2:** Después de publicarlo, `GET /inmuebles/9` lo devuelve y `GET /inmuebles` trae 9 inmuebles.
- **CA3:** Si `precio` es 0 o negativo, responde 422.
- **CA4:** Si `tipo` no es casa, apartamento o local, responde 422.
- **CA5:** Si `titulo` tiene menos de 5 caracteres, responde 422.
- **CA6:** Si falta un campo obligatorio (por ejemplo `ciudad`), responde 422.

## Fuera de alcance
Guardar en el archivo o en base de datos, login de la inmobiliaria, editar y borrar.
