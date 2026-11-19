---
paths:
  - "tests/**/*.py"
---

# Reglas para las pruebas

- Cada prueba lleva en el nombre el criterio que verifica: `test_ca1_lista_todos_los_inmuebles`.
- Se prueba contra la API real con `TestClient(app)`. No se simula el repositorio.
- Toda prueba tiene al menos un `assert` sobre el resultado (código de estado y contenido), no solo sobre el largo de la lista.
- Siempre hay un caso de error (404 o 422) cuando la spec lo menciona.
- Las pruebas que cambian datos (POST) usan la fixture que reinicia el repositorio, para que no dependan del orden.
