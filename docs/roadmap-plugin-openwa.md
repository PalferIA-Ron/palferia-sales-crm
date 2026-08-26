# Roadmap — Plugin PalferIA AI Agent para OpenWA
**Fecha inicio:** Fin de semana 23-24 agosto 2026  
**Objetivo:** Crear un plugin nativo de OpenWA que integre IA (Claude) + Supabase sin reemplazar la infraestructura actual

---

## Contexto

OpenWA (desplegado en `wa.palferia.me`) tiene un sistema de plugins propio basado en:
- `manifest.json` — declara hooks, permisos y configuración
- `index.ts` → `dist/index.js` — lógica compilada con esbuild, corre en worker thread aislado
- Referencia: https://github.com/rmyndharis/OpenWA-plugins.git

**Decisión:** Crear plugin propio `palferia-ai-agent` en lugar de migrar a Baileys (whatsapp-ai-agent-kit). Motivos:
- No hay que romper la sesión de WhatsApp activa
- Plugin es configurable por sesión (multi-cliente desde el mismo OpenWA)
- Sandboxed — si falla el plugin, OpenWA sigue funcionando
- Menor superficie de mantenimiento

---

## Fase 1 — Preparación (viernes noche / sábado mañana)

### 1.1 Estudiar el repo de referencia
- [ ] Clonar `https://github.com/rmyndharis/OpenWA-plugins.git` en local
- [ ] Leer completo `http-action/index.ts` — es el plugin más parecido a lo que necesitamos
- [ ] Leer `supabase-otp-hook/index.ts` — referencia de integración con Supabase
- [ ] Identificar el tipo `HookContext` y `HookResult` del SDK de OpenWA
- [ ] Entender cómo se instala un plugin en la instancia de `wa.palferia.me`

### 1.2 Entender el SDK de OpenWA
- [ ] Buscar la documentación del tipo `ctx` (capabilities: `conversations`, `storage`, `net`)
- [ ] Confirmar cómo se registran hooks: `ctx.registerHook('message:received', ...)`
- [ ] Confirmar cómo se envía un mensaje: `ctx.conversations.send(phone, text)`
- [ ] Confirmar cómo se usa storage: `ctx.storage.get/set` (para historial de conversación)

### 1.3 Setup de entorno de desarrollo
- [ ] Crear carpeta `palferia-ai-agent/` en el workspace
- [ ] Instalar dependencias: `typescript`, `esbuild`, `@types/node`
- [ ] Configurar `tsconfig.json` + script de build con esbuild
- [ ] Crear `manifest.json` base con los campos mínimos

---

## Fase 2 — Construcción del plugin (sábado)

### 2.1 manifest.json
```json
{
  "name": "palferia-ai-agent",
  "version": "1.0.0",
  "hooks": ["message:received"],
  "permissions": ["messages:send", "net:fetch", "storage:use"],
  "config": {
    "claudeApiKey":  { "type": "string", "masked": true, "required": true },
    "supabaseUrl":   { "type": "string", "required": true },
    "supabaseKey":   { "type": "string", "masked": true, "required": true },
    "systemPrompt":  { "type": "textarea", "required": true },
    "humanPhone":    { "type": "string", "description": "Número para derivar a humano" },
    "maxHistory":    { "type": "number", "default": 10 },
    "respondGroups": { "type": "boolean", "default": false }
  }
}
```

### 2.2 index.ts — flujo principal

```
message:received
    │
    ├─ ¿Es mensaje de grupo? → ignorar (si respondGroups=false)
    ├─ ¿Es mensaje propio (fromMe)? → ignorar
    ├─ ¿Ya procesado? (dedup por storage) → ignorar
    │
    ├─ Guardar mensaje en Supabase mensajes_whatsapp (dirección: inbound)
    │
    ├─ Recuperar historial de Supabase (últimos N mensajes del número)
    │
    ├─ Llamar Claude API (system prompt + historial + mensaje actual)
    │
    ├─ Guardar respuesta en Supabase (dirección: outbound, es_bot: true)
    │
    └─ Enviar respuesta por WhatsApp (ctx.conversations.send)
```

### 2.3 Módulos internos a construir

| Módulo | Archivo | Responsabilidad |
|---|---|---|
| Hook principal | `index.ts` | Registrar hook, orquestar flujo |
| Cliente Claude | `lib/claude.ts` | Llamada a Anthropic API, gestión de historial |
| Cliente Supabase | `lib/supabase.ts` | Guardar mensajes, recuperar historial, buscar prospecto |
| Dedup | `lib/dedup.ts` | Storage para evitar doble procesamiento |
| Derivación | `lib/derivar.ts` | Detectar palabras clave → enviar aviso a humanPhone |

### 2.4 Build
```bash
npx esbuild index.ts --bundle --platform=node --format=cjs --outfile=dist/index.js
zip -r palferia-ai-agent.zip manifest.json dist/
```

---

## Fase 3 — Pruebas en local (sábado tarde)

- [ ] Simular un `HookContext` mock para testear sin OpenWA real
- [ ] Probar flujo completo: mensaje entrante → Claude → respuesta
- [ ] Verificar que los mensajes llegan a Supabase correctamente
- [ ] Probar dedup: mismo mensaje dos veces → solo una respuesta
- [ ] Probar derivación: "hablar con una persona" → aviso a humanPhone

---

## Fase 4 — Deploy en wa.palferia.me (domingo)

- [ ] Subir el ZIP del plugin al panel de OpenWA (`wa.palferia.me`)
- [ ] Configurar las variables desde el dashboard:
  - `claudeApiKey` — API key de Anthropic
  - `supabaseUrl` — `https://aqaiqmsypbwhgknbbmae.supabase.co`
  - `supabaseKey` — `sb_publishable_lxcUh7WtArLQbbP7CA-1Vw_yt7wOyje`
  - `systemPrompt` — prompt base de PalferIA (configurable por sesión)
  - `humanPhone` — número de Adrián para derivaciones
- [ ] Activar plugin en la sesión `palferia-principal`
- [ ] Enviar mensaje de prueba desde otro número
- [ ] Verificar en Supabase que el mensaje y la respuesta aparecen en `mensajes_whatsapp`
- [ ] Verificar en el CRM (`sales.palferia.me`) que el chat aparece en el panel WhatsApp

---

## Fase 5 — Iteración post-deploy (semana siguiente)

- [ ] Ajustar `systemPrompt` según las primeras conversaciones reales
- [ ] Añadir lógica de **detección de prospecto**: si el número está en `prospectos`, usar contexto del negocio en el prompt
- [ ] Añadir lógica de **calificación**: si el agente detecta intención de compra → cambiar estado del prospecto en Supabase
- [ ] Añadir modo **HUMAN**: si el prospecto está en modo humano en el CRM, el plugin no responde
- [ ] Versión 2: plugin separado por cliente (Cortinajes Valls, Tecniluispa, etc.) con prompts distintos

---

## Arquitectura final objetivo

```
WhatsApp
    │ mensaje entrante
    ▼
OpenWA (wa.palferia.me)
    │
    ▼
Plugin palferia-ai-agent
    ├── Supabase mensajes_whatsapp  ← guarda todo
    ├── Claude API                  ← genera respuesta
    └── OpenWA conversations.send   ← responde
    
    ↕ sincronización

CRM (sales.palferia.me)
    └── Panel WhatsApp              ← vista unificada + modo humano
```

---

## Decisiones pendientes para el fin de semana

1. **¿Un plugin genérico o uno por proyecto (COM-studio / ME-sport)?**
   - Opción A: un plugin con `systemPrompt` configurable por sesión → más flexible
   - Opción B: un plugin por proyecto con lógica propia → más control

2. **¿Historial en Supabase o en el storage local del plugin?**
   - Supabase: consistente con el CRM, visible en el dashboard
   - Storage local: más rápido, no depende de conexión externa

3. **¿Derivación a humano por WhatsApp o por notificación en el CRM?**
   - WhatsApp directo: más inmediato
   - CRM: más ordenado, con contexto de la conversación

---

## Referencias

- Repo plugins: https://github.com/rmyndharis/OpenWA-plugins.git
- OpenWA dashboard: https://wa.palferia.me
- Supabase proyecto: https://aqaiqmsypbwhgknbbmae.supabase.co
- CRM: https://sales.palferia.me
- Anthropic API docs: https://docs.anthropic.com/en/api
