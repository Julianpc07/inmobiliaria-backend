# Spec 002 · Filtrar inmuebles

## Qué y por qué
Un visitante no quiere ver todo: busca, por ejemplo, un apartamento en arriendo en Neiva que no pase de cierto precio. `GET /inmuebles` debe aceptar filtros opcionales que se pueden combinar.

## Criterios de aceptación
- **CA1:** `GET /inmuebles?tipo=casa` devuelve solo casas: los ids 1, 4 y 6.
- **CA2:** `GET /inmuebles?operacion=arriendo` devuelve los ids 2, 3, 6 y 8.
- **CA3:** `GET /inmuebles?ciudad=neiva` devuelve los ids 1, 2, 3 y 5. La ciudad no distingue mayúsculas.
- **CA4:** `GET /inmuebles?precio_min=1000000&precio_max=2000000` devuelve los ids 2 y 6. Los límites se incluyen.
- **CA5:** Los filtros se combinan: `?tipo=apartamento&operacion=venta` devuelve solo el id 5.
- **CA6:** Si ningún inmueble cumple, la respuesta es 200 con una lista vacía.
- **CA7:** `?tipo=finca` responde 422.
- **CA8:** Si `precio_min` es mayor que `precio_max`, responde 422.

## Fuera de alcance
Búsqueda por texto, ordenar por precio y paginación.
