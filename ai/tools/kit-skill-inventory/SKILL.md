---
name: skill-inventory
description: Audita el sistema de skills instalado. Muestra qué skills están instaladas, cuáles faltan según CLAUDE.md, qué hace cada una y el estado general del sistema. Usar cuando el usuario pregunte por sus skills, qué tiene instalado, o qué le falta.
---

# Skill Inventory — Auditoría del Sistema de Skills

Cuando el usuario invoque esta skill o pregunte por sus skills instaladas, ejecuta esta auditoría completa.

## Flujo

### 1. Leer el estado actual
Ejecuta con Bash:
```bash
ls ~/.claude/skills/ | sort
```

### 2. Comparar contra el inventario de referencia

El inventario canónico viene del CLAUDE.md del usuario. Estas son las skills esperadas:

#### Skills Locales (PalferIA)
| Slug esperado | Descripción |
|---|---|
| `kit-web-scrolling` | Crea webs premium con animaciones de scroll |
| `kit-instagram-web` | Convierte Instagram en web de marca personal |
| `kit-auditoria-seo` | Auditoría SEO completa con informe HTML |
| `kit-dashboard-facturas` | Lee PDFs de facturas y genera dashboard financiero |
| `kit-automatizaciones-n8n` | Crea workflows n8n directamente o como JSON |
| `kit-prospeccion` | Busca y puntúa clientes potenciales por sector/ciudad |
| `kit-auditoria-negocio` | Auditoría de presencia digital completa |
| `kit-auditoria-meta-ads` | Audita anuncios Meta Ads y landing pages |
| `kit-extension-chrome` | Crea extensiones Chrome con Manifest V3 |
| `kit-skill-creator` | Crea nuevas skills para Claude Code |

#### Skills Remotas (ecosistema)
| Slug esperado | Descripción |
|---|---|
| `gestor-autonomos` | IVA, IRPF, facturas para autónomos en España |
| `find-skills` | Descubre e instala skills del ecosistema |
| `skill-creator` | Creador de skills (versión Anthropic) |
| `mcp-builder` | Construye servidores MCP personalizados |
| `writing-plans` | Planificación antes de ejecutar (obra/superpowers) |
| `subagent-driven-development` | Desarrollo con subagentes especializados |
| `verification-before-completion` | Checklist de verificación antes de entregar |
| `skill-judge` | Evalúa la calidad de una skill |
| `planning-with-files` | Planificación persistente en archivos |

#### Skills n8n (sistema)
| Slug esperado | Descripción |
|---|---|
| `n8n-code-javascript` | JavaScript en nodos Code de n8n |
| `n8n-code-python` | Python en nodos Code de n8n |
| `n8n-expression-syntax` | Sintaxis de expresiones n8n |
| `n8n-mcp-tools-expert` | Herramientas MCP para n8n |
| `n8n-node-configuration` | Configuración de nodos n8n |
| `n8n-validation-expert` | Validación de workflows n8n |
| `n8n-workflow-patterns` | Patrones de arquitectura n8n |

### 3. Generar el informe

Presenta el resultado en este formato:

---

## Estado del Sistema de Skills

**Total instaladas:** X / Y esperadas

### ✅ Instaladas (X)
Lista agrupada por categoría con nombre y descripción breve de cada una.

### ❌ Faltan (X)
Lista de las que están en CLAUDE.md pero no en `~/.claude/skills/`, con el comando para instalarlas.

### ➕ Extra (X) — instaladas pero no en CLAUDE.md
Skills adicionales encontradas que no estaban en el inventario original.

---

### 4. Comandos de instalación para las que faltan

Si hay skills faltantes, mostrar el comando exacto para instalar cada una:

**Gestor autónomos:**
```bash
git clone https://github.com/alexdcd/Mafia-Claude-Skills.git
claude skill add ./Mafia-Claude-Skills/skills/gestor-autonomos
```

**Skills de Anthropic (find-skills, skill-creator, mcp-builder):**
```bash
npx skills add https://github.com/anthropics/skills --skill find-skills
npx skills add https://github.com/anthropics/skills --skill skill-creator
npx skills add https://github.com/anthropics/skills --skill mcp-builder
```

**Skills de obra/superpowers:**
```bash
npx skills add https://github.com/obra/superpowers --skill writing-plans
npx skills add https://github.com/obra/superpowers --skill subagent-driven-development
npx skills add https://github.com/obra/superpowers --skill verification-before-completion
```

**Skill judge:**
```bash
npx skills add https://github.com/softaworks/agent-toolkit --skill skill-judge
```

**Planning with files:**
```bash
npx skills add https://github.com/othmanadi/planning-with-files --skill planning-with-files
```

**Skills locales PalferIA:**
```bash
claude skill add /Users/macbook/Desktop/workspace/skills/kit-[nombre]
```

## Reglas

- Siempre leer `~/.claude/skills/` en tiempo real — nunca asumir el estado
- Un skill puede ser un `.md` o una carpeta con `SKILL.md` dentro — ambos cuentan como instalados
- Si hay skills no reconocidas en el inventario, listarlas como "Extra" sin valoración negativa
- Al final, ofrecer instalar las que faltan si el usuario lo pide
