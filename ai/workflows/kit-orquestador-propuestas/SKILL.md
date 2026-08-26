---
name: kit-orquestador-propuestas
description: >
  Orquesta la creación completa de una propuesta comercial PalferIA: hace
  preguntas, corre auditorías, calcula precios, genera preview conversacional,
  construye el HTML de propuesta + setter tool, despliega en VPS y registra
  en Supabase. Actívala cuando el usuario diga "crear propuesta para [nombre]",
  "hacer propuesta", "generar propuesta", o cuando quiera iniciar el proceso
  completo de propuesta para un prospecto.
version: 1.0.0
author: PalferIA
---

# Kit Orquestador de Propuestas — PalferIA

Genera propuestas comerciales completas paso a paso: auditoría → precios →
preview conversacional → HTML → setter tool → deploy → Supabase.

**Principio rector:** Antes de construir nada, mostrar qué vas a construir.
El usuario revisa y corrige en conversación antes de generar el HTML final.

---

## FASE 0 — Intake del prospecto

### Paso 0.1 — Buscar en Supabase primero

Antes de preguntar, comprobar si el prospecto ya existe:

```bash
curl -s "https://aqaiqmsypbwhgknbbmae.supabase.co/rest/v1/prospectos?nombre=ilike.*[NOMBRE]*&select=*" \
  -H "apikey: sb_secret_Jtsn1Qe7tWlMvWThaDOJfg_TpNUCOP2" \
  -H "Authorization: Bearer sb_secret_Jtsn1Qe7tWlMvWThaDOJfg_TpNUCOP2"
```

- Si existe → mostrar los datos y preguntar: "¿Es este prospecto? ¿Los datos siguen siendo correctos?"
- Si no existe → hacer las preguntas del Paso 0.2

### Paso 0.2 — Preguntas de intake (todo en un solo bloque)

Hacer estas preguntas en conversación natural, no como formulario:

**Bloque 1 — El prospecto**
- Nombre del negocio y sector
- Municipio
- Web (URL si tiene)
- Instagram / redes activas
- Email de contacto
- ¿Proyecto? COM-studio o ME-sport

**Bloque 2 — Situación digital conocida**
- ¿Qué sabes ya de ellos? (pain conocido, auditorías previas, notas de reunión)
- Score aproximado si lo tienes (si no, lo calculamos en Fase 1)
- ¿Han tenido contacto previo? ¿Cuál fue la respuesta?

**Bloque 3 — Infraestructura (condicional)**
Solo si el usuario lo sabe. Si no, dejar para el setter:
- ¿El cliente tiene VPS/n8n propio?
- ¿Tiene dominio propio?
- ¿Tiene restricciones de datos (sector salud, legal)?

**Bloque 4 — Orientación comercial**
- ¿Qué plan estimas recomendar? (o dejamos que lo decida la auditoría)
- ¿Hay un presupuesto aproximado que el cliente mencionó?
- ¿Quién asumirá los costes de API? (cliente directamente / nosotros con markup)

### Paso 0.3 — Confirmación antes de auditar

Mostrar resumen de lo recogido:

```
📋 RESUMEN PROSPECTO
─────────────────────────────
Negocio:    [NOMBRE] — [SECTOR]
Municipio:  [MUNICIPIO]
Proyecto:   [COM-studio / ME-sport]
Web:        [URL o "sin web conocida"]
Instagram:  [@handle o "sin datos"]
Pain:       [lo que el usuario describió]
Infra:      [opción A/B/C o "por definir"]
─────────────────────────────
```

Preguntar: **"¿Empezamos las auditorías con estos datos?"**

---

## FASE 1 — Auditorías

Correr en orden según lo disponible. Mostrar resultado resumido tras cada una y preguntar si hay algo que corregir o añadir.

### 1.1 — Auditoría de presencia digital

Si tiene web → usar `kit-auditoria-negocio` de:
`/Users/macbook/Desktop/workspace/palferia-sales-crm/skills/kit-auditoria-negocio/SKILL.md`

Guardar resultado en:
`clientes/[proyecto]/[nombre-slug]/auditoria/auditoria-negocio-[nombre-slug].html`

**Preview tras auditoría:**
```
🔍 DIAGNÓSTICO DIGITAL
──────────────────────────────
Score:         [X]/100
Nivel:         [Muy alta / Alta / Media oportunidad]
Gaps críticos: [3 bullets principales]
──────────────────────────────
¿Algo que corregir antes de continuar?
```

### 1.2 — Auditoría Meta Ads (condicional)

Correr si: tiene presencia en Facebook/Instagram O si score < 55 (el 0 anuncios es argumento de venta).

Usar `kit-auditoria-meta-ads` de:
`/Users/macbook/Desktop/workspace/palferia-sales-crm/skills/kit-auditoria-meta-ads/SKILL.md`

Guardar en:
`clientes/[proyecto]/[nombre-slug]/auditoria/auditoria-meta-ads-[nombre-slug].html`

**Preview:**
```
📊 META ADS
──────────────────────────────
Anuncios activos:  [N]
Score landing:     [X]/100
Pixel instalado:   [Sí / No]
Argumento clave:   [frase de venta]
──────────────────────────────
```

### 1.3 — Auditoría SEO (condicional)

Correr si tiene web y el proyecto es COM-studio.

Usar `kit-auditoria-seo` de:
`/Users/macbook/Desktop/workspace/palferia-sales-crm/skills/kit-auditoria-seo/SKILL.md`

### 1.4 — Actualizar score en Supabase

Si el prospecto ya existía en Supabase, actualizar el score con el resultado de la auditoría:

```bash
curl -s -X PATCH \
  "https://aqaiqmsypbwhgknbbmae.supabase.co/rest/v1/prospectos?id=eq.[ID]" \
  -H "apikey: sb_secret_Jtsn1Qe7tWlMvWThaDOJfg_TpNUCOP2" \
  -H "Authorization: Bearer sb_secret_Jtsn1Qe7tWlMvWThaDOJfg_TpNUCOP2" \
  -H "Content-Type: application/json" \
  -d '{"score": [SCORE], "web": "[URL]", "pain": "[PAIN_RESUMIDO]"}'
```

---

## FASE 2 — Arquitectura de precios

Leer `references/planes-pricing.md`, `references/infraestructura-opciones.md` y `~/.claude/skills/kit-pricing-planes.md` antes de calcular.
La skill `kit-pricing-planes` es la fuente oficial de precios — incluye planes base, módulos adicionales, precios de mercado ES 2026 y el módulo ChatGPT Ads.

### Paso 2.1 — Recomendar plan de setup

Basarse en:
- Score de auditoría (más bajo = más complejo = plan más alto)
- Sector y volumen estimado de conversaciones
- Complejidad requerida (¿chatbot FAQ o agente operativo?)
- Integraciones necesarias (CRM, calendario, WhatsApp, voz)

Mostrar los 3 planes y marcar el recomendado:

```
💰 INVERSIÓN INICIAL (pago único)
──────────────────────────────────────────────────────
                    Vecino Digital    Autopilot 30    Socio Digital
Precio cliente:       1.200 €          3.100 €         4.900 €
Incluye:          [descripción]    [descripción]   [descripción]
──────────────────────────────────────────────────────
★ RECOMENDADO: [plan] — porque [razón basada en auditoría]
──────────────────────────────────────────────────────
```

### Paso 2.2 — Recomendar plan de mantenimiento (SEPARADO)

**IMPORTANTE:** Presentar siempre como línea separada. Son dos conversaciones distintas.

```
📅 CUOTA MENSUAL (recurrente, contrato independiente)
──────────────────────────────────────────────────────
Plan Básico:         250 €/mes — 1h ajustes, soporte email
Plan Profesional:    490 €/mes — 3h ajustes, soporte prioritario ← recomendado
Plan Avanzado:       900 €/mes — 6h ajustes, revisión quincenal
──────────────────────────────────────────────────────
```

### Paso 2.3 — Módulos adicionales (condicional)

Preguntar al usuario si quiere proponer módulos de marketing adicionales al plan base.
Mostrar solo los relevantes según el perfil del prospecto:

```
🧩 MÓDULOS ADICIONALES (opcionales — contrato/anexo separado)
══════════════════════════════════════════════════════════════

EJECUTADOS POR PALFERIA CON IA:
  Landing page IA             600–800 € (único)     [si no tiene web o es mala]
  Web corporativa IA        1.200–1.600 € (único)   [si necesita web completa]
  SEO local + on-page         300–450 €/mes          [si quiere posicionamiento]
  GEO/AEO ⭐                  400–600 €/mes          [diferenciador — ofrecer siempre]
  Gestión RRSS con IA         350–500 €/mes          [si tiene redes activas]
  ChatGPT Ads 🆕              400–600 €/mes          [ofrecer siempre desde ago-2026]

SUBCONTRATADOS (fee de gestión — presupuesto ads va directo al cliente):
  Meta Ads gestión            500–700 €/mes
  Google Ads gestión          400–600 €/mes
  Pack Ads completo           800–1.100 €/mes

══════════════════════════════════════════════════════════════
⚠️ El presupuesto publicitario (Meta/Google/OpenAI) lo paga
   el cliente directamente — NUNCA va incluido en el fee.
══════════════════════════════════════════════════════════════
```

**Regla de módulos:** Solo proponer los que aporten valor real según la auditoría. No saturar la propuesta. Máximo 2-3 módulos en la primera propuesta.

**ChatGPT Ads — nota especial:**
Desde el 24 agosto 2026 está disponible en España. Ofrecerlo siempre como diferenciador:
- Setup + configuración inicial: 300–500 € (único)
- Gestión mensual: 400–600 €/mes
- Presupuesto mínimo recomendado al cliente: 200–300 €/mes directo a OpenAI
- Frase de venta: *"Somos de las primeras agencias en España que gestiona anuncios en ChatGPT"*

### Paso 2.4 — Infraestructura (condicional)

Según opción A/B/C detectada en Fase 0:

```
🖥️ INFRAESTRUCTURA
──────────────────────────────────────────────────────
Opción: [A / B / C]

[Si B]:
+ Alojamiento en VPS PalferIA:    30–60 €/mes (incluido en cuota o aparte)

COSTES QUE ASUME EL CLIENTE DIRECTAMENTE:
• OpenAI / Claude tokens:          20–80 €/mes (variable por uso)
• WhatsApp Business API:           0–50 €/mes (variable)
• Dominio web:                     10–15 €/año
[+ otros según el caso]
──────────────────────────────────────────────────────
```

### Paso 2.5 — Preview final de precios

```
📊 RESUMEN ECONÓMICO COMPLETO
══════════════════════════════════════════════════════
INVERSIÓN INICIAL (una vez):
  Plan [nombre]:              [X.XXX] €
  [Módulo setup si aplica]:   [XXX] €
  ──────────────────────────────
  TOTAL INICIAL:              [X.XXX] €

CUOTA MENSUAL (recurrente):
  Mantenimiento [plan]:       [XXX] €/mes
  [Módulo mensual 1]:         [XXX] €/mes
  [Módulo mensual 2]:         [XXX] €/mes
  Alojamiento (si Opción B):  [XX] €/mes
  ──────────────────────────────
  TOTAL MENSUAL:              [X.XXX] €/mes

COSTES QUE ASUME EL CLIENTE DIRECTAMENTE:
  APIs IA (tokens):           20–80 €/mes
  WhatsApp Business API:      0–50 €/mes
  Presupuesto ads:            [XXX] €/mes → a Meta/Google/OpenAI
  Dominio web:                10–15 €/año
══════════════════════════════════════════════════════
```

Preguntar: **"¿Ajusto algún precio o cambio el plan antes de generar la propuesta?"**

---

## FASE 3 — Preview conversacional de la propuesta

**Antes de generar el HTML**, mostrar el índice de slides y el contenido de cada una en texto plano. Esperar aprobación slide a slide o en bloque.

**→ Si proyecto = COM-studio → usar bloque 3A**
**→ Si proyecto = ME-sport → usar bloque 3B**

---

### 3A — Preview COM-studio (negocios locales)

```
📋 ESTRUCTURA DE LA PROPUESTA — [NOMBRE]  ·  COM-studio
══════════════════════════════════════════════════════

SLIDE 1 — PORTADA
  Título: "Sistema Omnicanal IA — [Nombre negocio]"
  Subtítulo: [sector] · [municipio]
  CTA: "Ver propuesta"

SLIDE 2 — DIAGNÓSTICO
  Score: [X]/100
  Problema principal: [descripción]
  3 gaps críticos: [lista]

SLIDE 3 — META ADS (si aplica)
  [si hubo auditoría de Meta Ads]

SLIDE 4 — COSTE REAL DEL PROBLEMA
  Estimación de lo que pierde mensualmente sin automatización
  Ej: leads ignorados × ticket medio × meses = [€ perdidos/año]

SLIDE 5 — LA SOLUCIÓN
  Qué hace el agente IA: [descripción adaptada al negocio]
  Canales: WhatsApp · Web · Instagram · Email · Voz (según plan)
  Funciones clave: respuesta 24/7, captación de leads, seguimiento automático

SLIDE 6 — PLAN RECOMENDADO
  [Vecino Digital / Autopilot 30 / Socio Digital] — [precio] € (pago único)
  Qué incluye: [lista de deliverables del plan]

SLIDE 7 — CUOTA MENSUAL
  Plan [Básico/Profesional/Avanzado] — [precio] €/mes
  Qué incluye: [X] h/mes ajustes, soporte [plazo], reporting

SLIDE 7B — MÓDULOS ADICIONALES (si se proponen)
  [módulo 1]: [precio] — qué incluye
  [módulo 2]: [precio] — qué incluye
  Nota: contratos/anexos independientes

SLIDE 8 — INFRAESTRUCTURA Y COSTES
  Opción [A/B/C] — [explicación]
  Costes cliente directos: APIs IA, WhatsApp Business, dominio, ads

SLIDE 9 — ROI PROYECTADO
  Basado en: [X leads/mes actuales] × [ticket medio] × [% conversión mejora]
  Recuperación inversión estimada: [N] meses

SLIDE 10 — SIGUIENTE PASO
  CTA + datos de contacto PalferIA

══════════════════════════════════════════════════════
```

---

### 3B — Preview ME-sport (academias deportivas)

```
📋 ESTRUCTURA DE LA PROPUESTA — [NOMBRE]  ·  ME-sport
══════════════════════════════════════════════════════

SLIDE 1 — PORTADA
  Título: "Academia en Piloto Automático — [Nombre academia]"
  Subtítulo: [deporte/actividad] · [municipio]
  CTA: "Ver propuesta"

SLIDE 2 — DIAGNÓSTICO
  Score: [X]/100
  Problema principal: [descripción — ej: bajas no detectadas, altas manuales, impagos]
  3 gaps críticos: [lista adaptada a academia]
  Ej de gaps: sin recordatorios de pago / alta por WhatsApp manual / sin seguimiento de bajas

SLIDE 3 — META ADS (si aplica)
  [si hubo auditoría de Meta Ads — captación de nuevos alumnos]

SLIDE 4 — COSTE REAL DEL PROBLEMA
  Estimación de lo que cuesta la gestión manual mensualmente
  Ej: [X socios] × [% baja mensual] × [cuota media] = [€ perdidos en bajas/mes]
  Horas gestión manual × coste hora = [€ tiempo perdido/mes]

SLIDE 5 — LA SOLUCIÓN
  Qué automatiza el sistema:
  · Altas por WhatsApp — el socio se da de alta sin intervención humana
  · Recordatorios de pago — automáticos antes del vencimiento
  · Seguimiento de ausencias — detecta inactividad y reactiva al socio
  · Confirmación de clases — recordatorio 24h antes
  · Baja gestionada — proceso automatizado con encuesta de salida
  Canales: WhatsApp · Email (según plan)

SLIDE 6 — PLAN RECOMENDADO
  [Sprint IA / Equipo IA / Liga IA] — [precio] € (pago único)
  Qué incluye: [lista de deliverables del plan]
  [Si Liga IA: mencionar multi-sede y agente de voz]

SLIDE 7 — CUOTA MENSUAL
  Plan [Básico/Profesional/Avanzado] — [precio] €/mes
  Qué incluye: [X] h/mes ajustes, soporte [plazo], reportes mensuales de actividad

SLIDE 7B — MÓDULOS ADICIONALES (si se proponen)
  [módulo 1]: [precio] — qué incluye
  Ej habituales en academias: Gestión RRSS IA, Meta Ads captación alumnos
  Nota: contratos/anexos independientes

SLIDE 8 — INFRAESTRUCTURA Y COSTES
  Opción [A/B/C] — [explicación]
  Costes cliente directos: APIs IA, WhatsApp Business, dominio

SLIDE 9 — ROI PROYECTADO
  Retención: reducir baja mensual de [X%] a [Y%] = [€ retenidos/mes]
  Ahorro gestión: [X] horas/mes × [coste hora] = [€ ahorrados/mes]
  Recuperación inversión estimada: [N] meses

SLIDE 10 — SIGUIENTE PASO
  CTA + datos de contacto PalferIA

══════════════════════════════════════════════════════
```

---

Preguntar: **"¿Cambias algo? ¿Añado o quito algún slide? ¿Ajusto algún contenido?"**

Recoger correcciones. Aplicarlas al plan. Confirmar antes de generar.

**REGLA:** La propuesta NO incluye diagramas técnicos de flujo n8n ni paso a paso de implementación. Eso va en el setter tool. La propuesta habla de resultados y valor, no de tecnología.

---

## FASE 4 — Generar HTML de la propuesta

### Paso 4.1 — Generar slug único

```
[8 chars UUID]-[nombre-slug]
Ejemplo: b7f3c1a9-cortinajes-valls
```

### Paso 4.2 — Construir HTML (motor de slides)

**Estilo visual según proyecto:**
- COM-studio: acento teal `#0d9488` / `#14b8a6`, tipografía Playfair Display
- ME-sport: acento verde `#84cc16`, tipografía Inter

**Motor de slides** (igual que Cortinajes y Tecniluispa):
- Position-absolute, `opacity 0→1`, transición suave
- Navegación: flechas + teclado + swipe táctil
- Contador automático: `counterTotal.textContent = total` (no hardcodear)
- Responsive: breakpoints 480px y 900px, `100dvh` para iOS Safari
- Fondo: `#0a0f1a` oscuro

**Slides a construir** (según preview aprobado en Fase 3):

Cada slide tiene:
- `data-slide="N"` incremental
- `class="slide"` para el contador automático
- Contenido basado en los datos reales del prospecto

### Paso 4.3 — Guardar archivo

```
/Users/macbook/Desktop/workspace/palferia-sales-crm/public/propuestas/[slug].html
```

También guardar copia en:
```
/Users/macbook/Desktop/workspace/clientes/[proyecto]/[nombre-slug]/propuestas/propuesta-[nombre-slug]-palferia.html
```

### Paso 4.4 — Verificar antes de deploy

Abrir el archivo y confirmar:
- Número de slides correcto
- Contador funciona (auto-count, no hardcodeado)
- Precios correctos en cada slide
- Nombre del prospecto correcto en portada

---

## FASE 5 — Generar Setter Tool

El setter es la herramienta interna del setter (comercial). NO la ve el cliente.

**Contenido del setter** (basado en lo generado):

### Secciones obligatorias

**S1 — Resumen prospecto**
- Datos básicos + estado CRM + auditoría en 3 bullets
- Badge de estado (esperando / llamada / en reunión)

**S2 — Auditoría para dummies**
- Score + qué tiene / qué le falta / riesgo — en lenguaje simple
- Link al HTML de auditoría completa

**S-META — Meta Ads** (si hubo auditoría)
- 4 chips: anuncios activos / score landing / tracking / seguidores
- Argumento de venta listo para usar
- Gaps vs oportunidades
- Link al HTML de auditoría Meta Ads

**S3 — ROI**
- Cálculo pre-hecho del ROI del prospecto
- Calculadora interactiva con sliders editables

**S4 — Plan & Descuento**
- Los 3 planes con sus costes internos y floors
- Toggle setup/mensual
- Input descuento + slider sincronizado
- Semáforo verde/ámbar/rojo según margen
- Sección de módulos adicionales con sus márgenes:
  - Módulos propios (landing, SEO, GEO/AEO, RRSS, ChatGPT Ads): margen ~70-80%
  - Módulos subcontratados (Meta Ads, Google Ads): margen ~35-40%
  - Nota: presupuesto ads nunca cuenta como margen de PalferIA

```javascript
var PLANS = {
  // COM-studio:
  vecino:    { setup: 1200, mes: 0,   costeSetup: 550,  costesMes: 0,   floorSetup: 900,  floorMes: 0   },
  autopilot: { setup: 3100, mes: 499, costeSetup: 1400, costesMes: 180, floorSetup: 2400, floorMes: 380 },
  socio:     { setup: 4900, mes: 799, costeSetup: 2200, costesMes: 320, floorSetup: 3800, floorMes: 620 },
  // ME-sport:
  sprint:    { setup: 1800, mes: 0,   costeSetup: 800,  costesMes: 0,   floorSetup: 1400, floorMes: 0   },
  equipo:    { setup: 3500, mes: 499, costeSetup: 1600, costesMes: 180, floorSetup: 2700, floorMes: 380 },
  liga:      { setup: 5500, mes: 799, costeSetup: 2500, costesMes: 320, floorSetup: 4200, floorMes: 620 },
};
```

**S5 — Objeciones**
- Acordeón con las 5 objeciones más probables del sector
- Respuestas preparadas y específicas para este prospecto

**S6 — Tips negociación**
- Tácticas específicas según lo encontrado en la auditoría
- Señales de cierre a buscar
- Timing recomendado

**S7 — Entregables**
- Checklist de lo que incluye el plan seleccionado
- Estado / notas / fecha por ítem
- Persistido en localStorage

**S8 — Mapa del proceso**
- AS-IS (cómo lo hacen ahora) → TO-BE (cómo quedaría)
- Integraciones necesarias
- Persistido en localStorage

**S9 — Notas Gemini / Reunión**
- Si hay notas de reunión → cargarlas aquí
- Si no hay → placeholder con link a Drive search
- Zona de apuntes libres

**Estilo setter:** sidebar 240px fijo, acento ámbar `#f59e0b`, fondo `#0a0f1a`

**Guardar en:**
```
/Users/macbook/Desktop/workspace/palferia-sales-crm/public/setter/[slug].html
```

---

## FASE 6 — Deploy al VPS

```bash
# Propuesta
rsync -avz -e "ssh -i ~/.ssh/palferia_vps" \
  public/propuestas/[slug].html \
  root@31.97.192.164:/var/www/sales.palferia.me/propuestas/[slug].html

# Setter tool
rsync -avz -e "ssh -i ~/.ssh/palferia_vps" \
  public/setter/[slug].html \
  root@31.97.192.164:/var/www/sales.palferia.me/setter/[slug].html
```

Verificar HTTP 200:
```bash
curl -s -o /dev/null -w '%{http_code}' https://sales.palferia.me/propuestas/[slug].html
curl -s -o /dev/null -w '%{http_code}' https://sales.palferia.me/setter/[slug].html -u palferia:setter2024
```

---

## FASE 7 — Registrar en Supabase

### 7.1 — Crear o actualizar prospecto

Si el prospecto no existía:
```bash
curl -s -X POST \
  "https://aqaiqmsypbwhgknbbmae.supabase.co/rest/v1/prospectos" \
  -H "apikey: sb_secret_Jtsn1Qe7tWlMvWThaDOJfg_TpNUCOP2" \
  -H "Authorization: Bearer sb_secret_Jtsn1Qe7tWlMvWThaDOJfg_TpNUCOP2" \
  -H "Content-Type: application/json" \
  -H "Prefer: return=representation" \
  -d '{"nombre":"[NOMBRE]","municipio":"[MUN]","sector":"[SEC]","score":[SCORE],"web":"[WEB]","instagram":"[IG]","email":"[EMAIL]","pain":"[PAIN]","proyecto":"[PROYECTO]","estado":"proposal"}'
```

Si ya existía → actualizar estado a `proposal` y el score si cambió.

### 7.2 — Insertar propuesta

```bash
curl -s -X POST \
  "https://aqaiqmsypbwhgknbbmae.supabase.co/rest/v1/propuestas" \
  -H "apikey: sb_secret_Jtsn1Qe7tWlMvWThaDOJfg_TpNUCOP2" \
  -H "Authorization: Bearer sb_secret_Jtsn1Qe7tWlMvWThaDOJfg_TpNUCOP2" \
  -H "Content-Type: application/json" \
  -H "Prefer: return=representation" \
  -d '{
    "prospecto_id": "[ID]",
    "slug": "[SLUG]",
    "url": "https://sales.palferia.me/propuestas/[SLUG].html",
    "titulo": "[TITULO]",
    "estado": "borrador",
    "proyecto": "[PROYECTO]",
    "skills_usadas": ["kit-auditoria-negocio","kit-auditoria-meta-ads","kit-orquestador-propuestas"],
    "notas_internas": "Setter: https://sales.palferia.me/setter/[SLUG].html"
  }'
```

### 7.3 — Log de pipeline

```bash
curl -s -X POST \
  "https://aqaiqmsypbwhgknbbmae.supabase.co/rest/v1/pipeline_log" \
  -H "apikey: sb_secret_Jtsn1Qe7tWlMvWThaDOJfg_TpNUCOP2" \
  -H "Authorization: Bearer sb_secret_Jtsn1Qe7tWlMvWThaDOJfg_TpNUCOP2" \
  -H "Content-Type: application/json" \
  -d '{"prospecto_id":"[ID]","accion":"Propuesta generada via kit-orquestador","resultado":"[SLUG] — Plan [PLAN] — [PRECIO]€ setup + [PRECIO]€/mes","fecha":"[HOY]"}'
```

---

## FASE 8 — Resumen final

Mostrar al usuario:

```
✅ PROPUESTA LISTA — [NOMBRE NEGOCIO]
══════════════════════════════════════════════════════
🌐 Propuesta cliente:
   https://sales.palferia.me/propuestas/[SLUG].html

🔒 Setter tool (setter):
   https://sales.palferia.me/setter/[SLUG].html
   (contraseña: setter2024)

📋 Auditorías guardadas en:
   clientes/[proyecto]/[nombre-slug]/auditoria/

💾 Registrado en Supabase:
   Prospecto: [ID] → estado: proposal
   Propuesta: [ID] → slug: [SLUG]

💰 Resumen económico:
   Setup total:    [X.XXX] € (plan + módulos setup)
   Mensual total:  [XXX] €/mes (mantenimiento + módulos mensuales)
   Cliente asume:  [XXX] €/mes (APIs + presupuesto ads)

📅 Próxima acción sugerida:
   Enviar URL al prospecto + seguimiento en [X] días
══════════════════════════════════════════════════════
```

Preguntar: **"¿Quieres que actualice el CRM con la fecha de envío?"**

---

## Reglas del orquestador

1. **Nunca saltar fases** — cada fase tiene un preview que el usuario aprueba
2. **Nunca mezclar setup y mensual** — son dos líneas separadas siempre
3. **El plan recomendado se basa en la auditoría**, no en asumir presupuesto
4. **La propuesta no incluye diagramas de flujo técnico** — eso es del setter
5. **Los costes de API siempre se presentan como "asumidos por el cliente"**, nunca incluidos en el precio de PalferIA sin acuerdo explícito
6. **Infra opción B por defecto** — a menos que el cliente tenga VPS propio
7. **Preview conversacional obligatorio antes de generar HTML** — sin excepciones
8. **Si algo falla en el deploy** → informar y continuar con el resto. No bloquear
9. **El setter tool siempre se genera junto con la propuesta** — nunca uno sin el otro
10. **Guardar siempre copia local** en `clientes/[proyecto]/` además del deploy
11. **Módulos adicionales siempre en contrato/anexo separado** — nunca dentro del plan base
12. **El presupuesto de ads (Meta/Google/OpenAI) nunca se mezcla con el fee de gestión** — son líneas distintas en el resumen
13. **GEO/AEO y ChatGPT Ads ofrecerlos siempre** como diferenciadores — son los módulos con mayor margen y menor competencia en España
14. **Máximo 2-3 módulos en primera propuesta** — no saturar al cliente

---

## Condicionales de contenido

| Condición | Acción |
|-----------|--------|
| Sin web conocida | Slide 2 centrado en ausencia total de presencia digital + proponer módulo Landing/Web |
| Tiene web mala (score < 40) | Proponer módulo Landing page IA o Web corporativa IA |
| Tiene web, score > 60 | Slide 2 más enfocado en optimización que en creación |
| 0 anuncios Meta | Slide Meta Ads con argumento "doble problema" + proponer módulo Meta Ads |
| Tiene anuncios activos | Slide Meta Ads con análisis de rendimiento + proponer optimización |
| Sin presencia Google | Proponer módulo Google Ads como segundo módulo |
| Redes activas pero sin estrategia | Proponer módulo Gestión RRSS con IA |
| Opción B (hosting PalferIA) | Slide infraestructura con "todo gestionado" |
| Opción A (hosting propio) | Slide infraestructura omitido o breve |
| ME-sport | Planes Sprint/Equipo/Liga en vez de Vecino/Autopilot/Socio |
| Score < 35 | Plan más completo recomendado (Socio Digital / Liga IA) |
| Score 35-60 | Plan medio (Autopilot 30 / Equipo IA) |
| Score > 60 | Plan básico + upsell en módulos y mantenimiento |
| Cualquier prospecto (desde ago-2026) | Ofrecer siempre ChatGPT Ads como módulo diferenciador |
| Prospecto con competencia digital alta | Priorizar GEO/AEO — aparecer en IA antes que la competencia |
| Sector salud / legal / datos sensibles | Infra Opción C — no proponer ChatGPT Ads (datos sensibles) |
