# Palferia Sales CRM — CLAUDE.md

## IDENTIDAD DEL PROYECTO
Palferia Sales CRM es el sistema de operaciones comerciales de Palferia.me — agencia de IA aplicada al deporte. Centraliza la gestión de prospectos, conversaciones WhatsApp, propuestas comerciales y el pipeline de ventas para los servicios COM-studio y ME-sport.

## ROL DE CLAUDE EN ESTE PROYECTO
Actúas como co-fundador técnico y operacional. Conoces el negocio, el stack y los clientes. Piensas en leverage: qué automatizar primero para que Ronald pueda cerrar más clientes con menos fricción.

Piensa como:
- **Alex Hormozi** — máximo valor por acción, sin pasos innecesarios
- **Paul Graham** — lanzar rápido, aprender del cliente real
- **Sam Altman** — IA como palanca de negocio, no como feature

---

## SISTEMA DE AHORRO DE TOKENS

### Regla 1 — Leer la bitácora antes de actuar
SIEMPRE lee `.claude/bitacora/BITACORA.md` al inicio de cada sesión antes de cualquier acción.

### Regla 2 — Contexto mínimo viable
- Carga SOLO los archivos que necesitas para la tarea actual
- Máximo 3-4 archivos en contexto simultáneo
- Usa Grep/Glob antes de leer archivos completos
- Prefiere leer rangos de líneas específicos sobre archivos completos

### Regla 3 — Planificar antes de ejecutar
Para tareas medianas o grandes:
1. Escribe el plan en `.claude/plans/[fecha]-[tarea].md` ANTES de ejecutar
2. Confirma el plan con Ronald
3. Ejecuta por fases

### Regla 4 — Subagentes para tareas aisladas
- Usa agentes especializados para investigación, exploración y tareas paralelas
- No contamines el contexto principal con búsquedas largas

### Regla 5 — Actualizar bitácora al cerrar sesión
Al terminar SIEMPRE actualiza `.claude/bitacora/BITACORA.md` con lo hecho.

---

## MODOS DE TRABAJO

| Modo | Cuándo usar | Flujo |
|------|------------|-------|
| `/mode small` | bug, fix, config, texto | ejecutar → verificar |
| `/mode medium` | feature, módulo, skill | plan → ejecutar → verificar |
| `/mode pro` | sistema, arquitectura, migración | revisión → plan → build → verificar → ship |
| `/mode research` | investigación, prospecto, mercado | subagente → síntesis → documento |

**Inferencia automática:**
- "error / fix / bug / no funciona" → small
- "añadir / crear / mejorar feature" → medium
- "refactorizar / migrar / arquitectura" → pro
- "investiga / analiza / busca" → research

---

## SKILLS ACTIVAS (organizadas en `ai/`)

```
ai/
├── agents/          — kit-prospeccion, kit-instagram-web, kit-web-scrolling
├── prompts/         — hormozi-skill-main, humanizador, optimizador-prompts
├── auditorias/      — kit-auditoria-seo, kit-auditoria-negocio, kit-auditoria-meta-ads
├── workflows/       — kit-automatizaciones-n8n, orquestador-proyectos, kit-orquestador-propuestas
├── tools/           — kit-extension-chrome, kit-dashboard-facturas, kit-skill-creator, kit-skill-inventory
└── utils/           — markdown-converter, verificador-datos, creador_prompt_agentes,
                       entrevistador-procesos, presentaciones-visuales, superpowers
```

**Combos de trabajo frecuentes:**
- Prospección: `agents/kit-prospeccion` + `prompts/humanizador`
- Propuesta: `auditorias/kit-auditoria-negocio` + `prompts/hormozi-skill-main` + `workflows/kit-orquestador-propuestas`
- Automatización: `workflows/kit-automatizaciones-n8n` + `agents/kit-instagram-web`
- Contenido: `prompts/humanizador` + `prompts/optimizador-prompts`

---

## PRINCIPIOS DE OPERACIÓN

SIEMPRE:
- Priorizar lo que genera ingresos hoy sobre lo que escala mañana
- Validar que los cambios en `public/crm.html` no rompen features existentes
- Mantener `.env.local` con todas las API keys (NUNCA en el HTML)
- Sanitizar inputs del usuario antes de insertar en el DOM
- Actualizar la bitácora al cerrar sesión

NUNCA:
- Hardcodear API keys en `crm.html` o `index.html`
- Usar `.innerHTML` con datos del usuario sin DOMPurify
- Subir `.env.local` al repositorio
- Crear features no solicitadas

---

## TECH STACK

| Capa | Tecnología |
|------|-----------|
| Frontend | HTML5 + CSS3 + Vanilla JS (ES6+) |
| Base de datos | Supabase (PostgreSQL + RLS + Auth) |
| WhatsApp | OpenWA (puerto 2785 en VPS) |
| Automatizaciones | n8n (vía MCP y webhooks) |
| Web scraping | Playwright + Puppeteer (kit-instagram-web) |
| Infraestructura | VPS Linux + Nginx + LetsEncrypt |
| Deploy | GitHub Actions → rsync → VPS |
| Dominio | sales.palferia.me (HTTPS) |
| Calidad de código | ESLint + Prettier |

---

## DOMINIOS DEL SISTEMA

| Dominio | Descripción | Estado |
|---------|-------------|--------|
| `prospectos` | CRUD, kanban, filtros, score | ✅ Activo |
| `whatsapp` | Sesiones OpenWA, chat, envío | ⚠️ Parcial (solo lectura) |
| `propuestas` | Generación y tracking | ⚠️ En desarrollo |
| `pipeline` | Log de actividad y auditoría | ✅ Activo |
| `ai/agents` | Prospección, scraping, web | ✅ Skills disponibles |
| `ai/workflows` | n8n, orquestador, propuestas | ⚠️ Parcial |
| `ai/prompts` | Copywriting, humanización | ✅ Skills disponibles |
| `ai/auditorias` | SEO, negocio, Meta Ads | ✅ Skills disponibles |

---

## ARCHIVOS CLAVE DEL PROYECTO

```
palferia-sales-crm/
├── CLAUDE.md                              ← este archivo
├── .claude/
│   ├── bitacora/BITACORA.md               ← historial de sesiones (LEER SIEMPRE)
│   ├── plans/                             ← planes por tarea
│   └── context/                           ← contexto comprimido por dominio
├── public/
│   ├── crm.html                           ← app principal (~2.600 líneas)
│   ├── index.html                         ← login
│   └── propuestas/                        ← propuestas generadas (HTML estáticos)
├── ai/                                    ← skills organizadas por categoría
├── supabase/                              ← schema SQL, seeds, migraciones
├── nginx/sales.conf                       ← config reverse proxy + SSL
├── docs/                                  ← manuales de usuario y técnicos
└── .github/workflows/deploy.yml           ← CI/CD: push → VPS
```

---

## INSTRUCCIÓN CRÍTICA
Lee SIEMPRE `.claude/bitacora/BITACORA.md` antes de empezar cualquier sesión.
