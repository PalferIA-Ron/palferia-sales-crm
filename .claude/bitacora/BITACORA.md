# Palferia Sales CRM — Bitácora del Proyecto

> Este archivo es la memoria viva del proyecto. Leerlo SIEMPRE al iniciar sesión.

---

## ESTADO ACTUAL
**Fase:** 1 — MVP en producción / Consolidación de arquitectura
**Última sesión:** 2026-09-03
**Próxima acción prioritaria:**
1. Completar integración OpenWA ↔ Chatwoot (ver pasos pendientes abajo)
2. Orquestador de propuestas — añadir bloque 3C DraftDayES + referenciar deliverables en S7
3. Seguimiento Tecniluispa y Cortinajes Valls & París

---

## PENDIENTES ACTIVOS

### CRM / Producto
- [ ] Envío de mensajes WhatsApp desde el CRM (actualmente solo lectura)
- [ ] Botón importación bulk prospectos desde JSON
- [ ] Modal "nueva propuesta" completo y funcional
- [ ] Búsqueda global en tabla de prospectos

### Comercial
- [ ] **29/08** — Seguimiento Tecniluispa: recordatorio suave + pedir referidos de academias
- [ ] **~25/08** — Sensibilizar Cortinajes Valls & París (regresa vacaciones)
- [ ] Contactar 6 nuevos COM-studio semana 2: Orquisato Floristería, Talleres Godella, Academia Oposiciones Valencia, Inmobiliaria Moncada, Baker Street Panadería, Clínica Dental Moncada
- [ ] Llamadas seguimiento ~24/08 si no hay respuesta de los 8 en espera
- [ ] CrossFit Taronja — WhatsApp o llamada fría (es franquicia WodBuster, solo complemento)
- [ ] Pádel Valencia Horta Nord — contactar
- [ ] Identificar 4 prospectos más ME-sport (slots 7–10)

### Infraestructura / Técnico
- [ ] **INBOX — 3 pasos para completar integración OpenWA ↔ Chatwoot:**
  1. Verificar error exacto en logs: `docker logs openwa-api --tail=5 | grep error` — debería mostrar 401 con accountId=1 o token incorrecto
  2. Si sigue en 401: reiniciar OpenWA (`cd /opt/OpenWA && docker compose restart`), esperar 20s, luego activar adapter vía API (`curl -s -X POST -H "x-api-key: M4rtin091121+" http://localhost:2785/api/plugins/chatwoot-adapter/enable`) y probar con WhatsApp de prueba
  3. Configurar webhook de vuelta en Chatwoot: Settings → Integrations → Webhooks → URL: `https://wa.palferia.me/api/ingress/chatwoot-adapter/6b4c21ab-6f5b-464d-ae7c-2e04d76e141d/chatwoot` (eventos: Message Created + Conversation Status Changed)
- [ ] Construir plugin `palferia-ai-agent` para OpenWA (roadmap en `docs/roadmap-plugin-openwa.md`)
- [ ] Conectar webhook http-action OpenWA → n8n para clientes
- [ ] Sesión Cortinajes Valls en OpenWA — pendiente escanear QR
- [ ] Generar N8N_API_KEY en n8n y guardar en `config/infra.env` del Orquestador
- [ ] Actualizar Orquestador para que genere setter tool automáticamente al crear propuesta
- [ ] Proxy nginx: `/api/n8n/*` → n8n interno (seguridad)

### Pricing / Contratos
- [ ] Completar campos fijos en `kit-contrato-cliente`: NIF PalferIA, dirección fiscal, cuenta bancaria
- [ ] Revisar y cerrar valores del SOP de mantenimiento (precios, horas, tarifa/hora)
- [ ] Crear documento oficial one-pager COM-studio y ME-sport (desbloquea propuesta UD Rocafort CF)
- [ ] Integrar `kit-pricing-planes` como referencia oficial en kit-orquestador-propuestas

### UD Rocafort CF (bloqueantes)
- [ ] Gap 2: Web demo con kit-instagram-web (@udrocafortcf) + kit-web-scrolling
- [ ] Gap 3: Google My Business en orquestador y deliverables
- [ ] Gap 4: Correr kit-auditoria-negocio y kit-auditoria-meta-ads reales
- [ ] Gap 5: Deploy propuesta desde CRM (webhook/n8n)

---

## REGISTRO DE CLIENTES / PROSPECTOS

### Estado pipeline (26/08/2026)

| Proyecto | Identificados | Contactados | ⏳ Esperando | 🔄 Alt. canal | 📋 Propuesta |
|----------|--------------|-------------|--------------|---------------|--------------|
| COM-studio | 11 | 4 | 4 | 0 | 1 (Cortinajes) |
| ME-sport | 6 | 5 | 4 | 1 | 1 (Tecniluispa) |

### Prospectos destacados

**Tecniluispa** (Luis Pascual García Notario — baloncesto 3x3)
- Reunión: 21/08/2026 ✅ — Propuesta bien recibida, no cierra ahora
- Motivo: momento del año + 2 proyectos activos (UE + Valencia Basket)
- Estado: 🔄 seguimiento programado **29/08/2026**
- Acción: recordatorio suave + pedir que recomiende otras academias de su red
- Propuesta: `sales.palferia.me/propuestas/d904b65e-tecniluispa.html`
- Precio discutido: 750€ (canales) / 1.000€ (con landings) — propuesta enviada: 900€/mes Plan Avanzado

**Cortinajes Valls & París** (Godella, COM-studio)
- Propuesta enviada: `sales.palferia.me/propuestas/b7f3c1a9-cortinajes-valls.html`
- Estado: 📋 en espera — regresa de vacaciones ~25/08
- Acción: sensibilizar semana 25/08
- Plan propuesto: Vecino Digital 1.200€ setup o Autopilot 30 (3.100€ + 499€/mes)

**CrossFit Taronja Moncada** (ME-sport)
- Es franquicia WodBuster — NO vender lo que ya cubre WodBuster
- Propuesta adaptada: Sprint 900€/mes como complemento (captación externa, WhatsApp, newsletter, reseñas, RRSS)

---

## DECISIONES TÉCNICAS VIGENTES

| Decisión | Motivo | Fecha |
|----------|--------|-------|
| `/setter/` con Basic Auth nginx (`setter` / `Palferia2026`) | Más seguro que `?interno` en URL pública | 21/08 |
| `Cache-Control: no-store` en HTML del VPS | Safari cachea agresivamente — problema resuelto | 21/08 |
| Plugin OpenWA en vez de migrar a Baileys | Resuelve el mismo problema sin romper sesión activa | 20/08 |
| kit-prospeccion v3 usa service role key (solo en `.env.local`) | Necesita escribir en Supabase sin RLS anon | 21/08 |
| Propuestas: `/propuestas/` con 403 listing | Un prospecto no puede ver propuestas ajenas | 21/08 |
| Logo ME-sport separado de COM-studio | Identidad visual correcta por vertical | 21/08 |
| `window.location.replace('/')` en logout | Evita exponer `index.html` en URL | 21/08 |
| API keys fuera del HTML → `public/config.js` (gitignored) | Buenas prácticas + no exponer en GitHub | 26/08 |
| rsync con `--exclude='config.js'` en deploy | config.js vive en VPS, no en repo | 26/08 |
| Skills reorganizadas en `ai/` con 6 categorías | Alineación con arquitectura DraftDayES, mejor discoverabilidad | 26/08 |

---

## INFRAESTRUCTURA (referencia rápida)

```
VPS:          31.97.192.164 (Ubuntu 24.04 LTS)
CRM:          sales.palferia.me → /var/www/sales.palferia.me/
OpenWA:       wa.palferia.me → puerto interno 2785 | API Key: M4rtin091121+
              Sesión: ronia-palferia | ID: 6b4c21ab-6f5b-464d-ae7c-2e04d76e141d | Tel: 34672037621
Chatwoot:     inbox.palferia.me | ripvlad@gmail.com / M1ch3_020927
              Account ID: 3 | Inbox ID: 1 | API Token: 63kAV4Ldevd6SEiFw7cbouyN
n8n:          n8n.srv905238.hstgr.cloud | N8N_API_KEY: PENDIENTE
Supabase:     aqaiqmsypbwhgknbbmae.supabase.co
GitHub:       PalferIA-Ron/palferia-sales-crm
SSH key:      ~/.ssh/palferia_vps
Deploy:       push main → GitHub Actions → rsync --exclude='config.js'
```

**Supabase tablas:**
- `prospectos` — núcleo CRM (+ campos web, instagram, pain, semana añadidos en migración)
- `pipeline_log` — auditoría de acciones
- `mensajes_whatsapp` — historial chats WA
- `propuestas` — propuestas generadas (slug UUID, url, estado, skills_usadas)

**RLS:** authenticated = full access | anon = INSERT only en prospectos y pipeline_log (para kit-prospeccion)

**OpenWA plugins instalados (10):** http-action, after-hours, chat-flow, chatwoot-adapter, faq-bot, group-translate, gsheets-logger, supabase-otp-hook, typebot-connector, voice-transcription. Auto-update diario 3am.

---

## SESIONES

---

### Sesión 2026-08-29/30 + 2026-09-03 — Inbox Chatwoot + CRM actualizado
**Objetivo:** Integrar inbox centralizado (WhatsApp + otros canales) vía Chatwoot + OpenWA

**Completado:**
- [x] Catálogo de 15 automatizaciones n8n con pricing (`_deliverables/COM-studio/catalogo-automatizaciones.md`)
  - Precios: Simple 1.200€ / Media 1.500€ / Compleja 1.800€ / Multi-flujo 2.500€
  - La Tribu Divisual: 130€/mes por todos sus workflows
- [x] CRM: sección WhatsApp reemplazada por botón → `inbox.palferia.me` (ya no iframe)
- [x] Chatwoot instalado en VPS (`inbox.palferia.me`) — Docker con pgvector:pg16 + Redis
  - Usuario: ripvlad@gmail.com / M1ch3_020927
  - Account ID: 3 | Inbox ID: 1 | Inbox Identifier: JEeHukSqa9mHLsvWi2GBfj1v
  - API Token usuario: 63kAV4Ldevd6SEiFw7cbouyN
- [x] OpenWA reinstalado limpio desde `/opt/OpenWA/`
  - Sesión: ronia-palferia (ID: 6b4c21ab-6f5b-464d-ae7c-2e04d76e141d, teléfono: 34672037621)
  - API Key: M4rtin091121+
- [x] chatwoot-adapter habilitado en registry.json con config correcta (accountId=3, token actualizado)
- [x] Plugin se carga correctamente: "Plugin loaded: Chatwoot Adapter v0.9.4" ✅
- [x] Plugin se activa correctamente vía API: `{"success":true}` ✅

**Estado integración:** El adapter recibe mensajes y los intenta enviar a Chatwoot — último error conocido: `401` apuntando a accountId=1. Config en registry.json actualizada a accountId=3 pero necesita verificación post-reinicio.

**Pendiente (3 pasos):** Ver sección Infraestructura/Técnico arriba.

**Decisiones tomadas:**
- Opción B (OpenWA → Chatwoot) en vez de WhatsApp Cloud API (Meta) — número nuevo reservado para futuro Meta API
- Meta Developer App creada: ID 2375385899536563 (para uso futuro con número dedicado)
- inbox.palferia.me = herramienta independiente, NO embebida en el CRM (fue iframe, ahora botón)

---

### Sesión 2026-08-28 — Deliverables Orquestador + Paths corregidos
**Objetivo:** Crear archivos de referencia de deliverables para el Orquestador de Propuestas (COM-studio y ME-SportCenter) + corregir rutas rotas en SKILL.md

**Completado:**
- [x] Creado `_deliverables/COM-studio/deliverables-planes.md`
  - Fuentes: `oferta-sistema-autopilot30.md` + `planes-pricing.md`
  - Cubre: Vecino Digital (1.200€) / Autopilot 30 (3.100€) / Socio Digital (4.900€)
  - Incluye: checklist S7 por plan, módulos add-on, cuotas mantenimiento, costes de APIs, objeciones, frases de cierre, escasez real, caso Grupo Cueva
- [x] Creado `_deliverables/ME-SportCenter/deliverables-planes.md`
  - Fuentes: `planes.md` + `servicios.md` + `servicios-vertical-academias-clubes.md` + `vertical-eventos.md`
  - Cubre: Sprint IA (900€/mes) / Equipo IA (1.500€/mes) / Liga IA (2.500€+/mes) + modalidad por evento (1.200 / 2.000 / 3.500€) + patrocinios + integración apps deportivas
  - **Diferenciador clave:** sección de Verticales sector-específicas — los deliverables se adaptan según academia / club / evento / federación / turismo activo / patrocinios
- [x] Rutas rotas en `ai/workflows/kit-orquestador-propuestas/SKILL.md` corregidas:
  - `skills/kit-auditoria-negocio/` → `ai/auditorias/kit-auditoria-negocio/`
  - `skills/kit-auditoria-meta-ads/` → `ai/auditorias/kit-auditoria-meta-ads/`
  - `skills/kit-auditoria-seo/` → `ai/auditorias/kit-auditoria-seo/`

**Pendiente del Orquestador (próxima sesión):**
- [ ] Añadir bloque 3C (DraftDayES) en las fases de preview de SKILL.md
- [ ] Referenciar `_deliverables/COM-studio/deliverables-planes.md` y `_deliverables/ME-SportCenter/deliverables-planes.md` en la Fase 5 (S7) del SKILL.md

---

### Sesión 2026-08-26 — Arquitectura Claude + Seguridad
**Objetivo:** Establecer fundamentos de arquitectura Claude + reorganizar skills + ESLint + seguridad básica

**Completado:**
- [x] Análisis comparativo DraftDayES vs palferia-sales-crm
- [x] Creado `CLAUDE.md` con identidad, stack, dominios, modos de trabajo, principios
- [x] Creado `.claude/bitacora/BITACORA.md` (este archivo, con historial completo recuperado)
- [x] Creado `.claude/plans/2026-08-26-plan-maestro.md` con roadmap por fases
- [x] Reorganización `skills/` → `ai/` (agents, prompts, auditorias, workflows, tools, utils)
- [x] ESLint + Prettier configurados (`package.json`, `eslint.config.js`, `.prettierrc`)
- [x] Seguridad: `public/config.js` con credenciales fuera del HTML (gitignored)
- [x] `crm.html` e `index.html` usan `window.PALFERIA_CONFIG` en vez de keys hardcodeadas
- [x] `deploy.yml` actualizado con `--exclude='config.js'`
- [x] Verificado: función `esc()` ya protege contra XSS — no había riesgo activo

**Acción pendiente (Ronald):** subir `config.js` al VPS una vez:
```bash
scp public/config.js root@31.97.192.164:/var/www/sales.palferia.me/config.js
```

---

### Sesión 2026-08-23 — Auditoría seguridad + Skills comerciales + ChatGPT Ads
**Objetivo:** Auditoría seguridad + Fase 1 skills comerciales + Fase 3 pricing

**Completado:**
- [x] Auditoría de seguridad completa del workspace
  - `SUPABASE_SERVICE_KEY` en `.env.local` — en `.gitignore`, nunca entró a git ✅
  - IP VPS solo en docs/skills, no en `public/` desplegado ✅
  - GitHub Actions usa secrets correctamente ✅
  - Pendiente: `StrictHostKeyChecking=no` en rsync
- [x] Informe generado: `/workspace/INFORME-auditoria-skills-chatbot.md`
- [x] Mapa de 11 proyectos creado: `/workspace/PROYECTOS-OVERVIEW.md`
- [x] Skills globales creadas (`~/.claude/skills/`):
  - `kit-objeciones-ventas` — 8 objeciones con respuestas por perfil ESMERALDA/RUBÍ/ZAFIRO/PERLA
  - `kit-seguimiento-propuesta` — secuencia 7 días post-propuesta (Día 0/1/3/5/7)
  - `kit-contrato-cliente` — generador contratos Setup y Mantenimiento con deliverables por plan
  - `kit-pricing-planes` — fuente oficial de precios: planes base + módulos + mercado ES 2026 + ChatGPT Ads
- [x] Módulos adicionales incorporados al orquestador: Landing IA (600-800€), Web corporativa IA (1.200-1.600€), SEO local (300-450€/mes), GEO/AEO (400-600€/mes), Gestión RRSS IA (350-500€/mes), ChatGPT Ads (400-600€/mes), Meta Ads (500-700€/mes), Google Ads (400-600€/mes)
- [x] Desglose costes cliente vs PalferIA documentado

**Hallazgo clave:** ChatGPT Ads llega a España el **24 agosto 2026** — primera agencia en la zona que lo ofrece

**Sesión continuó en:** `/workspace/openwa-palferia`

---

### Sesión 2026-08-24 — OpenWA dashboard HTTPS + Manual plugins + Arquitectura multicanal
*(registrada en openwa-palferia — impacto en palferia-sales-crm)*

**Completado:**
- [x] `https://wa.palferia.me` operativo — Traefik → nginx-proxy → openwa-api:2785
- [x] SSL Let's Encrypt válido hasta Nov 2026, auto-renovación
- [x] Manual de plugins creado: `openwa-palferia/docs/manual-plugins.md`
- [x] Arquitectura multicanal definida: WA + Facebook + Instagram + Email → n8n → Claude → respuesta por canal
- [x] Pestaña Plantillas documentada, personalización logo/color documentada

**Pendiente de implementar:**
- [ ] Webhook OpenWA → n8n (una llamada API para configurar URL)
- [ ] App Meta para Facebook/Instagram (si cliente lo necesita)
- [ ] Workflow n8n que enruta canales al mismo agente Claude

---

### Sesión 2026-08-22 — Skills comerciales (Sesión 11)
**Objetivo:** Análisis Marketing Hackers + Fase 1 Skills comerciales

**Completado:**
- [x] Análisis completo de `/Downloads/marketing hackers/` y `/skills/`
- [x] Skills globales creadas: `kit-objeciones-ventas`, `kit-seguimiento-propuesta`, `kit-contrato-cliente`
- [x] Pendiente completar en `kit-contrato-cliente`: NIF PalferIA, dirección fiscal, cuenta bancaria

---

### Sesión 2026-08-21/22 — Propuesta Cortinajes + Orquestador config central (Sesión 10)
**Objetivo:** Propuesta Cortinajes Valls & París + setter tool + centralizar config Orquestador

**Completado:**
- [x] Propuesta cliente Cortinajes (`b7f3c1a9-cortinajes-valls.html`): 11 slides, acento teal, Playfair Display
- [x] Setter tool Cortinajes (`/setter/b7f3c1a9-cortinajes-valls.html`): 10 secciones + sección Meta Ads
- [x] Auditoría Meta Ads Cortinajes: 0 anuncios activos, landing 28/100, sin Pixel, sin GA4
- [x] Calculadora descuento COM-studio (Vecino Digital / Autopilot 30 / Socio Digital) en setter
- [x] Orquestador — `config/` centralizado: `infra.env`, `infra.env.example`, `config_manager.py`
- [x] `n8n_client.py` auto-carga desde `config/infra.env` (sin `export` manual)
- [x] Estado `check`: 10 credenciales definidas, 1 vacía (`N8N_API_KEY`)

---

### Sesión 2026-08-21 (tarde/noche) — Propuesta Tecniluispa + Setter tool (Sesión 9)
**Objetivo:** Generar propuesta Tecniluispa, setter tool, configurar /setter/ en nginx

**Completado:**
- [x] Propuesta cliente: `sales.palferia.me/propuestas/d904b65e-tecniluispa.html` (10 slides)
  - Logo ME-sport correcto, avatares reales, foto Luis fondo, textura baloncesto
  - Registrada en Supabase: `prospecto_id: 1672d1a1`, `propuesta_id: b91506d0`
- [x] `/setter/` configurado en nginx con Basic Auth (`setter` / `Palferia2026`)
- [x] `Cache-Control: no-store` en HTML — Safari ya no cachea
- [x] Setter tool Tecniluispa: 9 secciones (resumen, auditoría, ROI, plan+descuento, objeciones, tips negociación, entregables, mapa proceso, Notas Gemini)
- [x] Calculadora descuento ME-sport: 4 planes con floor automático y semáforo
- [x] Notas Gemini embebidas: Drive MCP funcional con `ri@palferia.com`
- [x] Botón "🔒 Setter" en CRM para acceder al setter desde tarjeta de propuesta
- [x] Logout redirige a `/` en vez de `/index.html`

**Dato clave Tecniluispa:** equipo 3x3 cancelado en 2026 — coste viajes + seguros sin apoyo

---

### Sesión 2026-08-21 — Resultado reunión Tecniluispa + kit-prospeccion v3 + Supabase (Sesión 8)
**Objetivo:** Seguimiento reunión + completar integraciones técnicas CRM

**Completado:**
- [x] Reunión Tecniluispa celebrada 12:00 — Propuesta bien recibida, NO cierra (momento del año + UE + Valencia Basket)
- [x] Estado → 🔄 seguimiento **29/08/2026**
- [x] Seguridad CRM: intento acceso externo (`viralcommunity.co@gmail.com`) bloqueado ✅
- [x] Sign Ups desactivado en Supabase Auth — confirmado ✅
- [x] kit-prospeccion v3: nuevo Paso 6 → escribe en Supabase al finalizar búsqueda
  - Verifica duplicados por nombre+municipio → inserta en `prospectos` → log en `pipeline_log`
  - JSON estandarizado: nombre, municipio, sector, score, web, instagram, email, telefono, pain, proyecto, semana
- [x] Migración Supabase ejecutada: tabla `propuestas` + campos nuevos en `prospectos` (web, instagram, pain, semana)
- [x] RLS: anon INSERT en prospectos y pipeline_log (para que el skill escriba sin auth)
- [x] nginx: `/propuestas/` → 403 listing | inexistente → 404 | token exacto → 200
- [x] Creado `docs/manual-supabase-tablas.md`

---

### Sesión 2026-08-21 (mañana) — Preparación reunión Tecniluispa + Análisis integración skills (Sesión 6)
**Objetivo:** Preparar reunión + analizar cómo integrar skills con subdominios

**Completado:**
- [x] Guión reunión Tecniluispa: 6 bloques, hoja credenciales, señales de cierre, Email A y B
- [x] `docs/analisis-integracion-skills.md` creado con roadmap completo
- [x] Decisión sobre whatsapp-ai-agent-kit: NO migrar Baileys → usar plugin nativo OpenWA
- [x] Decisión kit-prospeccion: integrar con Supabase (FÁCIL — 1 día trabajo)
- [x] Roadmap acordado: kit-prospeccion esta semana / plugin WA semana 3 / panel WA semana 4

---

### Sesión 2026-08-20 (noche) — Investigación plugins OpenWA (Sesión 7)
**Objetivo:** Analizar plugins OpenWA para construir agente IA

**Completado:**
- [x] Analizados plugins nativos de `rmyndharis/OpenWA-plugins`
- [x] Decisión: crear plugin propio `palferia-ai-agent` (NO migrar a Baileys)
- [x] Arquitectura: `message:received → dedup → Supabase (inbound) → Claude API → Supabase (outbound) → respuesta`
- [x] Roadmap creado: `docs/roadmap-plugin-openwa.md`

---

### Sesión 2026-08-20 (tarde) — CRM online en producción (Sesión 5)
**Objetivo:** Desplegar CRM completo en sales.palferia.me

**Completado:**
- [x] CRM desplegado en `sales.palferia.me` con Traefik + SSL automático
- [x] Stack: HTML/JS estático + Supabase + OpenWA port 2785 + Traefik
- [x] Supabase: schema + seed (17 prospectos precargados) + credencial n8n
- [x] Dashboard OpenWA en `wa.palferia.me` — sesión `palferia-principal` conectada via QR
- [x] Webhook OpenWA → n8n → Supabase: flujo probado y funcionando ✅
- [x] CRM funcionalidades: login, prospectos (tabla+kanban), WhatsApp (sesiones+chat), propuestas (cards+links), log
- [x] Tecniluispa añadido al CRM — reunión **21/08/2026 a las 12:00**
- [x] Propuesta Tecniluispa en Netlify: `https://tenic-luispa-100pme1.netlify.app`
- [x] GitHub Actions deploy configurado (secrets: VPS_HOST, VPS_USER, VPS_SSH_KEY)

---

### Sesión 2026-08-20 (mañana) — Seguimientos + CRM local + Landing servicios (Sesión 4)
**Objetivo:** Seguimientos +4 días + herramientas comerciales

**Completado:**
- [x] Seguimientos enviados a 8 prospectos (COM-studio: 4, ME-sport: 4) → estado ⏳
- [x] CrossFit Taronja: confirmado franquicia WodBuster, canal alternativo (WA/llamada)
- [x] `clientes/CRM.html` creado: 3 vistas (Kanban/Tabla/Acciones), 17 prospectos, persistencia localStorage
- [x] Servicios PalferIA definidos: Vecino Digital (1.200€), Socio Digital (3.100€), A Medida + planes mensuales Starter (299€), Growth (499€), Partner (799€)
- [x] `COM-studio/landing-servicios.html` creado

---

### Sesión 2026-08-16 — Prospección Semana 1 + estructura carpetas (Sesiones 2-3)
**Objetivo:** 10 COM-studio + 10 ME-sport identificados + estructura completa

**Completado:**
- [x] kit-prospeccion ejecutado en Horta Nord (Burjassot, Paterna, Moncada, Rocafort, Bétera)
- [x] COM-studio: 11 identificados (4 prioridad alta, 7 semana 2)
- [x] ME-sport: 6 identificados (5 prioridad alta, 1 media)
- [x] 9 emails enviados el 16/08/2026 desde ri@palferia.com
- [x] Carpetas por prospecto creadas (COM-studio: 9 / ME-sport: 5) con README + subcarpetas
- [x] Estado CRM: 11 COM-studio identificados (4 contactados) + 6 ME-sport (5 contactados)

**Prospectos prioridad alta COM-studio:** Romaib Fontaneros, Cortinajes Valls & París, Fisioterapia Bienestar, Masía Rocafort
**Prospectos prioridad alta ME-sport:** Estudio Vitale, Dojo Hikari, DF Swimming Team, CrossFit Taronja, B-Phulness

---

### Sesión 2026-08-16 — Inicio del proyecto (Sesión 1)
**Objetivo:** Estructura comercial formal para gestionar prospección

**Completado:**
- [x] `CLAUDE.md` — configuración del proyecto
- [x] `PLAYBOOK-v2.md` — estrategia comercial actualizada
- [x] `CRM.md` — tracker de prospectos
- [x] `RUTINA-SEMANAL.md` — proceso lunes a viernes
- [x] `BITACORA.md` — este archivo
- [x] Estado inicial: 1 prospecto COM-studio activo (Cortinajes Valls, score 33/100, email enviado agosto sin respuesta), 0 ME-sport

---

## PRECIOS DE REFERENCIA (vigentes a 26/08/2026)

### Setters (implantación única)
| Plan | Precio |
|------|--------|
| Vecino Digital | 1.200€ |
| Autopilot 30 | 3.100€ + 499€/mes |
| Socio Digital | 4.900€ + 799€/mes |

### Planes mantenimiento (mensuales)
| Plan | Precio | Horas | Respuesta |
|------|--------|-------|-----------|
| Básico (Pit Stop) | 250€/mes | 1h | 48-72h |
| Profesional (Alto Rendimiento) | 490€/mes | 3h | 24-48h |
| Avanzado | 900€/mes | 6h | 24h |
| Crítico | 1.500€+/mes | Bolsa amplia | Prioritario |

Tarifa hora extras: **60€/h** | Consumos (tokens, WA, telefonía): siempre aparte

### Módulos adicionales
Landing IA (600-800€) · Web corporativa IA (1.200-1.600€) · SEO local (300-450€/mes) · GEO/AEO (400-600€/mes) · RRSS IA (350-500€/mes) · ChatGPT Ads (400-600€/mes) · Meta Ads (500-700€/mes) · Google Ads (400-600€/mes)
