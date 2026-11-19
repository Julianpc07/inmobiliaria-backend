---
name: nueva-spec
description: Crea la carpeta de una spec nueva (specs/NNN-nombre) con spec.md, plan.md y tasks.md siguiendo la plantilla del proyecto. Úsala cuando Julián pida empezar una funcionalidad nueva.
---

# Nueva spec

1. Mira el último número en `specs/` y usa el siguiente (001, 002...).
2. Crea `specs/NNN-nombre-corto/` con tres archivos:

**spec.md**
```
# Spec NNN · Título
## Qué y por qué
(1 o 2 párrafos: qué necesita el usuario y para qué)
## Criterios de aceptación
- CA1: Dado ..., cuando ..., entonces ...
## Fuera de alcance
```

**plan.md**
```
# Plan NNN
## Decisiones técnicas
## Archivos que se tocan
| Archivo | Cambio |
## Pruebas
| Criterio | Prueba |
```

**tasks.md**
```
# Tareas NNN
- [ ] T1 Pruebas en rojo (probador)
- [ ] T2 ...
- [ ] Tn Revisión (revisor)
```
3. Los criterios tienen que ser verificables: un código de estado, un campo, un número. Nada de «que funcione bien».
4. No escribas código. La spec la aprueba Julián antes de pasar al orquestador.
