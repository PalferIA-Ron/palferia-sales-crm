---
name: crear-skill
description: Crea skills personalizadas para Claude Code. Genera el archivo .md con instrucciones completas y opcionalmente un kit completo (CLAUDE.md + INSTRUCCIONES.md + SKILL.md) listo para compartir.
version: 1.0.0
author: PalferIA
---

# Creador de Skills para Claude Code

Diseña y genera skills personalizadas para Claude Code siguiendo los 10 principios de una buena skill.

## Qué es una skill

Una skill es un archivo `.md` que le enseña a Claude a ejecutar una tarea específica de forma repetible y consistente. Es como un "modo experto" activable para procesos concretos.

## Flujo

### 1. Entender el proceso a automatizar
Preguntar:
- ¿Qué proceso quieres que Claude ejecute de forma repetible?
- ¿Qué datos necesita para empezar? (URL, archivos, texto, parámetros)
- ¿Qué produce al terminar? (archivo, código, informe, acción)
- ¿Hay pasos que se repiten siempre? ¿Cuáles varían?
- ¿Necesita herramientas externas? (WebFetch, Node.js, APIs)

### 2. Diseñar la skill aplicando los 10 principios

1. **No inventa datos** — pregunta lo que necesita, no asume
2. **Obtiene datos automáticamente** cuando puede (WebFetch, WebSearch, Read)
3. **Auto-instala dependencias** si las necesita (verifica Node.js, instala paquetes)
4. **Libertad creativa** en diseño visual — no CSS rígido predefinido
5. **Se adapta al contexto** del usuario (sector, tamaño, nivel técnico)
6. **Flujo conversacional** — no es un interrogatorio, hace preguntas naturales
7. **Fallbacks amigables** — si algo falla, tiene alternativa y lo comunica
8. **Mensaje de bienvenida claro** en el CLAUDE.md del kit
9. **Sin precios sugeridos** ni consejos de venta no pedidos
10. **Resumen claro** de lo generado al terminar

### 3. Estructura del archivo SKILL.md

```markdown
---
name: nombre-skill
description: Descripción de una línea de qué hace y qué produce.
version: 1.0.0
author: [autor]
---

# Título de la Skill

Descripción breve de cuándo y cómo se activa.

## Datos que necesitas recopilar
[Qué pedir al usuario]

## Flujo
[Pasos numerados y claros]

## Formato de salida
[Qué produce: HTML, JSON, código, archivo...]

## Reglas
[Restricciones y comportamientos obligatorios]
```

### 4. Generar los archivos

**Mínimo obligatorio:**
- `[nombre-skill].md` — la skill completa

**Kit completo (si el usuario lo pide o si tiene sentido compartirla):**
- `kit-[nombre]/CLAUDE.md` — comportamiento al abrir el kit, mensaje de bienvenida
- `kit-[nombre]/INSTRUCCIONES.md` — guía para el usuario final
- `kit-[nombre]/SKILL.md` — la skill para instalar en la versión web

### 5. Revisar antes de entregar

Checklist:
- [ ] El flujo cubre el 100% del proceso sin pasos a medias
- [ ] Hay fallback para los casos donde algo puede fallar
- [ ] El formato de salida está bien definido
- [ ] No inventa datos en ningún paso
- [ ] Los 10 principios están respetados

## Reglas

- Una skill debe poder ejecutarse sin instrucciones adicionales del usuario — es autocontenida
- Si la skill es muy compleja, dividirla en sub-skills con responsabilidades claras
- Siempre generar la skill completa, no un borrador
