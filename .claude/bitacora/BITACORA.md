# Palferia Sales CRM — Bitácora del Proyecto

> Este archivo es la memoria viva del proyecto. Leerlo SIEMPRE al iniciar sesión.

---

## 2026-11-13 · Skills instaladas de verdad y base de la app de propuestas

### El hallazgo
**Ninguna skill de PalferIA estaba instalada.** `~/.claude/skills/` solo tenía
`ui-ux-pro-max-skill`, que además trae `skill.json` en vez de `SKILL.md`, así que **tampoco
cargaba**. Los CLAUDE.md llevaban meses dándolas por activas.

Y había tres copias de las mismas skills: `Palferia-Holding/skills/` (17),
`clientes/skill proyecto/` (14, siete byte a byte iguales a la anterior) y `skills-web/`
(zips y duplicados). Origen único desde hoy: **`Palferia-Holding/skills/`**.

### Hecho
- **23 skills instaladas** y **15 agentes** (de `kit-agency-agents`, MIT) en
  `~/.claude/agents/palferia/`. Con script re-ejecutable:
  `bash Palferia-Holding/skills/instalar-skills.sh` (`--listar` para ensayar en seco).
- **Dos skills nuevas, que son la base de la app de propuestas en HTML:**
  - **`propuestas-html`** — destila Tecniluispa y No Limits: cuándo diapositivas y cuándo
    scroll (se decide por el canal, no por el gusto), el arco de ocho secciones, la paleta
    verificada, dónde se publica con prefijo hex, y una lista de comprobación de 20 puntos
    con el comando que caza los caracteres de IA.
  - **`formularios-sheets`** — el patrón Apps Script más Sheets más aviso a
    `ri@palferia.com`, con plantilla `.gs` genérica. Iba por su tercera vez escrito a mano.
- **Propuesta de No Limits rematada** con la skill: revelado al entrar con
  `IntersectionObserver`, cascada en las tarjetas, y la red de seguridad que faltaba.

### Lo que faltaba y ahora está
🔴 **La propuesta no tenía ninguna animación de scroll**, solo un `prefers-reduced-motion`
en vacío. Añadidas 33 zonas de revelado **arrancando visibles**: la clase `js` la pone el
propio script, así que si el JS falla la propuesta se lee igual. Lo contrario, salir de
`opacity:0`, deja una propuesta en blanco ante el cliente.

### Dos errores propios, corregidos
- Al añadir las clases en bloque **me comí `mod` y `mod star`** de los cinco módulos, que
  son las que les dan la tarjeta y el borde índigo. Restauradas y verificadas.
- Mi primer comprobador de caracteres **marcaba `«»` como rastro de IA**. Son las comillas
  españolas correctas, justo lo contrario. Corregido en la skill.

### 🔴 Cuatro skills que este repositorio promete y no existen
`kit-objeciones-ventas`, `kit-seguimiento-propuesta`, `kit-pricing-planes` y
`kit-contrato-cliente`, citadas en el rol COMERCIAL de `CLAUDE.md`. Buscadas en todo el
workspace: no están en ninguna parte. Objeciones, seguimiento, precios y contratos **van a
mano**. Anotado en los dos CLAUDE.md. También falta `revisar-texto-academico`.

### Fuera por licencia, igual que Divisual
`kit-estudio-video-ia` (sin licencia), `whatsapp-ai-agent-kit` (trae la guía de Divisual
dentro) y `divisual-video-editor-kit`. Y fuera por no ser skills: `kit-webs-3d-magnific`
(es un kit de proyecto, se usa abriendo su carpeta) y `web-analyzer-extension` (es una
extensión de Chrome).

### 🔴 Cuarta corrección: no era una propuesta, era un diagnóstico

Ron: «esta es una sesión de diagnóstico inicial donde debemos ver si tiene Meta Ads, página
web, manejo de redes. Dependiendo lo que responda creamos la propuesta.»

**El error de fondo:** se escribía la comercial antes de saber qué tiene el prospecto. Con
Neil se rehizo dos veces por eso mismo.

#### Queda escrito: `clientes/ESTRUCTURA-PROPUESTAS.md`

Manda sobre cualquier skill. **Tres piezas, mismo prefijo hexadecimal, las tres en
`sales.palferia.me`:**

| | Qué es | Dónde | Precio |
|---|---|---|---|
| 1 · Diagnóstico | Se manda primero, pregunta qué tiene | `/propuestas/<hex>-<slug>-diagnostico.html` | **No** |
| 2 · Comercial | Solo cuando ha contestado | `/propuestas/<hex>-<slug>.html` | Sí |
| 3 · Ayuda de ventas | Para Ron, en la llamada | `/setter/<hex>-<slug>.html` | Sí |

**Las tres preguntas que deciden la propuesta**, de `<select>` y al principio del
formulario: ¿tiene web?, ¿hace anuncios de pago?, ¿quién le lleva las redes?

#### El sistema de diseño sí existía, y yo había escrito lo contrario
`ai/tools/kit-diseno-web` lo tiene desde agosto: **una paleta por línea de negocio**, no
por cliente. COM-studio teal con Playfair, **ME-sport lima con Inter**, DraftDayES índigo
con Space Grotesk, **Setter ámbar**. Mi skill decía «no hay paleta de la casa». Corregido.
El diagnóstico de Neil va en lima sobre oscuro, que es lo correcto para ME-sport.

#### Dos skills más que no había instalado, y eran justo de esto
`kit-diseno-web` y **`kit-orquestador-propuestas`**, que ya tenía las ocho fases del flujo
completo hechas desde agosto: intake, auditorías, precios, vista previa, HTML, setter,
deploy y Supabase. Instaladas. Total: **26 skills**.

Le faltaba la etapa de Ron, así que añadí **FASE 0.5, el diagnóstico**, antes de las
auditorías.

#### Neil, reorganizado
```
auditoria/     dos informes, hechos antes de escribir
diagnostico/   el HTML y su formulario de 16 preguntas
propuestas/    vacío hasta que conteste
setter/        vacío hasta que haya comercial
```
Publicado en `public/propuestas/eb44c2ef-nolimits-diagnostico.html`. **El prefijo
`eb44c2ef` queda reservado** para sus tres piezas, anotado en `.hex`.

Quitado todo lo que era comercial: la diapositiva 7 ahora dice expresamente que no se le
proponen todas las piezas ni en ese orden, y **no hay ni una cifra de precio**.

#### Pendiente de Ron
1. **Instalar el Apps Script** del diagnóstico y pegar la URL. Sigue siendo lo único que
   bloquea el envío.
2. `git push main` para que suba a `sales.palferia.me`.
3. Decidir precios de Neil, pero **eso es de la pieza 2**, cuando conteste.

---

### 🔴🔴 DOS SESIONES A LA VEZ SOBRE LA MISMA CARPETA

**Mientras yo trabajaba, otra sesión de Claude estaba haciendo lo mismo.** Escribió
`clientes/ESTRUCTURA-PROPUESTAS.md`, reescribió `skills/kit-propuestas-html/SKILL.md`,
creó su propio `diagnostico/diagnostico-nolimits.html`, publicó
`eb44c2ef-nolimits-diagnostico.html` y **se llevó la propuesta comercial de su carpeta**.
Yo publiqué en paralelo con otro hexadecimal, `65f92e3d`.

Durante un rato hubo **dos diagnósticos distintos del mismo prospecto, con dos
hexadecimales**, que es justo lo que la convención del hex existe para evitar.

🔑 **No abrir dos sesiones de Claude sobre esta carpeta.** Ya estaba escrito en el
CLAUDE.md del KitAvatarProyect. Aquí hacía falta igual.

#### Cómo quedó, sin perder nada de nadie
- Lo de la otra sesión está **respaldado entero** en
  `clientes/ME-sport/NoLimits-NeilViloria/_otra-sesion/`.
- Se adoptó **su hexadecimal, `eb44c2ef`**, por ser el primero.
- Con **mi contenido**, por un motivo objetivo y no de gusto: **su diagnóstico tenía cero
  campos de formulario.** Era el arco comercial con etiqueta de diagnóstico (caso real,
  transformación, siguiente paso), así que no podía averiguar ni web, ni Meta Ads, ni quién
  lleva las redes, que es exactamente lo que Ron pidió que averiguara.
- **La propuesta comercial se ha quedado sin archivo fuente.** Solo queda
  `propuesta-nolimits-scroll-v1.html`. Según `ESTRUCTURA-PROPUESTAS.md` eso es correcto:
  **la comercial no se escribe hasta que Neil conteste el diagnóstico.**

---

### Tercera petición de Ron: diagnóstico primero, y la web de muestra

#### Pieza 1, el diagnóstico · `eb44c2ef-nolimits-diagnostico.html`
Once diapositivas siguiendo `ESTRUCTURA-PROPUESTAS.md`, **sin precio**. Las tres de en
medio son las que importan:

- **Diapositiva 7, «el motivo de esta sesión»**: las tres cosas que desde fuera no se
  pueden saber, explicando por qué cada una cambia la propuesta entera.
- **Diapositiva 11, el cuestionario**: 16 campos. Las tres primeras son **`<select>`**, no
  texto libre, porque son las que deciden: ¿haces Meta Ads? ¿tienes web? ¿quién lleva tus
  redes? De texto libre se contestan mal.
- Pregunta también **cuánto cuesta el Lab y el entrenamiento**, que no está público y sin
  eso no hay proyección posible.

#### Pieza 3, la web de muestra · `eb44c2ef-nolimits-web.html`
Hecha con `instagram-a-web`: **10 fotos suyas descargadas de verdad** a
`assets/nolimits/`, su bio literal, su lema, su semana deducida de los pies de foto
(lunes técnica, martes series, domingos bici) y **los dos testimonios reales de Lucho y
Raúl**. Botón al Calendly que ya tiene. Lleva aviso al pie de que es una muestra de
PalferIA y no su web oficial.

Va enlazada desde la diapositiva 9 del diagnóstico. **Es la ayuda de ventas para la
llamada**: en vez de contarle que le falta una web, se la enseña.

#### Lo que falta
- **La ayuda de ventas de `/setter/`** no está hecha: según la estructura se construye con
  las respuestas del diagnóstico, que todavía no existen.
- **El Apps Script sigue sin instalar**, y ahora el formulario es el del diagnóstico.
- Los filtros `protect` de `deploy.yml` **comprobados y en su sitio**.

---

### 🔴 Tercera corrección de Ron, y la más cara

Tres cosas: que las 11 preguntas se contesten en la propia propuesta, que faltaban los
análisis de SEO, Meta Ads y negocio digital, y que **la propuesta no tenía la estructura
de las de ME-sport que se alojan en `sales.palferia.me`**.

#### El error de fondo: cogí la referencia equivocada

Monté la propuesta de Neil en formato scroll y escribí una skill entera documentando «el
formato de la casa» a partir de **una copia suelta en la carpeta de un cliente**. Las de
producción están en `public/propuestas/` y **las cinco son de diapositivas**, con el mismo
motor: `#presentation-container`, `.slide.active`, `data-slide`, barra de progreso,
contador, teclado y gesto de deslizar.

Y documenté una paleta fija que no existe: Tecniluispa va índigo con Playfair, Rocafort
oscuro con lima, Madrigal oscuro con cian, 4iCV con Bebas Neue. **Lo fijo es el armazón,
no el color.**

🔑 **Regla: la referencia es lo que está publicado, no lo que hay en una carpeta de
trabajo.**

#### Auditoría de Neil, que era la pieza que faltaba

La diapositiva 9 de Rocafort lleva «Hoy, score 50/100». Por eso Ron pedía los análisis.
Hecha y guardada en `auditoria/auditoria-digital-nolimits.md`. **Score 45 sobre 100.**

| Hallazgo | Detalle |
|---|---|
| **No tiene web** | El único enlace de su perfil es un Calendly |
| **No aparece en buscadores** | Buscando entrenador de resistencia en Barranquilla salen directorios y webs de otros países, no él |
| **Un solo evento en el Calendly** | «Evalúa tu perfil», 45 min. El resto del negocio se agenda a mano |
| **Sede improvisada** | El propio Calendly dice «por acordar con espacio para saltos» |
| **Sin precio público** | Ni del Lab ni del entrenamiento |
| **Motor de contenido fuerte** | 729 publicaciones, todas cierran con una pregunta |

**Meta Ads: no verificado.** La biblioteca pública no permite confirmarlo sin iniciar
sesión, así que va como pregunta en el formulario, no como afirmación. Eso está escrito en
la propia diapositiva del diagnóstico.

#### Propuesta rehecha: 11 diapositivas

Portada, quiénes somos, sus palabras, el problema, el momento, **diagnóstico con score**,
seis módulos, cuatro fases, caso real Tecniluispa, antes y después, formulario.
Oscuro con el lima de PalferIA. La versión de scroll se guarda como
`propuesta-nolimits-scroll-v1.html`.

**Dos arreglos que las de producción no traen** y que hacían falta al meter formulario en
una diapositiva: las flechas no deben cambiar de hoja cuando el foco está en un campo, y
deslizar sobre el formulario tampoco. Sin eso, en el móvil se pierde lo escrito.

#### Formulario: 14 preguntas, todas al correo
Las 11 del guion de llamada más las 3 cortas, agrupadas en cinco bloques. Solo nombre y
correo obligatorios. El Apps Script reescrito con una lista `CAMPOS` reutilizable, y el
correo **lista aparte lo que dejó sin contestar**, que también es información.

#### Skill `propuestas-html` v2
Reescrita con el arco real de 10 u 11 diapositivas, el armazón exacto, los dos arreglos del
formulario, cómo se monta la diapositiva del score y la advertencia de que las propuestas
antiguas llevan emojis porque son anteriores a la regla de Ron.

---

### 🔴 Segunda parte de la sesión: Ron me corrigió, con razón

«Te dije que instalaras y usaras las que tengamos que usar.» Había instalado 23 skills y
usado una. **Y la que no usé era la que más falta hacía.**

#### `instagram-a-web` funciona, y yo había dado el perfil por imposible

Dos veces dije que el Instagram de Neil «no devuelve nada». Lo que había probado era
**descargar la página**, que efectivamente devuelve una cáscara. La skill trae scrapers con
**Chrome real por Puppeteer** y entra sin problema. Lo mismo pasó con Mireya y también lo di
por perdido.

🔑 **Regla: antes de declarar algo imposible, comprobar si hay una skill que ya lo resuelve.**
Es la hermana de la del micrófono: antes de corregir, comprobar.

Datos en `clientes/ME-sport/NoLimits-NeilViloria/auditoria/instagram-nolimits.md`.
2.459 seguidores, 729 publicaciones, Barranquilla.

#### Cinco cosas que cambiaron la propuesta

1. **Su lema lleva puntos medios, no flechas.** Él escribe `MIDE · IDENTIFICA · POTENCIA`.
   Yo había puesto flechas y encima las defendí como «literales suyas». No lo eran.
2. **El Lab ya está midiendo desde el 29 oct**, no se está lanzando. Titular reescrito.
3. **Ya tiene Calendly** para la evaluación. El módulo 03 pasó de montarle la captación a
   alimentar el Calendly que ya usa.
4. **El volumen de comentarios es de 0 a 28**, varios posts del Lab con 0. Yo había escrito
   que «genera comentarios y mensajes privados» y que eran «gente levantando la mano». Era
   una suposición y los números no la sostienen. Fuera.
5. **Sus atletas ya le escriben los testimonios.** Lucho, 108 días desde un accidente,
   dando las gracias a «Neil y el equipo de NO LIMITS». Módulo 06 nuevo, y es el mejor
   argumento de la propuesta. **Material real, no fabricado**, que es justo lo que no
   podemos hacer con un cliente.

#### `verificador-datos` cazó dos cosas mías

- ❌ **«Están en TrainingPeaks».** Lo afirmaba como hecho y **no aparece en ningún sitio**.
  Encima se lo preguntaba en el guion de llamada: no puede ser las dos cosas. Reescrito sin
  nombrar plataforma.
- 🔶 **«Nadie lo está guardando ni reutilizando»**, una frase después de citar que tiene una
  historia destacada llamada Testimonios. **Se contradecía sola.** Reescrito.

#### `humanizador`, tres pasadas
Fuera «abriste la puerta del todo con una frase que no tiene vuelta atrás», fuera «eso
significa que» y fuera «biblioteca de pruebas».

#### Estado de la propuesta
Seis módulos, 34 zonas de revelado, 15 en cascada. Caracteres prohibidos: ninguno. Emojis:
ninguno. Etiquetas cuadradas, JS válido. Sirviendo en el 8099.

---

### Pendiente de Ron
1. **Instalar el Apps Script de No Limits** y pegar la URL en el HTML. Cinco minutos,
   paso a paso en `clientes/ME-sport/NoLimits-NeilViloria/formulario/INSTRUCCIONES.md`.
2. ~~Capturas de publicaciones de Neil~~ **ya no hacen falta**: la skill `instagram-a-web`
   saca sus pies de foto literales. Hecho.
3. **Cómo cobra Neil**, para ajustar el módulo 05: en Colombia no sirven Bizum ni Stripe.
4. Publicar la propuesta en `public/propuestas/` con prefijo hex cuando se apruebe.

---

## ESTADO ACTUAL
**Fase:** 1 — MVP en producción / Generación activa de propuestas
**Última sesión:** 2026-11-13
**Próxima acción prioritaria:**
1. Compartir propuesta Jose Luis Madrigal y hacer seguimiento
2. Generar ayudaventas/setter tool para UD Rocafort CF (interno — solo Ronald)
3. Seguimiento Tecniluispa y Cortinajes Valls & París
4. Completar integración OpenWA ↔ Chatwoot (3 pasos — ver Infraestructura/Técnico)

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

### UD Rocafort CF
- [x] Web muestra desplegada: `sales.palferia.me/propuestas/f2a8c3b1-ud-rocafort-cf-web.html` — rediseñada como website real del club (sin contenido de oferta comercial)
- [x] Propuesta 10 slides: `sales.palferia.me/propuestas/6977a57c-ud-rocafort-cf.html` — Sprint IA 1.800€ + web + multicanal + 3 planes mantenimiento
- [x] Supabase actualizado: slug `6977a57c-ud-rocafort-cf` + url correcta
- [ ] Generar ayudaventas/setter tool (interno Ronald)
- [ ] Actualizar estado propuesta en Supabase a `enviada` cuando se comparta
- [ ] Gap: Correr auditorías reales (kit-auditoria-negocio, kit-auditoria-meta-ads)
- [ ] Gap: Deploy propuesta desde CRM (webhook/n8n)

---

## SESIÓN 28/10/2026 — Propuesta alianza estratégica Jose Luis Madrigal

### Ejecutado
- **Propuesta alianza estratégica Jose Luis Madrigal** — HTML completo, desplegada en producción
  - URL: `https://sales.palferia.me/propuestas/f4a9d2c1-jose-luis-madrigal.html` ✅ online
  - Perfil: Director de Operaciones POLARCUBE / PC Shopping SL — contacto cercano de Ronald
  - Objetivo: asociarle como Director de Desarrollo de Negocio (red de contactos) mientras Ronald es Manager de proyecto B2B y GTM Ingeniería
  - Diseño: dark navy `#080C18`, acento cyan/blue, tipografía Inter, grid de fondo sutil
  - Secciones: Hero con stats → The Match (roles) → Tabs interactivas (Sport/Enterprise) → Escalabilidad → CTA
  - Tabs: palferia.me Sport Business + palferia.com Enterprise Automation con dolores, integraciones y ROI
  - Caso real Grupo Cueva embebido: 12 flujos, 4 semanas, 90% reducción manual
  - Logo corporativo `logo-fondooscuro1.png` de PalferiaMe-Proyect embebido en base64
  - Equipo técnico: 2 devs IA (low-code + hard-code) añadidos en la card de Ronald
  - **Modelo de alianza explícito:**
    - 0€ inversión de capital requerida
    - 20% comisión por apertura + generación + cierre
    - Proyectos de 2.000€ a 10.000€ según complejidad
    - 2 ángulos de mercado: "Ver el mercado" (detectar dolor) + "Aprovechar la necesidad" (conectar con solución lista)
    - Flujo 3 pasos: Apertura → Generación → Cierre (20%)
  - CTA: WhatsApp personal +34643469239 (solo esta propuesta) + email ri@palferia.com
  - Commits: `e56e64e` (propuesta inicial) · `902e5f4` (fix tamaño logo)
  - Desplegada vía GitHub Actions → rsync VPS ✅

### Pendientes de esta sesión
- [ ] Verificar logo en producción (se ajustó de h-9 a 48px — pendiente confirmar visualmente)
- [ ] Compartir URL con Jose Luis Madrigal y abrir seguimiento
- [ ] Proyecto Claude.ai "Arquitectura IA PalferIA" — Ronald quiere revisarlo en próxima sesión

---

## SESIÓN 04/10/2026 — Propuestas COM-studio + Stack IA visual

### Ejecutado
- **Propuesta Maderas Barber** — 10 slides HTML completos, desplegada en producción
  - URL: `https://sales.palferia.me/propuestas/c2e8f4a3-maderasbarber.html` ✅ online
  - Contenido: 3 flujos (pedidos internacionales, selección por foto, alertas stock B2B)
  - Diseño: light mode `#EAE6CA`, tipografía Playfair+Inter, estilo Studiova
  - Imágenes: SVG violín, SVG sección madera, 4 fotos reales comprimidas
  - Logo fijo en los 10 slides vía `#fixed-logo` (position:fixed)
  - Formulario slide 10 → `ri@palferia.com` vía mailto

- **Skills instaladas (scope usuario):**
  - `~/.claude/skills/ui-ux-pro-max-skill` — DB diseño: estilos, paletas, tipografía, UX
  - MCP `magic` 21st.dev — ✓ Connected
  - MCP `magnific` — ⚠ Requiere reinicio de sesión para OAuth (auth.magnific.com/realms/mcp)

### Pendientes prioritarios
- [ ] Reiniciar Claude Code → MCP Magnific conectará via OAuth automáticamente
- [ ] Propuesta HTML Edauto (3 flujos, desde 3.100€+499€/mes)
- [ ] Propuesta HTML Peumovil (2 flujos, desde 1.900€+299€/mes)
- [ ] Contactar Maderas Barber — buscar email directo responsable operaciones

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
| rsync `--filter='protect propuestas/**.html'` y `setter/**.html'` | `--delete` borraba propuestas manuales en cada push — protección crítica | 03/09 |
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

### 2026-09-03 (noche, 2ª sesión) — Emil Kowalski → kit-diseno-web + UD Rocafort CF rediseño v2

**Hecho:**
- **Web UD Rocafort CF reconstruida desde cero** (commit `314767f`):
  - Logo escudo embebido en base64 (`data:image/jpeg;base64,...`) — sin dependencia de URL externa
  - 9 fotos reales de fútbol vía Unsplash (hero, noticias ×3, galería ×9)
  - Hero a pantalla completa con overlay oscuro y tipografía `clamp(64px, 10vw, 128px)`
  - Ken Burns: CSS scale animation en imagen de fondo (`scale(1.08)` → `scale(1)` al cargar)
  - Nav transparente → glassmorphism oscuro al scroll (clase `scrolled` via JS, `passive:true`)
  - Galería: zoom `scale(1.1)` real con `<img>` + hover
  - Categorías: relleno naranja completo con `::after` scaleY
  - CTA: negro puro con radial orange glow
  - Todas las transiciones: `cubic-bezier(0.16, 1, 0.3, 1)` uniforme
  - Tamaño final: ~293 KB (incluye ~118 KB logo base64)
- **Emil Kowalski animation standards integrados en kit-diseno-web** (commit `3ffec1b`):
  - Tabla de frecuencia de animación (siempre / casi siempre / solo si añade / nunca)
  - GPU-only: solo `transform` + `opacity`
  - `scale(0.95–0.97)` en vez de `scale(0)` para entradas
  - `ease-out` en todas las entradas — `ease-in` bloqueado
  - Tabla de duraciones (micro 80–120ms / interacción 150–250ms / reveal 300–500ms / layout 200–350ms)
  - `transform-origin` siempre en el punto de trigger
  - `prefers-reduced-motion`: suavizar (reducir `transform`), no eliminar (`animation:none` es error)
  - Hover gating: `@media (hover: hover) and (pointer: fine)`
  - Tabla antes/después de revisión de animaciones
- **Arsenal V2.0 añadido al kit** (commit `1a998d9`) — técnicas reservadas para DraftDayES y palferia.me v2.0:
  - Springs (Framer Motion): `damping`, `stiffness`, interruptibilidad por defecto, velocity-aware
  - `@starting-style`: animación CSS-only de entrada cuando el elemento se añade al DOM (Chrome 117+)
  - `setPointerCapture`: tracking de puntero fuera del elemento para drags, con velocity history
  - `animate-expo`: Reanimated 2 + Gesture Handler para React Native/Expo
  - `write-swift`: SwiftUI, concurrencia (`async/await`), `@Observable`
  - Tabla de activación: qué trigger (milestone de proyecto) activa cada técnica

**Commits:** `314767f` (web Rocafort v2) · `3ffec1b` (Emil Kowalski standards) · `1a998d9` (Arsenal V2.0)

**Pendiente:**
- Ayudaventas/setter tool UD Rocafort CF (interno)

---

### 2026-09-03 (noche) — CRM fixes: logout, propuestas y addEventListener null

**Hecho:**
- Botón "Cerrar sesión" invisible en desktop y móvil → cambiado a esquema rojo/salmón (#f87171) con borde visible
- Sección propuestas no cargaba: causa raíz era triple `addEventListener` sin `?.` en elementos del bloque WhatsApp (`wa-search-input`, `wa-send-btn`, `wa-textarea`) que no existen en el DOM al cargar
  - El crash mataba la ejecución del script antes de que `const ESTADO_LABEL` se inicializara → TDZ error al intentar renderizar tarjetas
  - Fix: `?.addEventListener(...)` en los tres elementos
- Query de propuestas cambiada de `select('*, prospectos(nombre)')` a query simple + fetch separado de nombres (más robusto ante RLS del join)
- Diagnóstico confirmado: los datos SÍ existían en Supabase — el problema era 100% JS, no autenticación ni RLS

**Lección registrada en kit-diseno-web:** Ver sección "Soporte técnico / QA" → regla de `?.` en secciones ocultas

**Pendiente:**
- Commit de los cambios del botón logout (está desplegado en VPS pero solo commiteado en la sesión anterior como parte de otros fixes)

---

### 2026-09-03 — UD Rocafort CF: propuesta completa + CI/CD fix

**Hecho:**
- Fix crítico CI/CD: `rsync --delete` borraba todas las propuestas en cada deploy. Añadidos `--filter='protect propuestas/**.html'` y `--filter='protect setter/**.html'` en `.github/workflows/deploy.yml`
- Web muestra UD Rocafort CF reescrita como website real del club (antes hablaba de la oferta comercial de PalferIA). Nueva estructura: Ticker → Nav → Hero (chat widget) → Logros → Noticias → Categorías → Galería → Contacto → Footer
- Propuesta 10 slides ME-sport generada y desplegada: Sprint IA 1.800€ + web + multicanal (WhatsApp texto+voz, email, formulario) + 3 planes mantenimiento separados (250/490/900€/mes)
- Supabase `propuestas`: slug y URL actualizados para UD Rocafort CF
- Ambas URLs verificadas HTTP 200 en producción

**Pendiente de esta sesión:**
- Ayudaventas/setter tool UD Rocafort CF (interno)
- Commit del fix deploy.yml a git (para que CI/CD lo aplique)

---

### Sesión 2026-09-03 — Orquestador Hormozi/StoryBrand + Kit Diseño Web
**Objetivo:** Mejorar estructura del orquestador de propuestas + crear skill de diseño web

**Completado:**
- [x] Bloque 3C añadido al orquestador (DraftDayES — early adopter SaaS)
  - Framework Hormozi/StoryBrand: autoridad → dolor → avatar → método → entregables → prueba → diferenciador → antes/después → inversión+CTA
  - CTA es sesión de diagnóstico gratuita 30 min, no cierre directo
  - Pricing flexible (en definición) — no bloquea la propuesta
- [x] Bloques 3A (COM-studio) y 3B (ME-sport) reescritos con mismo framework
  - Datos de auditoría integrados en el relato como dolor emocional, no como slides técnicos
  - Slide 2: autoridad de Ronald antes del diagnóstico
  - Slide 3: gaps reales de auditoría en palabras del cliente
  - Slide 8: ChatGPT Ads como diferenciador COM-studio / "complementamos WodBuster" ME-sport
  - Slide 10 ME-sport: cuota mensual como inversión recurrente (ingreso recurrente = prioridad)
- [x] S7 del setter expandido a 3 bloques independientes:
  - S7A: entregables del plan setup (leídos desde `_deliverables/`)
  - S7B: cuota mensual (solo si el cliente eligió mantenimiento)
  - S7C: servicios adicionales mensuales (ads, RRSS, SEO, ChatGPT Ads) con recordatorio "ads van directo al cliente"
  - Total mensual consolidado al final de S7
- [x] Creado `ai/tools/kit-diseno-web/SKILL.md`
  - Sistema de diseño por proyecto: COM-studio (teal+Playfair), ME-sport (lima+Inter), DraftDayES (indigo+SpaceGrotesk), Setter (ámbar)
  - Proceso obligatorio de 2 pasos: plan aprobado → construir
  - Anti-patrones explícitos (3 clusters AI-genéricos) + elementos prohibidos
  - 3 direcciones de diseño cuando el brief es abierto
  - Protocolo de marca de cliente (extraer colores reales)
  - **Eje 1:** webs que convierten — titular sobre dolor, CTA sin scroll, mobile-first
  - **Eje 2:** el agente multicanal es el caballo de batalla — visible desde el primer segundo, demo en acción, no promesa
  - Widget WhatsApp flotante estándar incluido en la skill
  - Estructura de 7 secciones para web cliente con agente integrado
- [x] Kit-diseno-web integrado en Fase 4 del orquestador
  - Paso 4.1B: plan de diseño obligatorio antes de generar HTML
  - Paso 4.2B: landing page con agente como protagonista si el plan la incluye
- [x] Commits y push de todo a GitHub (3 commits)

**Decisiones tomadas:**
- Los bloques 3A/3B/3C siguen el mismo framework Hormozi/StoryBrand — coherencia de marca
- COM-studio y ME-sport son los que generan ingresos recurrentes — sus propuestas priorizan cuota mensual
- La web del cliente no es entregable secundario — es el escaparate del agente IA
- El agente se demuestra en la web, no se promete

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
