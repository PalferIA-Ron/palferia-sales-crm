---
name: kit-diseno-web
description: >
  Diseña páginas web, propuestas, landings y herramientas internas con identidad
  visual fuerte y no genérica. Aplica el sistema PalferIA por proyecto
  (COM-studio / ME-sport / DraftDayES) y evita los patrones AI-genéricos.
  Actívala cuando el usuario diga "diseña", "crea una página", "hazme una landing",
  "genera el HTML", o cuando el Orquestador llegue a Fase 4.
version: 1.0.0
author: PalferIA
---

# Kit Diseño Web — PalferIA

Genera diseños HTML/CSS nativos con identidad visual distintiva.
Sin templates genéricos. Sin "AI slop". Cada página habla del negocio que representa.

**Principio rector:** Gasta tu audacia en un solo lugar. El elemento signature
es lo memorable — el resto debe ser quieto y disciplinado.

---

## LOS DOS ESCENARIOS DE TRABAJO

### Escenario A — Cliente SIN web (construimos desde cero)

Aquí aplican los dos ejes completos:

**Eje 1 — Web impactante:**
La web no es un folleto digital. Es una máquina de captura.
Cada decisión responde a una sola pregunta: **¿esto acerca al visitante a convertir?**

Principios que no se negocian:
- El titular de la hero habla del dolor del cliente, no del nombre del negocio
- El primer CTA aparece sin necesidad de hacer scroll
- La velocidad de carga es parte del diseño (sin imágenes pesadas, CSS inline si aplica)
- La identidad del negocio (colores, tono, sector) impregna cada elemento — no es un template con el logo cambiado
- Mobile-first siempre — el 80% del tráfico viene de móvil

**Eje 2 — El agente multicanal es el caballo de batalla:**
(ver sección completa abajo)

---

### Escenario B — Cliente CON web existente

No rehacemos su web. Integramos el agente sobre lo que ya tiene.

**Qué entregamos:**
- Widget de WhatsApp/Chat flotante que se añade con 2 líneas de script
- Landing page de captación independiente (subdominio o `/agente`) — esta SÍ la construimos nosotros
- Instrucciones claras para que el cliente o su webmaster pegue el snippet

**La landing page de captación es nuestro lienzo:**
Aunque el cliente tenga web, siempre creamos una landing page propia donde el agente es protagonista. Es la página que se usa en anuncios, QR, tarjetas y WhatsApp Bio.
- URL: `[negocio].com/agente` o subdominio dedicado
- Estructura: las 7 secciones del Escenario A, pero enfocada en una sola acción
- Sin menú, sin links externos — foco total en activar el agente

**Cuándo sugerir rediseño web completo:**
Solo si el score de la auditoría < 40 Y la web actual perjudica activamente la conversión.
No proponer rediseño como primera opción — el agente genera valor independientemente de la web.

---

### El agente multicanal es el caballo de batalla (aplica en ambos escenarios)

El agente IA integrado en la web es el producto principal de PalferIA.
La web no presenta el negocio — **presenta el agente y lo pone en acción**.

**El agente es visible desde el primer segundo:**
- Widget de chat flotante activo (no oculto, no "¿necesitas ayuda?")
- Mensaje de bienvenida personalizado del agente visibles en hero
- Demo funcional o screenshot del agente respondiendo en el sector del cliente
- Canal preferente destacado: WhatsApp > Chat web > Email según el cliente

**La web demuestra el agente, no lo promete:**
```
❌ "Implementamos agentes de IA para tu negocio"
✅ "Hola, soy el asistente de [Nombre negocio]. ¿Buscas [servicio principal]?
    Respondo en segundos — pruébame."
```

**Integración visual del agente según plan:**
- Vecino Digital / Sprint IA → widget WhatsApp flotante + CTA directo
- Autopilot 30 / Equipo IA → widget chat web + WhatsApp + formulario inteligente
- Socio Digital / Liga IA → chat omnicanal con selector de canal (WA / Email / Chat)

**El agente como diferenciador en el diseño:**
- Sección "Habla con [Nombre negocio] ahora" con demo real o simulada
- Contador de respuestas: "Responde en menos de 30 segundos · 24/7"
- Casos de uso del agente específicos para el sector en formato conversacional:
  ```
  👤 "¿Tenéis mesa para 4 personas el viernes?"
  🤖 "Claro, ¿a qué hora te viene bien? Tengo disponibilidad a las 20h y 21:30h."
  ```

---

---

## SISTEMA DE DISEÑO PALFERIA

### Paletas por proyecto

**COM-studio** (automatización B2B, negocios locales)
```
--accent-1:  #0d9488   /* teal profundo — acción, conversión */
--accent-2:  #14b8a6   /* teal claro — hover, highlights */
--bg-dark:   #0a0f1a   /* fondo oscuro base */
--bg-card:   #111827   /* tarjetas, paneles */
--text-main: #f1f5f9   /* texto principal */
--text-muted:#94a3b8   /* texto secundario */
--success:   #22c55e
--warning:   #f59e0b
```
Tipografía: **Playfair Display** (display/headlines) + **Inter** (cuerpo)
Tono: autoridad, precisión, ROI. No juguetón.

**ME-sport** (automatización deportiva)
```
--accent-1:  #84cc16   /* verde lima — energía, movimiento */
--accent-2:  #a3e635   /* verde claro — hover */
--bg-dark:   #0a0f1a
--bg-card:   #111827
--text-main: #f1f5f9
--text-muted:#94a3b8
--energy:    #facc15   /* amarillo — urgencia, resultados */
```
Tipografía: **Inter** (todo) — bold pesado en headlines
Tono: dinámico, directo, orientado a resultados. Confianza deportiva.

**DraftDayES** (SaaS deportivo)
```
--accent-1:  #6366f1   /* indigo — tech, plataforma */
--accent-2:  #818cf8   /* indigo claro */
--accent-sport: #f97316 /* naranja — energía deportiva */
--bg-dark:   #0a0f1a
--bg-card:   #111827
--text-main: #f1f5f9
--text-muted:#94a3b8
```
Tipografía: **Space Grotesk** (display) + **Inter** (cuerpo)
Tono: innovador, early adopter, SaaS premium. No corporativo.

**Setter tool** (herramienta interna Ronald)
```
--accent:    #f59e0b   /* ámbar — alerta, acción comercial */
--bg-dark:   #0a0f1a
--sidebar:   #0f172a
```
Tipografía: **Inter** (todo) — máxima legibilidad, sin adornos

---

## PROCESO DE DOS PASOS (obligatorio)

### Paso 1 — Plan antes de construir

Antes de escribir una sola línea de HTML, mostrar:

```
🎨 PLAN DE DISEÑO — [nombre del proyecto]
══════════════════════════════════════════

CONCEPTO: [Una frase que define la idea central. No "moderno y limpio".]

PALETA:
  Background:  [hex] — [por qué este fondo]
  Accent 1:    [hex] — [rol funcional]
  Accent 2:    [hex] — [rol funcional]
  Texto:       [hex]

TIPOGRAFÍA:
  Display:  [fuente] [peso] — [por qué esta para este negocio]
  Cuerpo:   [fuente] [peso]
  Escala:   [tamaños principales]

ELEMENTO SIGNATURE: [El detalle que hace memorable esta página]
  Ej: línea teal animada en scroll / contador de leads en tiempo real /
      grid asimétrico de testimonios / hero con video loop del negocio

LAYOUT PRINCIPAL: [ASCII wireframe de la estructura]
  [hero]
  [stat row]
  [features grid]
  [CTA]

QUÉ EVITAMOS: [Los 3 clichés más probables para este tipo de página]

══════════════════════════════════════════
¿Apruebas el plan o ajustamos algo?
```

### Paso 2 — Construir solo tras aprobación

Si el usuario aprueba → generar el HTML completo.
Si pide cambios → ajustar el plan, no el código.

---

## ANTI-PATRONES — LO QUE NO HACEMOS

### Clusters AI-genéricos a evitar
1. **Cluster crema**: fondo `#F4F1EA` + serif alto contraste + terracota/naranja tostado
2. **Cluster brutal**: casi-negro + verde ácido o rojo vermellón como único acento
3. **Cluster broadsheet**: layout periódico con hairlines y columnas densas

### Elementos prohibidos salvo brief específico
- Gradientes purple/pink/violet sin justificación de marca
- Emojis como íconos funcionales (usar Heroicons, Lucide o SVG propios)
- `border-left: 4px solid` como único elemento decorativo
- SVG de caras genéricas o ilustraciones "SaaS bubble"
- Inter en display headline de más de 48px (usar display face)
- Cards con `border-radius: 12px` + sombra gris suave + icono azul — el combo más visto
- Sección "Por qué elegirnos" con 4 íconos en grid 2×2
- Hero con headline centrado + subtítulo gris + dos botones lado a lado

### Qué hacer en su lugar
- Jerarquía tipográfica agresiva: tamaños extremos (8px vs 80px) crean tensión visual
- Un color de acento bien usado > tres colores mediocres
- Layout roto intencionalmente (columna que sangra, elemento fuera de grid)
- Animación de scroll reveal solo donde el contenido lo justifica
- Datos reales como elemento visual: "247 leads capturados este mes"

---

## TIPOS DE PÁGINA POR CASO DE USO

### Web cliente con agente integrado (producto estrella)

Estructura obligatoria para cualquier web entregada a un cliente de PalferIA:

```
SECCIÓN 1 — HERO (above the fold, sin scroll)
  Titular: dolor resuelto en 8 palabras máximo
  Subtítulo: qué hace el agente + para quién
  CTA primario: botón WhatsApp / Chat (el agente en acción)
  Elemento visual: screenshot/demo del agente en contexto del sector

SECCIÓN 2 — PRUEBA INMEDIATA (agente visible)
  Widget activo con mensaje de bienvenida personalizado
  3 preguntas frecuentes del sector como chips clickables
  Respuesta simulada o real del agente

SECCIÓN 3 — EL PROBLEMA (empathy)
  2-3 dolores del sector con SUS palabras
  Coste invisible en números: "Cada lead no respondido en 5 min = -30% probabilidad"

SECCIÓN 4 — CÓMO FUNCIONA (el método en 3 pasos)
  Paso 1: El cliente escribe → respuesta en segundos
  Paso 2: El agente clasifica, responde y agenda
  Paso 3: Tú recibes solo lo que necesita tu atención

SECCIÓN 5 — PARA TU SECTOR (específico)
  Ejemplos de conversaciones reales del sector del cliente
  Adaptado: restaurante ≠ clínica ≠ academia ≠ taller

SECCIÓN 6 — PRUEBA SOCIAL
  Resultado con número si existe: "X leads capturados / Y% conversión / Z horas ahorradas"
  Sin clientes → caso de ejemplo honesto con proyección

SECCIÓN 7 — CTA FINAL
  Repetir CTA principal (WhatsApp/Chat)
  Urgencia real si existe
  Datos de contacto del negocio
```

**Widget de WhatsApp/Chat — implementación estándar:**
```html
<!-- Widget WhatsApp flotante (bottom-right) -->
<a href="https://wa.me/[NÚMERO]?text=[MENSAJE_PREDEFINIDO]"
   class="wa-widget" target="_blank" aria-label="Chat por WhatsApp">
  <svg><!-- icono WhatsApp --></svg>
  <span class="wa-pulse"></span>
</a>

<style>
.wa-widget {
  position: fixed; bottom: 24px; right: 24px; z-index: 9999;
  background: #25D366; border-radius: 50%; width: 60px; height: 60px;
  display: flex; align-items: center; justify-content: center;
  box-shadow: 0 4px 20px rgba(37,211,102,0.4);
  transition: transform 0.2s;
}
.wa-widget:hover { transform: scale(1.1); }
.wa-pulse {
  position: absolute; inset: -4px; border-radius: 50%;
  border: 2px solid #25D366; animation: pulse 2s infinite;
}
@keyframes pulse {
  0%,100% { opacity: 1; transform: scale(1); }
  50%      { opacity: 0; transform: scale(1.3); }
}
</style>
```

### Propuesta comercial (slides HTML)
- Motor: position-absolute, opacity 0→1, transición suave
- Navegación: flechas + teclado + swipe táctil
- Contador automático (no hardcodeado)
- Responsive: breakpoints 480px y 900px, `100dvh` para iOS Safari
- Elemento signature: animación de entrada del dato clave en cada slide
- Ver: `public/propuestas/` para referencia de propuestas existentes

### Landing page cliente
- Hero con el dolor del cliente en primera línea (no el nombre del servicio)
- Prueba social visible en primer scroll (número, testimonio, logo)
- CTA repetido 3 veces: arriba, mitad, final
- Sin menú de navegación — foco en conversión
- WhatsApp flotante si el cliente lo usa como canal principal

### Setter tool (interno)
- Sidebar fijo 240px con navegación por secciones
- Contenido principal scrollable
- Sin animaciones distractoras — máxima legibilidad
- Colores de estado: verde (cerrado) / ámbar (en proceso) / rojo (bloqueado)
- localStorage para persistir estado entre sesiones

### CRM / Dashboard
- Tabla como protagonista — no cards
- Filtros rápidos visibles, no en modal
- Indicadores de estado por color, no solo texto
- Modo oscuro por defecto (`#0a0f1a`)

---

## PROTOCOLO DE MARCA DEL CLIENTE

Cuando se diseña una página para un cliente específico (landing, propuesta):

1. **Extraer colores reales** — no asumir. Si tiene web → usar kit-web-scrolling para extraer palette. Guardar en `brand-spec.md` del cliente.
2. **Buscar logo** — pedir al usuario o buscar en web pública. Nunca generar logo falso.
3. **Tono del sector** — clínica ≠ restaurante ≠ academia deportiva. El diseño habla el idioma del sector.
4. **Si no hay marca definida** → usar paleta PalferIA del proyecto + placeholder con nota visible.

```
/* brand-spec.md mínimo por cliente */
nombre: [nombre negocio]
sector: [sector]
color-primario: [hex extraído]
color-secundario: [hex extraído]
tipografia-usada: [si la detectamos]
tono: [formal/cercano/técnico/deportivo]
logo-path: [ruta o "pendiente"]
```

---

## TIPOGRAFÍA — REGLAS

### Cargar fuentes correctamente
```html
<!-- COM-studio -->
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;700;900&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">

<!-- ME-sport / Setter -->
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">

<!-- DraftDayES -->
<link href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=Inter:wght@400;500;600&display=swap" rel="stylesheet">
```

### Escalas recomendadas
```css
/* Escala COM-studio (contraste serif/sans) */
--text-hero:    clamp(2.5rem, 6vw, 5rem);    /* Playfair Display 900 */
--text-xl:      clamp(1.5rem, 3vw, 2.5rem);  /* Playfair Display 700 */
--text-lg:      1.25rem;                      /* Inter 600 */
--text-base:    1rem;                         /* Inter 400 */
--text-sm:      0.875rem;                     /* Inter 400 */
--text-label:   0.75rem;                      /* Inter 500 uppercase */

/* Escala ME-sport (impacto puro) */
--text-hero:    clamp(3rem, 8vw, 7rem);       /* Inter 900 */
--text-xl:      clamp(1.75rem, 4vw, 3rem);   /* Inter 800 */
```

---

## ANIMACIONES — ESTÁNDARES DE CRAFT (Emil Kowalski)

> Fuente: repositorio `emilkowalski/skills` — reglas aplicables a HTML/CSS vanilla y DraftDayES (React).
> Las reglas marcadas con 🟦 aplican también a DraftDayES. Las sin marca aplican a todo.

---

### 1. ¿Debe animar? — La pregunta que va primero

Antes de escribir una sola línea de animación, responde esto:

| Frecuencia de uso | Decisión |
|---|---|
| 100+ veces/día (atajos de teclado, command palette, navegación principal) | **Sin animación. Nunca.** |
| Decenas de veces/día (hover, navegación de lista, toggles frecuentes) | Eliminar o hacer casi imperceptible |
| Ocasional (modales, drawers, toasts, ajustes) | Animación estándar |
| Rara / primera vez (onboarding, estados vacíos, confirmaciones) | Aquí vive el presupuesto de deleite |

**Si no puedes nombrar el propósito en una de estas palabras, no la construyas:**
- **Feedback** — confirmar que la interfaz oyó al usuario
- **Consistencia espacial** — mostrar de dónde vino o adónde fue algo
- **Indicación de estado** — hacer legible un cambio de estado
- **Evitar un cambio brusco** — puentear contenido que de otro modo teleportaría
- **Explicación** — demostrar cómo funciona algo (solo onboarding/marketing)
- **Deleite** — permitido únicamente en el nivel raro/primera vez

---

### 2. Propiedades permitidas — solo GPU

```css
/* ✅ Estas dos propiedades y nada más */
transform: translateY(0) scale(1);
opacity: 1;

/* ❌ Estas disparan layout + paint — nunca animarlas */
/* width, height, margin, padding, top, left, right, bottom */
```

**Nunca `scale(0)`** — nada en el mundo real aparece de la nada.
Siempre empezar en `scale(0.95–0.97)` + `opacity: 0`.

---

### 3. Easing — la regla que más se viola

```css
/* ✅ Entradas: ease-out — la respuesta es inmediata */
transition: transform 200ms cubic-bezier(0.16, 1, 0.3, 1);

/* ❌ ease-in en entradas — se siente lento, el usuario espera */
transition: transform 200ms ease-in;

/* ✅ Para hover/press: ease-out también */
.btn:hover { transform: translateY(-2px); transition: transform 150ms ease-out; }

/* ✅ Curva estándar PalferIA (rápido al principio, suave al final) */
--ease-out: cubic-bezier(0.16, 1, 0.3, 1);
--ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1); /* ligero rebote — solo en deleite */
```

`ease-in` en cualquier interacción UI es un bloqueo. `ease-out` da feedback inmediato.

---

### 4. Presupuestos de duración

| Elemento | Duración |
|---|---|
| Press / :active feedback | 100–160ms |
| Tooltips, popovers pequeños | 125–200ms |
| Dropdowns, selects | 150–250ms |
| Modales, drawers | 200–350ms |
| Reveal en scroll (scroll reveal) | 500–700ms |
| Marketing / explicativo | Sin límite estricto |

UI por encima de 300ms sin justificación = hallazgo. Nunca `0.5s ease` en botones o toggles.

---

### 5. Transform-origin — escalar desde el trigger

```css
/* ✅ Popovers, dropdowns, tooltips — escalan desde donde se abren */
.dropdown { transform-origin: top left; } /* o top center, según posición */

/* ✅ Modales — excepción: se quedan centrados */
.modal { transform-origin: center; }

/* ❌ transform-origin: center en un dropdown anclado a un botón */
```

---

### 6. prefers-reduced-motion — suavizar, no eliminar

```css
/* ❌ Esto es demasiado agresivo — quita toda retroalimentación */
@media (prefers-reduced-motion: reduce) {
  * { animation: none !important; transition: none !important; }
}

/* ✅ Mantener opacity/color, quitar el movimiento */
@media (prefers-reduced-motion: reduce) {
  .reveal {
    opacity: 0;
    transform: none; /* quita el translateY, mantiene el fade */
    transition: opacity 0.4s ease;
  }
  .reveal.visible { opacity: 1; }
}
```

---

### 7. Hover gating — no disparar en táctil

```css
/* ✅ Solo en dispositivos con puntero fino (mouse) */
@media (hover: hover) and (pointer: fine) {
  .card:hover { transform: translateY(-4px); box-shadow: 0 12px 40px rgba(0,0,0,.12); }
  .btn:hover { transform: translateY(-2px); }
}
```

Sin este gate, los efectos hover quedan activos en móvil después de un tap.

---

### 8. Reveal estándar PalferIA (corregido)

```css
.reveal {
  opacity: 0;
  transform: translateY(24px);
  transition: opacity 0.65s cubic-bezier(0.16, 1, 0.3, 1),
              transform 0.65s cubic-bezier(0.16, 1, 0.3, 1);
}
.reveal.visible { opacity: 1; transform: none; }

@media (prefers-reduced-motion: reduce) {
  .reveal { transform: none; transition: opacity 0.4s ease; }
}
```

---

### 9. Tabla de revisión rápida

Cuando revises animaciones en cualquier HTML generado, comprueba:

| ❌ Antes | ✅ Después | Por qué |
|---|---|---|
| `transition: all 300ms` | `transition: transform 200ms ease-out` | `all` anima propiedades de layout |
| `transform: scale(0)` | `transform: scale(0.95); opacity: 0` | Nada aparece de la nada |
| `ease-in` en dropdown | `cubic-bezier(0.16, 1, 0.3, 1)` | ease-in retrasa el feedback |
| Sin `:active` en botón | `transform: scale(0.97)` en `:active` | Los botones deben sentirse físicos |
| `prefers-reduced-motion: none !important` | Suavizar movimiento, mantener opacity | El usuario pidió menos movimiento, no ceguera |
| Hover sin `@media (hover: hover)` | Gating con media query | En móvil el hover queda atascado |
| Animación en cada scroll reveal | Stagger de 80–120ms entre elementos | Todo a la vez abruma |

---

### 10. Qué NO aplicar aquí (contexto importante)

Los siguientes conceptos del repositorio de Emil Kowalski **no aplican a nuestras páginas HTML/CSS** (propuestas, landings, webs muestra):
- **Springs y física iOS** (Framer Motion, WAAPI, `requestAnimationFrame` avanzado) — no usamos React ni librerías de motion en HTML estático
- **`@starting-style`, `setPointerCapture`** — nivel de complejidad que no aplica en HTMLs autónomos
- **`animate-expo` y `write-swift`** — no son relevantes para el stack actual

🟦 **Para DraftDayES (React app):** estas reglas SÍ aplican en su totalidad, más los springs y Framer Motion. Cuando DraftDayES entre en fase de construcción de UI, incorporar los skills `animate`, `review-animations` y `apple-design` de Emil directamente en el entorno de desarrollo.

---

### Uso en propuestas y landings PalferIA

**Usar animación en:**
- Scroll reveal en headlines y cards (estándar PalferIA)
- Counters de 0 → valor real en sección de estadísticas
- Hover en CTAs y tarjetas (con hover gate)
- Transición entre slides en propuestas comerciales

**No usar animación en:**
- Navegación de secciones con nav (la respuesta debe ser instantánea)
- Chips del chat widget (respuesta inmediata, sin delay)
- Formularios mientras el usuario escribe
- Efectos decorativos sobre contenido funcional (tablas, datos)

---

## ACCESIBILIDAD — MÍNIMOS NO NEGOCIABLES

- Contraste texto/fondo: mínimo 4.5:1 (usar herramienta si hay duda)
- Focus visible en todos los elementos interactivos
- Imágenes con `alt` descriptivo
- Color nunca como única forma de transmitir información (añadir icono o texto)
- Semántica HTML correcta: `<button>` para acciones, `<a>` para navegación
- `lang="es"` en `<html>`

---

## RESPONSIVE — BREAKPOINTS ESTÁNDAR

```css
/* Mobile first */
/* Base: 0–479px */
@media (min-width: 480px) { /* mobile grande */ }
@media (min-width: 768px) { /* tablet */ }
@media (min-width: 900px) { /* desktop pequeño */ }
@media (min-width: 1200px) { /* desktop grande */ }

/* Altura para propuestas en iOS Safari */
height: 100dvh; /* en vez de 100vh */
```

---

## TRES DIRECCIONES DE DISEÑO (cuando el brief es abierto)

Si el usuario no especifica estilo → proponer 3 direcciones antes de construir:

```
DIRECCIÓN A — [nombre conceptual]
  Concepto: [una frase]
  Acento:   [color] + [tipografía]
  Signature: [el elemento memorable]
  Tono:     [adjetivos del feeling]

DIRECCIÓN B — [nombre conceptual]
  Concepto: [una frase]
  Acento:   [color] + [tipografía]
  Signature: [el elemento memorable]
  Tono:     [adjetivos del feeling]

DIRECCIÓN C — [nombre conceptual]
  Concepto: [una frase]
  Acento:   [color] + [tipografía]
  Signature: [el elemento memorable]
  Tono:     [adjetivos del feeling]

¿Cuál desarrollamos? ¿O combinamos elementos de varias?
```

---

## SOPORTE TÉCNICO / QA — FALLOS CONOCIDOS EN HTML DE UNA SOLA PÁGINA

Esta sección recoge bugs reales sufridos en producción. Aplicar en QA antes de entregar cualquier página con JavaScript.

### Regla 1 — `?.addEventListener` en elementos de secciones ocultas

**El bug:** `document.getElementById('elemento-en-seccion-oculta').addEventListener(...)` lanza `TypeError: Cannot read properties of null` si el elemento está dentro de una sección que no es visible al cargar. Esto mata la ejecución del script en ese punto — todo el código declarado después (variables `const`, otras funciones) queda sin inicializar.

**Síntoma en producción:** secciones que cargan correctamente de repente no muestran datos, o aparece "Cargando..." permanente sin mensaje de error visible, porque una `const` usada en el render nunca se inicializó (Temporal Dead Zone).

**La regla:**
```js
// ❌ Rompe el script si el elemento no existe en el DOM al cargar
document.getElementById('wa-send-btn').addEventListener('click', handler);

// ✅ Seguro — no hace nada si el elemento no existe
document.getElementById('wa-send-btn')?.addEventListener('click', handler);
```

**Cuándo aplicar:** en TODOS los `getElementById(...).addEventListener` que estén fuera de una función. Si el elemento pertenece a una sección con `display:none` al cargar, es obligatorio usar `?.`.

**Alternativa más robusta:** registrar el listener dentro de la función que activa la sección (`showSection`, `loadWhatsApp`, etc.) en lugar de a nivel global.

---

### Regla 2 — Declarar `const` y `let` ANTES de cualquier código que pueda fallar

**El bug:** si un `const NOMBRE = {...}` está declarado en la línea 200 del script pero hay un error no capturado en la línea 100, el `const` entra en Temporal Dead Zone. Cualquier función que intente acceder a `NOMBRE` (aunque esté definida antes en el archivo) lanzará `ReferenceError: Cannot access 'NOMBRE' before initialization`.

**La regla:** declarar todas las constantes de configuración/datos (objetos de labels, mapas, configuración) al inicio del bloque `<script>`, antes de cualquier código imperativo que pueda lanzar excepciones.

```js
// ✅ Al inicio del script, antes de event listeners y lógica
const ESTADO_LABEL = { borrador: 'Borrador', enviada: 'Enviada', ... };
const CONFIG = { ... };

// Event listeners y código imperativo DESPUÉS
document.getElementById('btn')?.addEventListener(...);
```

---

### Regla 3 — Joins en queries Supabase pueden fallar silenciosamente por RLS

**El bug:** `sb.from('tabla').select('*, otra_tabla(campo)')` puede devolver `[]` en vez de datos si la política RLS de `otra_tabla` bloquea la lectura anon/authenticated para el rol activo. No hay `error` — simplemente llega vacío.

**La regla:** si una query con join devuelve vacío y no hay error, separar en dos queries:
```js
// Query principal sin join
const { data } = await sb.from('propuestas').select('id, titulo, prospecto_id');

// Fetch separado de los nombres relacionados
const { data: prosp } = await sb.from('prospectos').select('id, nombre').in('id', ids);
const map = Object.fromEntries((prosp || []).map(p => [p.id, p.nombre]));
```

---

### Regla 4 — Envolver funciones async de carga en try-catch visible

Las funciones `async` que hacen queries no deben dejar al usuario con "Cargando..." si hay una excepción. Siempre mostrar el error en el contenedor:

```js
async function loadSeccion() {
  const contenedor = document.getElementById('mi-seccion');
  contenedor.innerHTML = '<p>Cargando...</p>';
  try {
    const { data, error } = await sb.from('tabla').select('*');
    if (error) { contenedor.innerHTML = `<p>Error: ${esc(error.message)}</p>`; return; }
    // render...
  } catch (ex) {
    contenedor.innerHTML = `<p>Error inesperado: ${esc(String(ex))}</p>`;
  }
}
```

---

## CHECKLIST ANTES DE ENTREGAR

```
☐ Plan aprobado antes de construir
☐ Sin clusters AI-genéricos
☐ Elemento signature presente y justificado
☐ Fuentes cargadas correctamente (no fallback genérico)
☐ Responsive probado en 375px y 1280px
☐ Contraste mínimo 4.5:1 en texto principal
☐ Focus visible en interactivos
☐ prefers-reduced-motion respetado
☐ localStorage si hay estado que persistir
☐ Contador de slides no hardcodeado (propuestas)
☐ Sin comentarios explicativos en el código entregado
☐ [JS] ?.addEventListener en todos los elementos de secciones ocultas
☐ [JS] const/let declarados antes de cualquier código imperativo
☐ [JS] Queries con join probadas con RLS real — no asumir que devuelven datos
☐ [JS] try-catch visible en todas las funciones async de carga
```
