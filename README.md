# inmobiliaria-backend

API de la **Plataforma Inmobiliaria con IA**, el proyecto integrador del Diplomado en Ingeniería de Software con IA y Sistemas Agénticos (FET).

**Autor:** Julián Andrés Pobre Campuzano (trabajo individual)
**Herramienta:** Claude Code · **Stack:** Python, FastAPI, Pydantic, pytest, uv
**Frontend:** [inmobiliaria-frontend](https://github.com/Julianpc07/inmobiliaria-frontend)

```
uv sync
uv run pytest
uv run uvicorn app.main:app --reload   # http://localhost:8000/docs
```

## El arnés

| Pieza | Dónde está | Qué hace |
| --- | --- | --- |
| Memoria | [`CLAUDE.md`](CLAUDE.md) | Comandos, capas, convenciones y lo que el agente no debe hacer. Claude Code lo lee al iniciar cada sesión. |
| Rules | [`.claude/rules/`](.claude/rules) | `pruebas.md` aplica solo a `tests/**` y `codigo-api.md` solo a `app/**`. Se cargan cuando el agente toca esos archivos. |
| Skills | [`.claude/skills/`](.claude/skills) | 4 procedimientos propios (tabla de abajo). |
| Agentes | [`.claude/agents/`](.claude/agents) | Orquestador + 3 subagentes, cada uno con sus herramientas, permisos y modelo. |
| Permisos | [`.claude/settings.json`](.claude/settings.json) | Comandos permitidos y prohibidos para todos los agentes (`git commit`, `git push`, `uv add`). |
| Hook | [`.claude/hooks/limitar_rutas.py`](.claude/hooks/limitar_rutas.py) | Rechaza cualquier Edit o Write fuera de las carpetas del agente. |
| Specs | [`specs/`](specs) | Las 4 specs del backend con spec, plan y tareas. |
| CI | [`.github/workflows/ci.yml`](.github/workflows/ci.yml) | Pruebas con cobertura mínima de 80 % en cada PR, y mutación informativa. |

No uso Spec Kit, así que no hay `constitution.md`: los principios no negociables están en la sección «Lo que el agente NO debe hacer» de `CLAUDE.md`.

### Skills

| Skill | Qué problema resuelve | Cuándo se invoca | La usa |
| --- | --- | --- | --- |
| [`nueva-spec`](.claude/skills/nueva-spec/SKILL.md) | Que todas las specs tengan la misma estructura y criterios verificables | Al empezar una funcionalidad nueva | Julián / orquestador-api |
| [`criterios-a-pruebas`](.claude/skills/criterios-a-pruebas/SKILL.md) | Que cada criterio de aceptación termine en una prueba real, con su matriz, y que las pruebas fallen por el motivo correcto | Paso Red de cada spec | probador-api |
| [`endpoint-fastapi`](.claude/skills/endpoint-fastapi/SKILL.md) | Que los endpoints respeten las capas router → repository → models y se prueben con curl | Paso Green | desarrollador-api |
| [`revision-pr`](.claude/skills/revision-pr/SKILL.md) | Que la revisión siempre mire lo mismo y deje hallazgos con el mismo formato para pegarlos en el PR | Antes de abrir el PR | revisor-api |

Las tres últimas se precargan en el subagente con el campo `skills:` de su archivo, así no dependen de que el modelo decida cargarlas.

## Sistema de agentes

| Agente | Rol | Modelo | Puede editar | Comandos |
| --- | --- | --- | --- | --- |
| [`orquestador-api`](.claude/agents/orquestador-api.md) | Lee la spec, hace aprobar el plan y delega. No escribe código | sonnet | nada | ninguno |
| [`probador-api`](.claude/agents/probador-api.md) | Pruebas primero (Red) | sonnet | `tests/**` | `uv run pytest` |
| [`desarrollador-api`](.claude/agents/desarrollador-api.md) | Código hasta verde (Green) | sonnet | `app/**` y casillas de `tasks.md` | pytest, uvicorn, curl a localhost |
| [`revisor-api`](.claude/agents/revisor-api.md) | Revisión antes del PR | opus | nada | git diff, pytest --cov |

### Cómo se usa (una spec)

```
git checkout -b 00N-nombre
claude --agent orquestador-api
> Implementa la spec specs/00N-nombre
```

1. El orquestador muestra el plan y espera que yo escriba **aprobado**.
2. `probador-api` escribe las pruebas y muestra que fallan → yo hago `git commit -m "test(00N): pruebas en rojo"`.
3. `desarrollador-api` escribe el código hasta que pasan y lo prueba con curl → `git commit -m "feat(00N): ..."`.
4. `revisor-api` revisa y da APROBADO o CAMBIOS. Si hay CRÍTICO o ALTO, vuelve al rol que corresponde (máximo 2 vueltas).
5. Abro el PR, pego el informe del revisor como comentario, espero el CI en verde y lo fusiono en main.

`CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1` (en `settings.json`) impide que un subagente cree otros.

### Qué cambió respecto del taller y por qué

| Cambio | Antes (taller) | Ahora | Por qué |
| --- | --- | --- | --- |
| Mutación | `revisor-api` corría `mutmut` | `mutmut` corre en el CI (Linux), informativo | mutmut 3 no funciona en Windows nativo, que es donde trabajo |
| Pausas para commit | El orquestador iba de Red a Green directo | Se detiene después de cada paso para que yo haga el commit | Así el TDD queda visible en el historial (commit de pruebas antes que el de código), y los agentes siguen sin poder hacer commit |
| `permissionMode: plan` | En el orquestador | Lo quité | En modo plan el orquestador no puede delegar hasta salir del modo. Ahora el plan se aprueba escribiendo «aprobado» |
| Skills precargadas | No estaban | Campo `skills:` en probador, desarrollador y revisor | Que cada subagente arranque con su procedimiento sin tener que buscarlo |
| `tasks.md` | Nadie podía marcar las tareas | `desarrollador-api` puede editar solo `specs/*/tasks.md` | Las tareas tienen que quedar marcadas como completadas |
| Comando del hook | `python ...` | `uv run python ...` | En mi PC Python está instalado con uv y `python` solo no siempre está en el PATH |

## Las specs (SDD)

Cada spec está en `specs/NNN-nombre/` con `spec.md` (qué y por qué, criterios de aceptación), `plan.md` (decisiones y archivos) y `tasks.md` (tareas marcadas). Cada una tiene su rama y su PR.

| Spec | Qué hace | PR |
| --- | --- | --- |
| [001](specs/001-listar-inmuebles/spec.md) | `GET /inmuebles` y CORS para el frontend | [PRs](https://github.com/Julianpc07/inmobiliaria-backend/pulls?q=is%3Apr) |
| [002](specs/002-filtrar-inmuebles/spec.md) | Filtros por tipo, operación, ciudad y precio | ↑ |
| [003](specs/003-detalle-inmueble/spec.md) | `GET /inmuebles/{id}` con 404 | ↑ |
| [004](specs/004-publicar-inmueble/spec.md) | `POST /inmuebles` con validaciones | ↑ |
| [005](https://github.com/Julianpc07/inmobiliaria-frontend/tree/main/specs/005-catalogo-inmuebles) | Catálogo en el frontend | en el repo del frontend |

## Calidad del código escrito por la IA

| Mecanismo | Cómo funciona | Evidencia |
| --- | --- | --- |
| 1. CI con cobertura mínima | Cada PR corre `pytest --cov-fail-under=80`. Si baja de 80 %, el PR queda en rojo | [GitHub Actions](https://github.com/Julianpc07/inmobiliaria-backend/actions) |
| 2. TDD visible | Las pruebas se escriben y se suben antes que el código | En cada PR, el commit `test(00N)` va antes del `feat(00N)` |
| 3. Revisión del revisor-api | Hallazgos con severidad y veredicto antes del PR | Comentario con el informe en cada [PR](https://github.com/Julianpc07/inmobiliaria-backend/pulls?q=is%3Apr) |
| 4. Permisos reales | El hook impide que el desarrollador cambie pruebas y `settings.json` prohíbe commit y push | `.claude/hooks/` y `.claude/settings.json` |
| 5. Mutación (informativa) | `mutmut` sobre `app/` en el CI | Artefacto `informe-mutmut` de cada ejecución en Actions |
