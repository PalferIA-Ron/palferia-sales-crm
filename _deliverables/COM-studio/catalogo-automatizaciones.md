# Catálogo de Automatizaciones — PalferIA Studio
> Referencia interna de pricing y asignación de automatizaciones por plan.
> Última revisión: 2026-08-28

---

## METODOLOGÍA DE COSTE

| Concepto | Valor |
|----------|-------|
| Tarifa mercado (precio cliente) | 60 €/h |
| Tarifa interna Ronald (floor real) | 40 €/h |
| Margen de negociación | ~33% |
| Suscripción La Tribu Divisual | 130 €/mes (coste fijo, se amortiza con escala) |

**Cómo se calcula el precio de cada automatización:**
- Horas setup (adaptación al cliente) + horas reunión BPM = total horas
- Precio tarifa mercado = total horas × 60 €/h
- Floor = total horas × 40 €/h
- La suscripción La Tribu se distribuye como overhead, no se repercute directamente

**Regla clave:** Las automatizaciones son rentables dentro de planes (el cliente paga el plan,
las automatizaciones están incluidas y el coste de setup está absorbido). Vendidas standalone,
el floor mínimo es 800 € — por debajo de eso se trabaja a pérdida.

---

## CATÁLOGO COMPLETO

---

### 1 — Recepcionista WhatsApp
**Archivo:** `Recepcionista/Clínica Dental - Recepcionista WhatsApp.json`
**Descripción:** Agente IA que atiende consultas, agenda citas y responde FAQs por WhatsApp 24/7. Origen: clínica dental, adaptable a cualquier negocio con citas.
**Complejidad:** Simple
**Horas:** 16h setup + 4h BPM = 20h
**Precio standalone:** 1.200 €  |  **Floor:** 800 €
**Sectores:** Clínicas, academias deportivas, centros de estética, restaurantes, servicios con cita previa
**Plan COM-studio:** Vecino Digital (componente principal)
**Plan ME-sport:** Sprint IA (componente principal)
**Coste suscripción:** No aplica (workflow propio adaptado)
**Nota:** El más versátil del catálogo. Primer candidato a incluir en cualquier propuesta.

---

### 2 — Recordatorios Automáticos
**Archivo:** `Recepcionista/Clínica Dental - Recordatorios Automáticos.json`
**Descripción:** Secuencia automática de recordatorios: 24h antes de cita, día de evento, pago pendiente. Reduce no-shows y morosos sin intervención manual.
**Complejidad:** Simple
**Horas:** 16h setup + 4h BPM = 20h
**Precio standalone:** 1.200 €  |  **Floor:** 800 €
**Sectores:** Cualquier negocio con citas, eventos, cuotas periódicas
**Plan COM-studio:** Vecino Digital (flujo complementario)
**Plan ME-sport:** Sprint IA (flujo core para academias y clubs)
**Nota:** Habitualmente se vende junto al Recepcionista WA como pack base.

---

### 3 — Agente Google Reviews
**Archivo:** `Agente Google Reviews.json`
**Descripción:** Detecta nuevas reseñas en Google My Business, genera respuesta personalizada con IA y la publica automáticamente. Mantiene la reputación online sin trabajo manual.
**Complejidad:** Simple
**Horas:** 16h setup + 4h BPM = 20h
**Precio standalone:** 1.200 €  |  **Floor:** 800 €
**Sectores:** Cualquier negocio con presencia en Google (especialmente hostelería, clínicas, comercios)
**Plan COM-studio:** Autopilot 30 (uno de los 3 flujos core)
**Plan ME-sport:** Equipo IA (add-on reputación)
**APIs cliente:** Google My Business API (gratuita con cuenta Google)

---

### 4 — MCP Server Email
**Archivo:** `MCP_Server___Email.json`
**Descripción:** Servidor MCP que conecta agentes IA con el email del cliente. Permite al agente leer, clasificar y responder emails automáticamente según reglas de negocio.
**Complejidad:** Simple
**Horas:** 16h setup + 4h BPM = 20h
**Precio standalone:** 1.200 €  |  **Floor:** 800 €
**Sectores:** Negocios con alto volumen de email entrante (agencias, despachos, e-commerce)
**Plan COM-studio:** Autopilot 30 (integración canal email)
**Plan ME-sport:** Equipo IA
**APIs cliente:** Gmail API o SMTP/IMAP del cliente

---

### 5 — MCP Server Google Calendar
**Archivo:** `MCP_Server___Google_Calendar.json`
**Descripción:** Servidor MCP que da al agente IA acceso al calendario del cliente. El agente puede consultar disponibilidad, crear eventos y gestionar agenda sin intervención humana.
**Complejidad:** Simple
**Horas:** 16h setup + 4h BPM = 20h
**Precio standalone:** 1.200 €  |  **Floor:** 800 €
**Sectores:** Servicios profesionales con agenda (clínicas, consultoras, academias, coaches)
**Plan COM-studio:** Vecino Digital (si el negocio agenda citas) / Autopilot 30
**Plan ME-sport:** Sprint IA (gestión de horarios de clases)
**APIs cliente:** Google Calendar API (gratuita con cuenta Google)
**Nota:** Habitualmente se combina con Recepcionista WA — el agente agenda en el calendario directamente desde el chat.

---

### 6 — Publicador Instagram
**Archivo:** `Publicador Insta Link By La Tribu Divisual.json`
**Descripción:** Publica automáticamente en Instagram según un calendario editorial. Genera o recibe el contenido y programa publicaciones sin intervención manual.
**Complejidad:** Simple-Media
**Horas:** 18h setup + 4h BPM = 22h
**Precio standalone:** 1.320 € → **1.500 €**  |  **Floor:** 880 €
**Sectores:** Cualquier negocio con Instagram activo
**Plan COM-studio:** Autopilot 30 (bono kit contenido 30 días) / Socio Digital
**Plan ME-sport:** Equipo IA (marketing digital activo)
**APIs cliente:** Instagram Graph API (requiere cuenta Meta Business verificada)
**Origen:** La Tribu Divisual (incluido en suscripción 130€/mes)

---

### 7 — Agente Prospección Email Scrapper
**Archivo:** `Prospeccion_agentes/v2 Agente Email Scrapper - Conseguir Clientes.json`
**Descripción:** Automatiza la búsqueda de prospectos y extrae emails de contacto de forma sistemática. Alimenta el pipeline de ventas sin prospección manual.
**Complejidad:** Media
**Horas:** 20h setup + 4h BPM = 24h
**Precio standalone:** 1.440 € → **1.500 €**  |  **Floor:** 960 €
**Sectores:** Cualquier negocio que necesite captación B2B activa
**Plan COM-studio:** Autopilot 30 (sistema captación automática)
**Plan ME-sport:** Equipo IA (captación nuevos socios)
**Plan DraftDayES:** Early adopter outreach
**Nota:** Uso interno también — el kit-prospeccion del CRM usa lógica similar.

---

### 8 — Agente Icebreaker (conseguir clientes)
**Archivo:** `Prospeccion_agentes/Agente Icebreaker - Conseguir Clientes.json`
**Descripción:** Genera mensajes de primer contacto personalizados para cada prospecto. Combina datos del prospecto con el pitch de la empresa para crear icebreakers que convierten.
**Complejidad:** Media
**Horas:** 20h setup + 4h BPM = 24h
**Precio standalone:** 1.440 € → **1.500 €**  |  **Floor:** 960 €
**Sectores:** Negocios con venta B2B activa, agencias, consultoras
**Plan COM-studio:** Autopilot 30 / Socio Digital (captación outbound)
**Plan DraftDayES:** Captación early adopters
**Origen:** La Tribu Divisual

---

### 9 — Agente Instagram PalferIA
**Archivo:** `Redes sociales/Agente instagram palferia.json`
**Descripción:** Gestión IA de Instagram: responde DMs, comenta en posts relevantes, monitoriza menciones y actúa según reglas de engagement configuradas para el cliente.
**Complejidad:** Media
**Horas:** 20h setup + 4h BPM = 24h
**Precio standalone:** 1.440 € → **1.500 €**  |  **Floor:** 960 €
**Sectores:** Negocios con comunidad en Instagram (deportes, retail, hostelería, academia)
**Plan COM-studio:** Socio Digital (sistema omnicanal)
**Plan ME-sport:** Equipo IA / Liga IA
**APIs cliente:** Instagram Graph API

---

### 10 — Automatiza Contenido RRSS con IA
**Archivo:** `Redes sociales/Automatiza el contenido de las redes sociales con IA.json`
**Descripción:** Pipeline completo de generación de contenido: tema → copy → imagen → publicación. Produce contenido para redes con la voz y oferta del cliente de forma continua.
**Complejidad:** Media
**Horas:** 20h setup + 5h BPM = 25h
**Precio standalone:** 1.500 €  |  **Floor:** 1.000 €
**Sectores:** Cualquier negocio que necesite presencia activa en redes
**Plan COM-studio:** Autopilot 30 (bono contenido) / Socio Digital
**Plan ME-sport:** Equipo IA (marketing digital activo)
**APIs cliente:** Tokens IA (Claude/OpenAI) + plataforma de publicación

---

### 11 — LinkedIn Automático
**Archivo:** `LinkedIn/LinkedIn Automático By La Tribu.json`
**Descripción:** Automatiza la presencia en LinkedIn: publica contenido según calendario, gestiona conexiones y mantiene el perfil activo sin trabajo manual.
**Complejidad:** Media
**Horas:** 20h setup + 4h BPM = 24h
**Precio standalone:** 1.440 € → **1.500 €**  |  **Floor:** 960 €
**Sectores:** Negocios B2B, consultoras, despachos, agencias, profesionales con marca personal
**Plan COM-studio:** Socio Digital (omnicanal B2B)
**Plan DraftDayES:** Captación early adopters e inversores
**Origen:** La Tribu Divisual
**APIs cliente:** LinkedIn API (requiere cuenta LinkedIn Premium o Sales Navigator)

---

### 12 — Blog SEO-GPT
**Carpeta:** `Blog SEO -GPT/`
**Archivos:** `blog-seo-agent_CLAUDE.md` + `blog-seo-agent_matriz-de-decision.md` + docs completas
**Descripción:** Agente IA completo para generación de artículos SEO. Investiga keywords, genera contenido optimizado y publica en la web del cliente de forma automatizada.
**Complejidad:** Compleja (tiene documentación propia + CLAUDE.md + matriz de decisión)
**Horas:** 24h setup + 6h BPM = 30h
**Precio standalone:** 1.800 €  |  **Floor:** 1.200 €
**Sectores:** Cualquier negocio que quiera posicionamiento orgánico (especialmente local)
**Plan COM-studio:** Socio Digital (SEO activo incluido como módulo add-on en realidad)
**Módulo adicional COM-studio:** SEO Básico 500€/mes (este agente es la herramienta)
**Nota:** Tiene documentación suficiente para entregarlo con autonomía al cliente.

---

### 13 — AutoShorts
**Archivo:** `AutoShorts - La Tribu Divisual.json`
**Descripción:** Genera automáticamente vídeos cortos (Reels, TikTok, YouTube Shorts) a partir de contenido existente o guiones generados por IA.
**Complejidad:** Compleja
**Horas:** 24h setup + 6h BPM = 30h
**Precio standalone:** 1.800 €  |  **Floor:** 1.200 €
**Sectores:** Negocios con estrategia de vídeo (academia deportiva, restaurante, e-commerce)
**Plan COM-studio:** Socio Digital (kit contenido mes)
**Plan ME-sport:** Liga IA (contenido deportivo viral)
**APIs cliente:** Tokens IA + plataforma de vídeo (Runway, Kling, etc.)
**Origen:** La Tribu Divisual
**Nota:** Wan 2.5 (`Wan 2.5 La Tribu Divisual.json`) es la alternativa open-source — misma función, sin coste de API de vídeo pero requiere GPU.

---

### 14 — Indexador RAG Avanzado
**Archivo:** `Indexador_de_datos_RAG_Avanzado.json`
**Descripción:** Sistema de indexación y consulta de documentos internos del cliente. El agente IA responde preguntas sobre el contenido de PDFs, manuales, contratos o bases de datos internas.
**Complejidad:** Compleja (requiere recopilar y estructurar documentación interna del cliente)
**Horas:** 24h setup + 6h BPM = 30h
**Precio standalone:** 1.800 €  |  **Floor:** 1.200 €
**Sectores:** Despachos legales, clínicas, academias con mucho material formativo, e-commerce con catálogo amplio
**Plan COM-studio:** Socio Digital (agente IA personalizado de la marca)
**Plan ME-sport:** Liga IA (reglamentos, fichas, historial de socios)
**APIs cliente:** Tokens IA (consumo alto en indexación inicial)

---

### 15 — AI Real Estate Agent v2
**Carpeta:** `sist_automatico_inmmbiliaria/`
**Archivos:** 4 flujos n8n + documentación técnica + guía comercial completas
**Descripción:** Sistema de 4 flujos para agencias inmobiliarias: captación de leads, calificación automática, seguimiento y gestión de visitas. El más documentado del catálogo.
**Complejidad:** Multi-flujo (4 flujos interconectados)
**Horas:** 30h setup + 8h BPM = 38h
**Precio standalone:** 2.280 € → **2.500 €**  |  **Floor:** 1.520 €
**Sectores:** Exclusivo inmobiliaria (no adaptable a otros sin rediseño)
**Plan COM-studio:** No entra en planes estándar — es un sistema vertical propio
**Vertical propia:** Inmobiliaria → presupuesto a medida (2.500€ setup + retainer)
**Nota:** Tiene guía comercial lista (`AI_Real_Estate_Agent_GUIA_COMERCIAL.rtf`) — revisar antes de usar en propuesta.

---

## RESUMEN — MAPA DE PLANES

| Automatización | Vecino Digital | Autopilot 30 | Socio Digital | Sprint ME | Equipo ME | Liga ME | Standalone |
|---------------|:--------------:|:------------:|:-------------:|:---------:|:---------:|:-------:|:----------:|
| Recepcionista WA | ✅ principal | ✅ incluido | ✅ incluido | ✅ principal | ✅ incluido | ✅ incluido | 1.200 € |
| Recordatorios | ✅ complemento | ✅ incluido | ✅ incluido | ✅ core | ✅ incluido | ✅ incluido | 1.200 € |
| Google Reviews | — | ✅ flujo core | ✅ incluido | — | ✅ add-on | ✅ incluido | 1.200 € |
| MCP Email | — | ✅ integración | ✅ incluido | — | ✅ incluido | ✅ incluido | 1.200 € |
| MCP Calendar | ✅ si agenda citas | ✅ incluido | ✅ incluido | ✅ horarios | ✅ incluido | ✅ incluido | 1.200 € |
| Publicador Instagram | — | ✅ bono contenido | ✅ incluido | — | ✅ marketing | ✅ incluido | 1.500 € |
| Email Scrapper | — | ✅ captación | ✅ incluido | — | ✅ captación | ✅ incluido | 1.500 € |
| Icebreaker | — | ✅ captación | ✅ incluido | — | — | ✅ incluido | 1.500 € |
| Agente Instagram | — | — | ✅ omnicanal | — | ✅ marketing | ✅ incluido | 1.500 € |
| Contenido RRSS | — | ✅ bono | ✅ incluido | — | ✅ marketing | ✅ incluido | 1.500 € |
| LinkedIn | — | — | ✅ omnicanal B2B | — | — | ✅ incluido | 1.500 € |
| Blog SEO-GPT | — | — | add-on 500€/mes | — | — | add-on | 1.800 € |
| AutoShorts | — | — | ✅ kit contenido | — | — | ✅ incluido | 1.800 € |
| RAG Avanzado | — | — | ✅ agente marca | — | — | ✅ Liga IA | 1.800 € |
| Real Estate Agent | — | — | — | — | — | — | **2.500 €** |

---

## REGLAS DE VENTA

**Standalone solo si:**
- El cliente no encaja en ningún plan (sector muy específico)
- Quiere una sola automatización concreta y no más
- Nunca por debajo del floor — si no es rentable, no se hace

**Dentro de plan siempre que sea posible:**
- El cliente percibe más valor ("tienes 3 automatizaciones incluidas")
- PalferIA amortiza el tiempo de setup en el precio total del plan
- El mantenimiento mensual cubre ajustes — no hay trabajo extra sin cobrar

**Pack de entrada si el cliente duda:**
- Recepcionista WA + Recordatorios = 2.000 € (ahorro de 400€ vs. standalone individual)
- Funciona como gancho hacia el Vecino Digital completo

**Negociación:**
- Precio tarifa mercado: primer número que se da
- Floor interno: nunca bajar de aquí
- Margen entre ambos: 33% — espacio para negociar sin perder rentabilidad
