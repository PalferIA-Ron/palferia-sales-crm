# Análisis de Integración — Skills con Infraestructura PalferIA
**Fecha:** 20 de agosto de 2026  
**Autor:** Adrián Gallardo / PalferIA  
**Scope:** Integración de dos skills con los subdominios activos

| Subdominio | Skill a integrar | Dificultad |
|---|---|---|
| `wa.palferia.me` | `whatsapp-ai-agent-kit` | MEDIA (reemplazando OpenWA) |
| `sales.palferia.me` | `kit-prospeccion` | FÁCIL |

---

## 1. whatsapp-ai-agent-kit → wa.palferia.me

### Qué hace el kit

Sistema completo de agente IA para WhatsApp con:
- **Backend:** Baileys 6.7 (cliente WhatsApp Web no oficial, igual que OpenWA)
- **LLM:** OpenRouter (soporta Claude, GPT-4, Mistral, 200+ modelos vía una API key)
- **DB local:** SQLite WAL-mode — tablas: `conversations`, `messages`, `outbox`, `connection_state`, `history`
- **Dashboard:** Next.js 16 + React 19 + Tailwind en `localhost:3000`
- **Herramientas IA:** `guardarLead`, `calificar` (0-10), `agendar` (Cal.com), `derivarHumano`
- **Deploy:** Nixpacks (no Docker requerido, pero compatible)

### El problema central: doble sesión

OpenWA y Baileys son dos implementaciones del mismo protocolo WhatsApp Web.
**No pueden ejecutarse simultáneamente sobre el mismo número** — se pelean por la sesión y ambos fallan.

### Escenarios de integración

#### ✅ Opción A — Reemplazar OpenWA con el Kit (RECOMENDADA)

**Dificultad:** MEDIA · **Tiempo estimado:** 3-5 días

Proceso:
1. Detener OpenWA en el VPS (`docker stop root-openwa-api-1`)
2. Desplegar el kit en el mismo VPS (puerto 3001, detrás de Traefik → `wa.palferia.me`)
3. Escanear nuevo QR desde el dashboard del kit
4. Modificar `src/lib/baileys/handler.ts` para escribir mensajes también en Supabase `mensajes_whatsapp`
5. Actualizar el CRM (`crm.html`) — el panel WhatsApp pasa de llamar a la API OpenWA (`:2785`) a llamar a la API del kit (`/api/conversations`, `/api/messages`)

**Código a añadir en `handler.ts` (bridge → Supabase):**
```typescript
// Tras insertMessage(convo.id, "user", text)
await fetch('https://aqaiqmsypbwhgknbbmae.supabase.co/rest/v1/mensajes_whatsapp', {
  method: 'POST',
  headers: {
    'apikey': process.env.SUPABASE_KEY,
    'Content-Type': 'application/json'
  },
  body: JSON.stringify({
    session_id: 'palferia-principal',
    telefono: phone,
    contenido: text,
    direccion: 'inbound',
    timestamp_wa: new Date().toISOString()
  })
});
```

**Lo que ganas respecto a OpenWA:**
- Agente IA que responde automáticamente (OpenWA solo guarda mensajes, no responde)
- Clasificación y puntuación de leads en tiempo real
- Panel unificado de conversaciones con switch AI ↔ humano
- Cola de mensajes salientes con control manual

**Lo que pierdes:**
- Historial de sesión de OpenWA (hay que escanear QR de nuevo)
- ~15 min de downtime durante la migración

---

#### ⚠️ Opción B — Mantener OpenWA, Kit como cerebro IA (COMPLEJA)

**Dificultad:** ALTA · **No recomendada ahora**

El kit está diseñado para recibir eventos en tiempo real de Baileys, no para hacer polling de una BD.
Habría que reescribir `handler.ts` para leer de Supabase cada 5 segundos en lugar de recibir eventos.
Añade latencia, complejidad y puntos de fallo sin ventajas claras sobre la Opción A.

---

#### 🔮 Opción C — Esperar API oficial de Meta con Coexistence (FUTURO)

Meta tiene una feature llamada **Coexistence** que permitirá usar API oficial + app móvil en el mismo número.
**Estado actual:** no disponible en España/UE. Timeline incierto (posiblemente 2027).
Cuando llegue: migrar ambos sistemas a la API oficial y deprecar Baileys + OpenWA.

---

### Decisión recomendada para wa.palferia.me

**Ejecutar Opción A en la semana 3** (después de validar el CRM en producción).

Variables de entorno necesarias en el VPS:
```
OPENROUTER_API_KEY=sk-or-...
OPENROUTER_MODEL=anthropic/claude-3-5-sonnet
SUPABASE_URL=https://aqaiqmsypbwhgknbbmae.supabase.co
SUPABASE_KEY=sb_publishable_lxcUh7WtArLQbbP7CA-1Vw_yt7wOyje
```

---

## 2. kit-prospeccion → sales.palferia.me

### Qué hace el kit

Skill de Claude Code (no código ejecutable standalone) que:
- Pregunta al usuario: tipo de negocio, zona, servicio que vende PalferIA
- Ejecuta búsquedas con `WebSearch` + `WebFetch` (o Firecrawl si está configurado)
- Analiza la presencia digital de cada web encontrada (HTTPS, SEO, responsive, redes)
- Puntúa la oportunidad (0-100, mayor = más pain digital = más urgente contactar)
- Genera un `HTML dashboard` + `JSON export` con todos los prospectos

**Lo que genera ahora:**
```
COM-studio/prospeccion-horta-nord-semana1.html
COM-studio/prospeccion-horta-nord-semana1.json
```

**Lo que falta:** escribir ese JSON directamente en la tabla `prospectos` de Supabase.

### Plan de integración

#### Paso 1 — Definir el formato de salida JSON estándar

El skill debe generar JSON con exactamente los campos de la tabla `prospectos`:

```json
{
  "prospectos": [
    {
      "nombre": "Romaib Fontaneros",
      "municipio": "Paterna",
      "sector": "Fontanería",
      "web": "https://romaib.es",
      "telefono": "+34961234567",
      "email": "info@romaib.es",
      "score": 28,
      "pain_principal": "Sin WhatsApp, sin formulario presupuesto",
      "proyecto": "COM-studio",
      "estado": "nuevo",
      "semana": 1
    }
  ]
}
```

#### Paso 2 — Añadir llamada HTTP al final del skill

Modificar `.claude/skills/06-prospeccion-firecrawl.md` — Paso 5 (generación) para que tras crear el HTML, también ejecute:

```bash
# Insertar prospectos en Supabase
curl -X POST https://aqaiqmsypbwhgknbbmae.supabase.co/rest/v1/prospectos \
  -H "apikey: sb_publishable_lxcUh7WtArLQbbP7CA-1Vw_yt7wOyje" \
  -H "Content-Type: application/json" \
  -d @prospeccion-output.json
```

O via Bash tool directamente desde Claude Code si el skill lo soporta.

#### Paso 3 — Log automático en pipeline_log

Tras insertar cada prospecto, añadir entrada en `pipeline_log`:
```json
{
  "prospecto_id": "<uuid del insertado>",
  "estado_nuevo": "nuevo",
  "notas": "Identificado via kit-prospeccion semana X",
  "fecha": "2026-08-20T00:00:00Z"
}
```

#### Paso 4 — Botón "Importar prospectos" en el CRM (opcional)

En `sales.palferia.me`, añadir en la sección Prospectos un botón que:
1. Abre modal para pegar el JSON generado por el kit
2. Hace bulk-insert en Supabase `prospectos`
3. Crea un log por cada uno en `pipeline_log`

Esto como alternativa manual mientras se automatiza el paso 2.

---

### Complejidad: FÁCIL

El kit ya produce el output correcto. Solo se necesita:
1. Estandarizar el esquema JSON de salida (30 min)
2. Añadir llamada curl/fetch al final del skill (1-2 horas)
3. Opcional: botón de importación en el CRM (2-3 horas)

**Tiempo total estimado:** 1 día

---

## Roadmap de integración

| Semana | Tarea | Subdominio | Dificultad |
|---|---|---|---|
| Semana 2 (esta semana) | Estandarizar JSON + añadir curl a kit-prospeccion | sales.palferia.me | Fácil |
| Semana 2 | Botón importación bulk en CRM | sales.palferia.me | Fácil |
| Semana 3 | Sustituir OpenWA por whatsapp-ai-agent-kit | wa.palferia.me | Media |
| Semana 3 | Bridge handler.ts → Supabase mensajes_whatsapp | wa.palferia.me | Media |
| Semana 4 | Actualizar panel WhatsApp en CRM (API kit) | sales.palferia.me | Media |
| Semana 5 | Conectar herramienta `calificar` del kit con tabla prospectos | sales+wa | Media |

---

## Seguridad

- La API Key de OpenWA (`M4rtin091121+`) está en texto plano en la config — moverla a variable de entorno en el VPS
- La Supabase Anon Key es pública (por diseño) pero las policies RLS limitan el acceso a usuarios autenticados
- El kit de WhatsApp expone un dashboard en localhost:3000 — usar Cloudflare Access o autenticación básica al desplegarlo en el VPS
- Las API keys de OpenRouter y Supabase deben ir en `.env.local`, nunca commiteadas al repo
