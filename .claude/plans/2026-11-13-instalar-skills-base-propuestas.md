# 13 nov 2026 · Instalar las skills y fijar la base de la app de propuestas

## Lo que pidió Ron
Mirar las carpetas de skills, instalarlas todas, usarlas en la propuesta de Neil
y en todas las siguientes. Que sean la base consistente de la app de propuestas
en HTML. Y proponer alguna nueva para probar.

## Lo que encontré

Tres copias de las mismas skills:

| Carpeta | Qué tiene |
|---|---|
| `Palferia-Holding/skills/` | 17 carpetas, 16 con `SKILL.md` válido. **Canónica** |
| `palferia-sales-crm/clientes/skill proyecto/` | 14, de las cuales 7 son copia byte a byte de la anterior |
| `Palferia-Holding/skills-web/` | zips y duplicados, más 4 únicas |

`~/.claude/skills/` solo tenía `ui-ux-pro-max-skill`. **Ninguna de las skills de
PalferIA estaba instalada**, aunque los CLAUDE.md las dan por activas.

## Decisiones

1. **Origen único: `Palferia-Holding/skills/`.** Las 7 duplicadas de `skill proyecto`
   son idénticas, así que no se pierde nada.
2. **Copia, no enlace simbólico.** No puedo verificar aquí que el cargador de skills
   atraviese symlinks, y una skill que no carga en silencio es peor que una copia.
   Se resincroniza con un script.
3. **`kit-agency-agents` son agentes, no skills** (207, licencia MIT). Van a
   `~/.claude/agents/` y solo un subconjunto: 207 en la lista es ruido.
4. **Fuera por licencia**, igual que Divisual:
   - `kit-estudio-video-ia` — sin licencia
   - `whatsapp-ai-agent-kit` — trae la guía de Divisual dentro
   - `divisual-video-editor-kit`
5. **Las 7 skills del Avatar Studio se quedan en su proyecto.** Sus rutas son
   relativas al kit (`docs/`, `prompts/`); instalarlas global las rompe.

## Lo que construyo

- `kit-propuestas-html` — **la base de la app.** Destila lo que ya funciona en
  Tecniluispa y No Limits: los dos formatos, la paleta, el arco de secciones, el
  formulario, dónde se publica y la lista de comprobación antes de enviar.
- `kit-formularios-sheets` — el patrón Apps Script + Sheets + aviso a
  `ri@palferia.com`, que ya va por su tercera vez escrito a mano.
- Aplicar las dos a la propuesta de Neil.

## Pendiente de Ron
- Instalar el Apps Script de No Limits y pegar la URL.
