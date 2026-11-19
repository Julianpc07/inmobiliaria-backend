# inmobiliaria-backend

API de la **Plataforma Inmobiliaria con IA** (proyecto del Diplomado en Ingeniería de Software con IA y Sistemas Agénticos, FET).

Autor: Julián Andrés Pobre Campuzano

## Stack

Python · FastAPI · Pydantic · pytest · uv

## Sistema de agentes (Claude Code)

Este repositorio tiene su propio sistema de agentes en `.claude/agents/`:

| Agente | Rol | Modelo | Puede editar |
| --- | --- | --- | --- |
| `orquestador-api` | Coordina, arma el plan y delega. No escribe código | sonnet | nada |
| `probador-api` | Escribe las pruebas primero (Red) | sonnet | `tests/**` |
| `desarrollador-api` | Código mínimo para que pasen (Green) y refactor | sonnet | `app/**` |
| `revisor-api` | Revisa diff, cobertura y mutación antes del PR | opus | nada |

Cómo se inicia:

```
set CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH=1
claude --agent orquestador-api
```

Los límites de carpetas no dependen solo del texto del agente: cada subagente tiene un hook `PreToolUse` (`.claude/hooks/limitar_rutas.py`) que rechaza cualquier Edit o Write fuera de sus rutas, y `.claude/settings.json` prohíbe `git commit`, `git push` y `pip/uv add` a todos los agentes. Los commits y el PR los hago yo.

## Estado

Por ahora el repositorio tiene la configuración de los agentes, `CLAUDE.md` y el CI. El código de la API (`app/`) y las pruebas (`tests/`) se van a ir construyendo con este mismo flujo.
