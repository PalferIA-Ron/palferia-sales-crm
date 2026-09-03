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
  -H "apikey: $SUPABASE_SERVICE_KEY" \
  -H "Authorization: Bearer $SUPABASE_SERVICE_KEY"
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
`/Users/macbook/Desktop/workspace/palferia-sales-crm/ai/auditorias/kit-auditoria-negocio/SKILL.md`

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
`/Users/macbook/Desktop/workspace/palferia-sales-crm/ai/auditorias/kit-auditoria-meta-ads/SKILL.md`

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
`/Users/macbook/Desktop/workspace/palferia-sales-crm/ai/auditorias/kit-auditoria-seo/SKILL.md`

### 1.4 — Actualizar score en Supabase

Si el prospecto ya existía en Supabase, actualizar el score con el resultado de la auditoría:

```bash
curl -s -X PATCH \
  "https://aqaiqmsypbwhgknbbmae.supabase.co/rest/v1/prospectos?id=eq.[ID]" \
  -H "apikey: $SUPABASE_SERVICE_KEY" \
  -H "Authorization: Bearer $SUPABASE_SERVICE_KEY" \
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

### 3A — Preview COM-studio (negocios locales B2B)

> Framework Hormozi/StoryBrand: el cliente es el héroe, PalferIA es el guía.
> Los datos de auditoría se integran en el relato — no son slides técnicos.
> El diagnóstico alimenta "El Problema" y "Resultado"; el ROI alimenta "Inversión".

```
📋 ESTRUCTURA DE LA PROPUESTA — [NOMBRE]  ·  COM-studio
══════════════════════════════════════════════════════

SLIDE 1 — PORTADA
  Título: "[Nombre negocio] en piloto automático"
  Subtítulo: [sector] · [municipio]
  Badge: "Powered by COM-studio · PalferIA"
  CTA: "Ver propuesta"

SLIDE 2 — QUIÉN SOY (autoridad)
  PalferIA: especialistas en automatización IA para negocios locales en Valencia y España
  · [dato de credibilidad: proyectos entregados / sectores / resultado concreto]
  · Metodología propia: diagnóstico → implementación → entrega en [N] semanas
  · [si aplica: primeros en España gestionando anuncios en ChatGPT desde ago-2026]
  Adaptar con logros reales de Ronald. Sin clientes → usar "fase de validación con
  negocios de Horta Nord" y ser directo.

SLIDE 3 — EL PROBLEMA (su dolor, con sus palabras)
  Integrar aquí los gaps reales de la auditoría en lenguaje del cliente, no técnico:
  · "Recibes consultas por WhatsApp, Instagram y email — y ninguna tiene seguimiento"
  · "Tu web tiene [X visitas/mes] pero convierte [Y%] — los leads se pierden sin responder"
  · [gap específico de la auditoría: score bajo en SEO / sin pixel / sin anuncios activos]
  Coste invisible: [X leads/mes ignorados] × [ticket medio €] = [€ perdidos/año]
  Fuente: datos reales del diagnóstico de Fase 1.

SLIDE 4 — PARA QUIÉN ES (avatar COM-studio)
  "Esta propuesta es para ti si..."
  · Tienes un negocio local con [X-Y empleados / facturación >X€/año]
  · Recibes clientes por WhatsApp, teléfono o walk-in sin sistema
  · Pierdes leads por falta de respuesta rápida fuera del horario
  · Quieres crecer sin contratar más personal de atención
  "No es para ti si buscas solo una web bonita o gestión de redes sin estrategia"

SLIDE 5 — LA SOLUCIÓN / EL MÉTODO (en 3 pasos)
  Cómo trabajamos:
  1. Radiografía digital — analizamos tu presencia, tus canales y tus puntos de fuga.
     Sabrás exactamente dónde pierdes clientes y cuánto te cuesta.
  2. Implementación — desplegamos el agente IA en tus canales: responde en segundos,
     captura el lead, lo clasifica y te avisa. Sin código, sin fricción.
  3. Entrega + soporte — te entregamos el sistema funcionando y formamos a tu equipo.
     Ajustes incluidos [según plan].
  Canales según plan: WhatsApp · Web · Instagram · Email · Voz

SLIDE 6 — ENTREGABLES (lo que recibes)
  Plan [Vecino Digital / Autopilot 30 / Socio Digital] — checklist completo:
  [Usar lista de `_deliverables/COM-studio/deliverables-planes.md` según plan elegido]
  · Agente IA configurado y probado
  · Landing / web [si incluida en el plan]
  · Flujos de automatización [N flujos según plan]
  · Dashboard de leads
  · Formación [horas según plan]
  · Soporte [plazo según plan]

SLIDE 7 — PRUEBA / CASO REAL
  Si hay cliente → resultado con números:
  "[Nombre o "un negocio de [sector] en [municipio]"] redujo su tiempo de respuesta
  de [X horas] a [Y minutos] y capturó [Z leads adicionales/mes] en [N semanas]"
  Sin clientes → caso de ejemplo con honestidad:
  "Basado en negocios similares: un restaurante con 200 visitas/mes a su web
  y 0 seguimiento automatizado recupera entre 8 y 15 clientes/mes con este sistema"
  Fuente del caso Grupo Cueva disponible en `_deliverables/COM-studio/deliverables-planes.md`

SLIDE 8 — POR QUÉ NOSOTROS Y NO OTRO
  Lo que hace distinto a COM-studio:
  · Especialización local — conocemos el tejido empresarial de Valencia y Horta Nord
  · IA aplicada, no prometida — entregamos sistemas que funcionan el día 1
  · ChatGPT Ads 🆕 — somos de las primeras agencias en España que gestiona anuncios
    en ChatGPT (disponible desde ago-2026)
  · Precio justo con margen de negociación — setup único + cuota predecible, sin sorpresas
  · [diferenciador encontrado en auditoría: ej. "tu competencia más cercana no tiene pixel"]

SLIDE 9 — RESULTADO + PLAZO (antes vs después)
  ANTES (hoy — basado en diagnóstico, score [X]/100):
  · [gap 1 de la auditoría en lenguaje humano]
  · [gap 2]
  · [gap 3]
  · Estimación: [€ perdidos/mes sin automatización]

  DESPUÉS (con [plan] en [N] semanas):
  · Respuesta automática 24/7 en todos los canales
  · [X leads/mes capturados que hoy se pierden]
  · [reducción de tiempo gestión manual: Y horas/mes]
  · ROI estimado: inversión recuperada en [N] meses

SLIDE 10 — INVERSIÓN + SIGUIENTE PASO
  PAGO ÚNICO (setup):     [precio plan] €
  CUOTA MENSUAL:          [precio mantenimiento] €/mes
  [Módulos adicionales si aplica]
  Costes directos del cliente: APIs IA + WhatsApp Business [rangos]

  Lo que cuesta NO actuar: [€ perdidos/mes] × 12 = [€/año en oportunidades perdidas]

  SIGUIENTE PASO:
  "¿Empezamos? Una reunión de 30 min para validar el plan y dar el OK."
  CTA claro: [link Calendly / WhatsApp / email]
  Contacto: Ronald Palma · ronald@palferia.me

══════════════════════════════════════════════════════
```

---

### 3B — Preview ME-sport (academias y clubes deportivos)

> Mismo framework Hormozi/StoryBrand adaptado al deporte.
> El cliente (club/academia) es el héroe. El dolor es operacional y emocional.
> La cuota mensual es el núcleo de ingreso recurrente — presentarla como inversión, no gasto.

```
📋 ESTRUCTURA DE LA PROPUESTA — [NOMBRE]  ·  ME-sport
══════════════════════════════════════════════════════

SLIDE 1 — PORTADA
  Título: "[Nombre club/academia] en piloto automático"
  Subtítulo: [deporte/actividad] · [municipio]
  Badge: "Powered by ME-SportCenter · PalferIA"
  CTA: "Ver propuesta"

SLIDE 2 — QUIÉN SOY (autoridad)
  PalferIA ME-SportCenter: especialistas en automatización IA para el deporte en España
  · [dato de credibilidad: academias / clubes trabajados o en validación]
  · Entendemos el deporte desde dentro — gestión de socios, cuotas, eventos, captación
  · No vendemos apps genéricas — construimos sistemas a medida para tu tipo de club
  Adaptar con logros reales. Sin clientes deportivos → validación con clubes de Horta Nord.

SLIDE 3 — EL PROBLEMA (su dolor, con sus palabras)
  Integrar gaps reales de la auditoría en lenguaje del entrenador/director, no técnico:
  · [Si academia]: "Das de alta nuevos alumnos por WhatsApp, cobras por Bizum y te
    enteras de las bajas cuando el alumno lleva 3 semanas sin venir"
  · [Si club]: "Gestionas [X socios] con un grupo de WhatsApp, una hoja de Excel
    y la memoria — y aun así se te escapan impagos cada mes"
  · [Si evento]: "Organizas el torneo en 4 grupos de WhatsApp distintos y el día del
    evento hay 3 equipos que no saben el horario"
  Coste real: [X socios] × [% baja] × [cuota media] = [€ perdidos/mes en bajas silenciosas]
  + [horas/mes en gestión manual] × [coste hora estimado] = [€ tiempo perdido/mes]

SLIDE 4 — PARA QUIÉN ES (avatar ME-sport)
  "Esta propuesta es para ti si..."
  · Gestionas entre [X y Y socios / N equipos / Z eventos al año]
  · Tu administración vive en WhatsApp + Excel + notas de papel
  · Pierdes socios sin saber por qué y sin poder reactivarlos a tiempo
  · Quieres crecer en socios sin contratar más administrativo
  · [Si federación/evento]: coordinas múltiples clubes o sedes sin sistema central
  "No es para ti si ya tienes WodBuster/Clupik cubriendo todo — nosotros complementamos,
  no sustituimos plataformas deportivas existentes"

SLIDE 5 — LA SOLUCIÓN / EL MÉTODO (en 3 pasos)
  Cómo trabajamos:
  1. Diagnóstico de operaciones — mapeamos cómo gestionas hoy: altas, bajas, pagos,
     comunicación, eventos. Identificamos qué automatizamos primero y qué ahorra más.
  2. Implementación — desplegamos los flujos en tus canales:
     · Altas automatizadas por WhatsApp — sin intervención tuya
     · Recordatorios de pago — antes del vencimiento, no después del impago
     · Detección de inactividad — el sistema te avisa antes de que el socio se vaya
     · Confirmaciones de clase — recordatorio 24h antes, 0 no-shows
     · Gestión de baja — encuesta automática, aprende por qué se van
  3. Entrega + soporte mensual — sistema funcionando + ajustes [según plan] + reporting.

SLIDE 6 — ENTREGABLES (lo que recibes)
  Plan [Sprint IA / Equipo IA / Liga IA] — checklist completo:
  [Usar lista de `_deliverables/ME-SportCenter/deliverables-planes.md` según plan y vertical]
  Adaptar según tipo de cliente:
  · Academia → flujos inscripción + pagos + seguimiento alumnos
  · Club → gestión socios + cuotas + eventos + comunicación
  · Evento → registro equipos + logística + comunicación día D
  · Federación → visibilidad multi-club + reporting centralizado

SLIDE 7 — PRUEBA / CASO REAL
  Si hay cliente → resultado con números:
  "[Nombre o 'una academia de [deporte] en [ciudad]'] redujo sus bajas de [X%] a [Y%]
  y recuperó [€ Z/mes] en cuotas que antes se perdían por falta de seguimiento"
  Sin clientes deportivos → caso de ejemplo con honestidad:
  "Basado en academia tipo con 120 socios y 8% de baja mensual:
  → Reducir baja a 5% = 4 socios retenidos × 50€ cuota = 200€/mes recuperados
  → Ahorro gestión: 10h/mes × 15€/h = 150€/mes en tiempo del director
  → Total: 350€/mes recuperados con un sistema que cuesta [X€/mes]"

SLIDE 8 — POR QUÉ NOSOTROS Y NO OTRO
  Lo que hace distinto a ME-SportCenter:
  · No somos WodBuster ni Clupik — los complementamos, no competimos con ellos
  · IA aplicada al deporte, no tecnología genérica — sabemos cómo piensa un director
    de academia y cómo se comporta un socio que está a punto de darse de baja
  · Retainer mensual, no proyecto único — estamos contigo a largo plazo, el sistema
    mejora cada mes con los datos reales de tu club
  · Especialización local — conocemos el deporte amateur en Valencia y España
  · [diferenciador específico del prospecto: ej. "eres el único club de [deporte] en
    [municipio] — esa exclusividad la aprovechamos para captación"]

SLIDE 9 — RESULTADO + PLAZO (antes vs después)
  ANTES (hoy):
  · [gap 1 en lenguaje humano — de la auditoría]
  · [gap 2]
  · [gap 3]
  · Estimación de coste mensual del caos: [€/mes]

  DESPUÉS (con [plan] en [N] semanas):
  · Altas y bajas gestionadas sin WhatsApp manual
  · Reducción de baja estimada: de [X%] a [Y%] = [€ retenidos/mes]
  · Ahorro gestión: [N horas/mes] = [€ tiempo recuperado]
  · Reportes automáticos — sabes en tiempo real el estado de tu club
  · Plazo de implementación: [4–8 semanas según plan]

SLIDE 10 — INVERSIÓN + SIGUIENTE PASO
  CUOTA MENSUAL (retainer):   [precio plan] €/mes — contrato mensual renovable
  [Setup si aplica según plan]
  [Módulos adicionales: captación RRSS, Meta Ads, eventos]
  Costes directos del cliente: APIs IA + WhatsApp Business [rangos]

  Lo que cuesta NO actuar: [€/mes perdidos en bajas + gestión manual] × 12 = [€/año]

  SIGUIENTE PASO:
  "¿Empezamos? Una sesión de diagnóstico gratuita de 30 min — sin compromiso.
  Saldrás con el mapa de qué automatizamos primero y cuánto recuperas."
  CTA: [link Calendly / WhatsApp / email]
  Contacto: Ronald Palma · ronald@palferia.me

══════════════════════════════════════════════════════
```

---

### 3C — Preview DraftDayES (SaaS deportivo — early adopters)

> **Nota:** DraftDayES usa un framework de propuesta distinto al de agencia (3A/3B).
> El objetivo no es vender un servicio — es convencer a un club/academia/federación
> de ser early adopter de un SaaS. La propuesta habla de visión + tracción + acceso exclusivo.
> Branding: "Powered by PalferIA" (no COM-studio ni ME-sport directamente).

```
📋 ESTRUCTURA DE LA PROPUESTA — [NOMBRE]  ·  DraftDayES
══════════════════════════════════════════════════════

SLIDE 1 — PORTADA
  Título: "El sistema operativo de tu club — [Nombre club/academia/federación]"
  Subtítulo: [deporte] · [municipio] · Acceso Early Adopter
  Badge: "Powered by PalferIA"
  CTA: "Ver propuesta"

SLIDE 2 — QUIÉN SOY (autoridad)
  Por qué confiar en PalferIA + DraftDayES:
  · [experiencia relevante: automatización IA aplicada al deporte]
  · [dato o logro: ej. "hemos automatizado la gestión de X clubes en Valencia"]
  · [formación / enfoque]: especialistas en IA aplicada al ecosistema deportivo
  Nota al orquestador: adaptar con datos reales de Ronald. Si no hay clientes deportivos
  aún → usar "construcción con validación de [N] clubes en Horta Nord" y ser honesto.

SLIDE 3 — EL PROBLEMA (su dolor, con sus palabras)
  2-3 dolores concretos del avatar según el tipo de prospecto:
  · [Si club/academia]: "Gestionas las inscripciones por WhatsApp, los pagos por
    transferencia y las bajas por silencio — y cada mes pierdes socios sin saber por qué"
  · [Si organizador eventos]: "Montas el torneo en 4 grupos de WhatsApp, un Excel y
    rezas para que nadie se confunda con el horario"
  · [Si federación]: "Tienes 40 clubes afiliados y ningún sistema que te diga en tiempo
    real cuántos socios activos hay en tu federación"
  Adaptar los 2-3 más relevantes según el perfil del prospecto.

SLIDE 4 — PARA QUIÉN ES (avatar)
  "DraftDayES es para ti si..."
  · Gestionas [X–Y socios / N equipos / Z eventos al año]
  · Hoy usas Excel + WhatsApp + formularios de papel
  · Quieres crecer sin contratar más personal administrativo
  · Eres de los primeros en tu liga en apostar por la tecnología
  "No es para ti si buscas solo una app de fichajes o un gestor básico de cuotas"

SLIDE 5 — LA SOLUCIÓN / EL MÉTODO (en pasos)
  Cómo funciona DraftDayES en 3 pasos:
  1. Diagnóstico digital — mapeamos cómo gestionas hoy: inscripciones, pagos,
     comunicación, eventos. Identificamos qué se automatiza primero.
  2. Implementación — configuramos el sistema para tu club: flujos de alta/baja,
     recordatorios de pago, gestión de eventos, comunicación automática.
  3. Entrega + autonomía — tu equipo opera sin depender de nosotros.
     El sistema aprende con el uso y mejora solo.
  Canales integrados: WhatsApp · Email · Web · (según plan)

SLIDE 6 — ENTREGABLES (lo que recibes)
  Según el plan seleccionado:
  · [Plan Fase 1 / Early Adopter / Pro — completar cuando precios estén cerrados]
  Lista concreta basada en `_deliverables/ME-SportCenter/deliverables-planes.md`
  Adaptar según si es club, academia, evento o federación.
  Incluir siempre: onboarding guiado, soporte directo con Ronald, acceso prioritario
  a nuevas funciones como early adopter.

SLIDE 7 — PRUEBA / CASO REAL
  Si hay cliente real → resultado con números: "reducimos las bajas de [X%] a [Y%]
  en [N] meses en [tipo de club]"
  Si no hay aún → caso de ejemplo con honestidad:
  "Trabajando con [tipo de club similar] en fase beta, el resultado esperado es:
  [X horas/mes ahorradas en gestión] · [Y% reducción bajas] · [Z€ recuperados/mes]"
  Nota: ser transparente sobre el estado early adopter — es un diferenciador, no una debilidad.

SLIDE 8 — POR QUÉ NOSOTROS Y NO OTRO
  Lo que hace distinto a DraftDayES + PalferIA:
  · No es una app genérica — está construida específicamente para el ecosistema deportivo
  · IA nativa desde el primer día — no es un Excel con automatizaciones, es un sistema
    que aprende
  · Acceso early adopter — precio especial, influencia directa en el roadmap,
    soporte directo con el fundador
  · Especialización local — entendemos cómo funciona el deporte amateur en España
  · [diferenciador específico encontrado en la auditoría del prospecto]

SLIDE 9 — RESULTADO + PLAZO (antes vs después)
  ANTES (hoy): [descripción de cómo gestiona el prospecto actualmente — basado en auditoría]
  · WhatsApp + Excel + llamadas manuales
  · [X horas/semana perdidas en administración]
  · [Y% bajas sin detectar / Z pagos tardíos / N torneos con caos logístico]

  DESPUÉS (con DraftDayES en [N] semanas):
  · Altas y bajas automatizadas — 0 intervención manual
  · Pagos recordados automáticamente — reduce morosidad [X%]
  · Eventos gestionados desde un dashboard — sin grupos de WhatsApp paralelos
  · Plazo de implementación: [4–8 semanas según plan]

SLIDE 10 — INVERSIÓN + SIGUIENTE PASO
  [Precio o rango según plan — completar cuando pricing DraftDayES esté cerrado]
  Modalidad early adopter: [precio especial] + acceso prioritario a roadmap
  Precio de referencia post-lanzamiento: [precio target] — asegura el tuyo ahora.

  SIGUIENTE PASO:
  "¿Comenzamos? Reserva una sesión de diagnóstico gratuita de 30 minutos.
  Sin compromiso — saldrás con el mapa exacto de qué automatizamos primero."
  CTA: [link Calendly o WhatsApp directo]
  Contacto: Ronald Palma · ronald@palferia.me · wa.me/[número]

══════════════════════════════════════════════════════
```

> **Nota de precios DraftDayES:** El pricing está en definición (freemium → pro → enterprise).
> Hasta que esté cerrado, usar rangos orientativos o "precio early adopter a definir en reunión".
> No bloquear la propuesta por falta de precio — la reunión de diagnóstico es el CTA real.

---

Preguntar: **"¿Cambias algo? ¿Añado o quito algún slide? ¿Ajusto algún contenido?"**

Recoger correcciones. Aplicarlas al plan. Confirmar antes de generar.

**REGLA:** La propuesta NO incluye diagramas técnicos de flujo n8n ni paso a paso de implementación. Eso va en el setter tool. La propuesta habla de resultados y valor, no de tecnología.

---

## FASE 4 — Generar HTML de la propuesta

> **Skill de diseño activa:** Antes de construir cualquier HTML, leer y aplicar
> `ai/tools/kit-diseno-web/SKILL.md`. Esa skill define paletas, tipografías,
> anti-patrones, proceso de dos pasos y el rol del agente en webs de cliente.

### Paso 4.1 — Generar slug único

```
[8 chars UUID]-[nombre-slug]
Ejemplo: b7f3c1a9-cortinajes-valls
```

### Paso 4.1B — Plan de diseño (proceso de dos pasos del kit-diseno-web)

Antes de escribir HTML, mostrar el plan de diseño según el proyecto:

```
🎨 PLAN DE DISEÑO — [NOMBRE] · [proyecto]
══════════════════════════════════════════
PALETA:     [según sistema PalferIA del proyecto]
TIPOGRAFÍA: [según proyecto — Playfair+Inter / Inter / Space Grotesk]
SIGNATURE:  [el elemento memorable de esta propuesta concreta]
            Ej: animación del dato clave de ROI / contador de leads /
                color del sector del cliente en el slide de diagnóstico
QUÉ EVITAMOS: [los 3 clichés más probables para este sector]
══════════════════════════════════════════
¿Apruebas el plan o ajustamos algo?
```

Esperar confirmación antes de generar el HTML.

### Paso 4.2 — Construir HTML (motor de slides)

**Estilo visual según proyecto** (del kit-diseno-web):
- COM-studio: `#0d9488`/`#14b8a6`, Playfair Display (display) + Inter (cuerpo)
- ME-sport: `#84cc16`, Inter 900 en headlines, bold agresivo
- DraftDayES: `#6366f1`/`#f97316`, Space Grotesk + Inter

**Motor de slides:**
- Position-absolute, `opacity 0→1`, transición suave
- Navegación: flechas + teclado + swipe táctil
- Contador automático: `counterTotal.textContent = total` (nunca hardcodear)
- Responsive: breakpoints 480px y 900px, `100dvh` para iOS Safari
- Fondo: `#0a0f1a` oscuro

**Slides a construir** (según preview aprobado en Fase 3):

Cada slide tiene:
- `data-slide="N"` incremental
- `class="slide"` para el contador automático
- Contenido basado en los datos reales del prospecto
- El slide de inversión (slide 10) incluye siempre el widget/CTA del agente

### Paso 4.2B — Si el plan incluye landing page para el cliente

Cuando el plan elegido incluye landing page (Autopilot 30, Socio Digital, Equipo IA, Liga IA),
generar también la landing usando la estructura del kit-diseno-web:

- Aplicar la estructura de 7 secciones (Hero → Agente → Problema → Método → Sector → Prueba → CTA)
- El agente IA integrado es el protagonista visual — widget WhatsApp flotante incluido
- Adaptar conversaciones de ejemplo al sector real del cliente
- Guardar en: `clientes/[proyecto]/[nombre-slug]/landing/landing-[nombre-slug].html`

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

**S7 — Entregables** (3 bloques independientes, cada uno con su checklist)

Leer primero el archivo de referencia según proyecto:
- COM-studio → `_deliverables/COM-studio/deliverables-planes.md`
- ME-sport → `_deliverables/ME-SportCenter/deliverables-planes.md`

Construir los 3 bloques según lo propuesto en Fase 2:

**S7A — Plan de setup** (pago único)
- Título: "Plan [Vecino Digital / Autopilot 30 / Socio Digital / Sprint IA / Equipo IA / Liga IA] — [precio]€"
- Checklist de todos los entregables del plan elegido (tomados del archivo `_deliverables/`)
- Cada ítem: ☐ nombre del entregable · campo notas · campo fecha estimada
- Badge de estado por ítem: pendiente / en progreso / entregado
- Persistido en localStorage

**S7B — Cuota mensual** (solo si el cliente eligió mantenimiento)
- Título: "Mantenimiento [Básico / Profesional / Avanzado] — [precio]€/mes"
- Checklist de lo que incluye la cuota: horas de ajuste, tipo de soporte, reporting, revisiones
- Referencia: precios y contenidos en `kit-pricing-planes` y en `_deliverables/`
- Cada ítem: ☐ descripción · frecuencia (mensual/quincenal/semanal)
- Persistido en localStorage

**S7C — Servicios adicionales** (solo los propuestos en Fase 2, pueden ser 0)
- Mostrar solo si se propusieron módulos adicionales en la propuesta
- Un bloque por cada servicio mensual activo:
  - Meta Ads gestión: ☐ [precio]€/mes · presupuesto ads: [X]€/mes directo al cliente
  - Google Ads gestión: ☐ [precio]€/mes · presupuesto ads: [X]€/mes directo al cliente
  - Gestión RRSS IA: ☐ [precio]€/mes · [N] publicaciones/semana · plataformas
  - SEO local: ☐ [precio]€/mes · objetivos acordados
  - GEO/AEO: ☐ [precio]€/mes
  - ChatGPT Ads: ☐ [precio]€/mes · presupuesto OpenAI: [X]€/mes directo al cliente
- Recordatorio visible: "El presupuesto de ads lo paga el cliente directamente — no es margen PalferIA"
- Persistido en localStorage

**Total mensual consolidado** (al final de S7):
```
Mantenimiento [plan]:        [XXX] €/mes
[Servicio adicional 1]:      [XXX] €/mes
[Servicio adicional 2]:      [XXX] €/mes
────────────────────────────────────
TOTAL MENSUAL PALFERIA:      [X.XXX] €/mes
+ Costes directos cliente:   [ads + APIs] €/mes (fuera de nuestro cobro)
```

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
  -H "apikey: $SUPABASE_SERVICE_KEY" \
  -H "Authorization: Bearer $SUPABASE_SERVICE_KEY" \
  -H "Content-Type: application/json" \
  -H "Prefer: return=representation" \
  -d '{"nombre":"[NOMBRE]","municipio":"[MUN]","sector":"[SEC]","score":[SCORE],"web":"[WEB]","instagram":"[IG]","email":"[EMAIL]","pain":"[PAIN]","proyecto":"[PROYECTO]","estado":"proposal"}'
```

Si ya existía → actualizar estado a `proposal` y el score si cambió.

### 7.2 — Insertar propuesta

```bash
curl -s -X POST \
  "https://aqaiqmsypbwhgknbbmae.supabase.co/rest/v1/propuestas" \
  -H "apikey: $SUPABASE_SERVICE_KEY" \
  -H "Authorization: Bearer $SUPABASE_SERVICE_KEY" \
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
  -H "apikey: $SUPABASE_SERVICE_KEY" \
  -H "Authorization: Bearer $SUPABASE_SERVICE_KEY" \
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
