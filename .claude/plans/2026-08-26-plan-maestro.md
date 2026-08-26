# Palferia Sales CRM — Plan Maestro
**Fecha:** 2026-08-26
**Basado en:** Arquitectura DraftDayES + estado actual del MVP

---

## SÍNTESIS DEL NEGOCIO

### El problema que resuelve
Ronald vende servicios de IA aplicada al deporte (COM-studio y ME-sport). El proceso comercial es manual: prospectos por WhatsApp, propuestas en Word, seguimiento por memoria. Sin sistema → oportunidades perdidas, lentitud, imposible escalar.

### La solución
Un CRM ligero, rápido y altamente automatizado con IA, diseñado para una agencia de 1 persona que necesita trabajar como si fueran 5.

### El posicionamiento operacional
> Palferia Sales CRM = el sistema nervioso comercial de Palferia.me

---

## FASES DE EVOLUCIÓN

### FASE 0 — Fundamentos (COMPLETADA ✅)
**Objetivo:** MVP funcional en producción
- CRM con CRUD de prospectos (tabla + kanban)
- Login via Supabase
- WhatsApp integration (lectura)
- Pipeline log
- Deploy automático GitHub → VPS
- 22 skills de IA disponibles

---

### FASE 1 — Consolidación (ACTUAL — 2026-08-26 → 2026-09)
**Objetivo:** Cerrar los gaps críticos del MVP y establecer fundamentos de calidad

#### 1.1 Arquitectura Claude
- [x] CLAUDE.md — identidad, stack, principios
- [x] Bitácora — historial de sesiones
- [x] Plan Maestro — este documento
- [x] Reorganización skills → `ai/`
- [x] ESLint + Prettier

#### 1.2 Seguridad básica
- [ ] API keys fuera del HTML (inyección desde VPS via Nginx o script)
- [ ] DOMPurify para sanitizar inputs antes de `.innerHTML`
- [ ] Auditoría de endpoints OpenWA expuestos

#### 1.3 Features pendientes MVP
- [ ] Envío de mensajes WhatsApp desde CRM (actualmente solo lectura)
- [ ] Notificaciones tiempo real de mensajes entrantes (polling o WebSocket)
- [ ] Conexión kit-prospeccion → inserción automática en Supabase
- [ ] Modal "nueva propuesta" completo y funcional
- [ ] Búsqueda global en tabla de prospectos

---

### FASE 2 — Automatización (2026-09 → 2026-10)
**Objetivo:** Que el CRM trabaje solo mientras Ronald cierra clientes

#### 2.1 Pipeline automático
- [ ] Trigger n8n: prospecto nuevo → mensaje WhatsApp de bienvenida automático
- [ ] Trigger n8n: propuesta enviada → recordatorio automático a los 3 días
- [ ] Score automático basado en actividad (último contacto, respuestas WA, estado)
- [ ] Alertas: prospectos sin actividad >7 días → notificación

#### 2.2 Prospección automática
- [ ] kit-prospeccion → scraping → inserción directa en Supabase
- [ ] kit-instagram-web → extracción de prospectos desde Instagram → BD
- [ ] Deduplicación automática por teléfono/email

#### 2.3 Propuestas automatizadas
- [ ] Orquestador de propuestas: auditoría web → propuesta personalizada en 1 clic
- [ ] Envío automático de propuesta por WhatsApp con tracking de apertura
- [ ] Templates por sector (academias, clubes, eventos, federaciones)

#### 2.4 Dashboard e inteligencia
- [ ] Métricas de pipeline: tasa conversión por proyecto, tiempo medio de cierre
- [ ] Embudo de ventas visual
- [ ] Actividad reciente en home del CRM

---

### FASE 3 — Calidad técnica (2026-10 → 2026-11)
**Objetivo:** Hacer el código mantenible sin romper lo que funciona

#### 3.1 Modularización de crm.html
Separar el monolito de ~2.600 líneas en módulos JS independientes:
```
public/
├── js/
│   ├── core/
│   │   ├── supabase.js       — cliente y auth
│   │   ├── router.js         — navegación entre secciones
│   │   └── ui.js             — toast, modales, helpers DOM
│   ├── modules/
│   │   ├── prospectos.js     — CRUD, kanban, filtros
│   │   ├── whatsapp.js       — sesiones, chat, envío
│   │   ├── propuestas.js     — generación, tracking
│   │   └── pipeline.js       — log, auditoría
│   └── main.js               — init y routing
├── css/
│   └── crm.css               — estilos extraídos
└── crm.html                  — solo estructura HTML + imports
```

#### 3.2 TypeScript (opcional, solo si hay tiempo)
- Migrar módulos JS a TypeScript
- Interfaces para Prospecto, Propuesta, MensajeWA, PipelineLog
- Compilación con tsc (sin bundler — output directo a public/)

#### 3.3 Testing básico
- Tests de las funciones críticas (loadProspectos, createWASession, renderKanban)
- Jest + jsdom para vanilla JS

---

### FASE 4 — Escalabilidad (2026-11+)
**Objetivo:** Preparar para multi-usuario y posible SaaS interno

#### 4.1 Multi-usuario
- Sistema de roles (admin, sales, viewer) vía Supabase Auth + RLS policies
- Audit trail: quién modificó cada prospecto y cuándo

#### 4.2 Backend API (si es necesario)
- Evaluar si el volumen de datos justifica una API propia (NestJS ligero)
- Alternativa: Supabase Edge Functions para lógica compleja

#### 4.3 Observabilidad
- Sentry para captura de errores en producción
- Logs de acciones comerciales (propuestas vistas, mensajes enviados)

---

## ARQUITECTURA TÉCNICA (DECISIONES VIGENTES)

### Principio guía
**Vanilla JS primero.** No añadir frameworks hasta que el pain de no tenerlos sea real y medible. La velocidad de desarrollo > la elegancia técnica en esta fase.

### Base de datos
```
prospectos          — núcleo del CRM (nombre, estado, score, proyecto, contacto)
pipeline_log        — auditoría de acciones
mensajes_whatsapp   — historial de conversaciones
propuestas          — propuestas generadas y su estado
```

### Capas de la aplicación
```
Browser (HTML + CSS + Vanilla JS)
    ↕ Supabase JS SDK v2
Supabase (PostgreSQL + RLS + Auth)
    ↕ API REST / Webhooks
n8n (automatizaciones)
    ↕ Webhooks
OpenWA (WhatsApp — VPS:2785)
    ↕ Proxy Nginx (/wa/)
VPS Linux (31.97.192.164)
```

### Deploy
```
GitHub (push main) → GitHub Actions → rsync → VPS → sales.palferia.me
```

---

## DOMINIOS Y RESPONSABILIDADES

| Dominio | Archivo principal | Estado |
|---------|------------------|--------|
| `prospectos` | `public/crm.html` (sección prospectos) | ✅ Estable |
| `whatsapp` | `public/crm.html` (sección WA) | ⚠️ Solo lectura |
| `propuestas` | `public/crm.html` + `public/propuestas/*.html` | ⚠️ Manual |
| `pipeline` | `public/crm.html` (sección log) | ✅ Estable |
| `ai/agents` | `ai/agents/` | ✅ Disponible |
| `ai/workflows` | `ai/workflows/` + n8n | ⚠️ Parcial |
| `ai/prompts` | `ai/prompts/` | ✅ Disponible |
| `ai/auditorias` | `ai/auditorias/` | ✅ Disponible |

---

## MÉTRICAS DE ÉXITO

### Fase 1 (Sept 2026)
- [ ] 0 API keys en HTML
- [ ] WhatsApp: envío funcional desde CRM
- [ ] kit-prospeccion → Supabase: integración completa
- [ ] <5 min de setup para nueva sesión de trabajo

### Fase 2 (Oct 2026)
- [ ] >50% de prospectos nuevos llegan automáticamente (sin entrada manual)
- [ ] Propuesta generada en <10 min desde auditoría
- [ ] Score automático activo para todos los prospectos

### Fase 3 (Nov 2026)
- [ ] crm.html separado en módulos (ningún archivo >500 líneas)
- [ ] 0 vulnerabilidades XSS conocidas
- [ ] Tiempo de carga del CRM <2s en 3G
