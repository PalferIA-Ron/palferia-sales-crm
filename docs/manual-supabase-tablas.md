# Manual de Tablas Supabase — PalferIA Sales CRM
**Proyecto Supabase:** `aqaiqmsypbwhgknbbmae`  
**URL base API:** `https://aqaiqmsypbwhgknbbmae.supabase.co/rest/v1/`  
**CRM en producción:** https://sales.palferia.me  
**Última actualización:** 21 agosto 2026

---

## Índice

1. [prospectos](#1-prospectos)
2. [pipeline_log](#2-pipeline_log)
3. [mensajes_whatsapp](#3-mensajes_whatsapp)
4. [propuestas](#4-propuestas)
5. [Repositorio y accesos](#5-repositorio-y-accesos)
6. [Preguntas frecuentes](#6-preguntas-frecuentes)

---

## 1. prospectos

### ¿Para qué sirve?
Es la tabla central del CRM. Guarda todos los negocios o academias que se han identificado como clientes potenciales de PalferIA, tanto para COM-studio como para ME-sport.

### Campos

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | uuid | Identificador único, generado automáticamente |
| `created_at` | timestamptz | Fecha y hora de creación |
| `nombre` | text | Nombre del negocio (obligatorio) |
| `municipio` | text | Ciudad o municipio |
| `sector` | text | Sector del negocio (fontanería, fisioterapia, etc.) |
| `score` | integer (0-100) | Puntuación de oportunidad digital (menor = más oportunidad) |
| `estado` | text | Estado en el pipeline (ver valores abajo) |
| `proyecto` | text | `COM-studio` o `ME-sport` |
| `email` | text | Email de contacto |
| `telefono` | text | Teléfono de contacto |
| `web` | text | URL de su web (si tiene) |
| `instagram` | text | Cuenta de Instagram (si tiene) |
| `pain` | text | Problema principal detectado |
| `semana` | integer | Semana de prospección en que se identificó |
| `socios_est` | text | Socios o estructura estimada |
| `ultimo_contacto` | date | Fecha del último contacto realizado |
| `proxima_accion` | text | Qué hacer con este prospecto a continuación |
| `notas` | text | Notas internas libres |

### Valores del campo `estado`

| Valor | Significado | Icono CRM |
|---|---|---|
| `identified` | Identificado, no contactado | 🔍 |
| `contacted` | Email enviado | 📧 |
| `waiting` | Esperando respuesta | ⏳ |
| `call` | Llamada programada | 📞 |
| `proposal` | Propuesta enviada | 📄 |
| `negotiating` | En negociación | 🤝 |
| `closed` | Cliente cerrado | ✅ |
| `discarded` | Descartado | ❌ |
| `alternative` | Canal alternativo (WhatsApp, llamada fría) | 🔄 |

### ¿Quién escribe en esta tabla?
- **kit-prospeccion v3** → inserta nuevos prospectos automáticamente al finalizar una búsqueda
- **CRM (sales.palferia.me)** → el usuario puede editar y actualizar manualmente desde la ficha
- **n8n** → puede actualizar el estado cuando llega un mensaje de WhatsApp de ese número

### Objetivo
Tener los 20 prospectos objetivo (10 COM-studio + 10 ME-sport) centralizados, con su estado actualizado en tiempo real y accesibles desde cualquier dispositivo.

### Futuras mejoras
- [ ] Campo `web_score` integer — puntuación SEO específica de la web
- [ ] Campo `propuesta_id` uuid — link directo a la propuesta generada
- [ ] Campo `valor_estimado` integer — ticket estimado en euros
- [ ] Campo `canal_origen` text — cómo se encontró (kit-prospeccion, manual, referido)
- [ ] Integración automática con kit-auditoria-seo al identificar un prospecto con web

---

## 2. pipeline_log

### ¿Para qué sirve?
Registro cronológico de todas las acciones realizadas con cada prospecto. Es el historial completo del proceso comercial: cuándo se contactó, qué pasó, qué se envió.

### Campos

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | uuid | Identificador único |
| `created_at` | timestamptz | Fecha y hora del registro |
| `fecha` | date | Fecha de la acción (puede ser distinta de created_at) |
| `proyecto` | text | `COM-studio` o `ME-sport` |
| `prospecto_id` | uuid | Referencia al prospecto (puede ser null si se borra) |
| `prospecto_nombre` | text | Nombre del prospecto (copia de seguridad si se borra) |
| `accion` | text | Qué se hizo (email enviado, llamada, propuesta, etc.) |
| `resultado` | text | Qué pasó (sin respuesta, reunión agendada, cerrado, etc.) |

### ¿Quién escribe en esta tabla?
- **kit-prospeccion v3** → entrada automática al identificar un prospecto nuevo
- **CRM (sales.palferia.me)** → el usuario puede añadir entradas manualmente desde el panel Log
- **n8n** → puede registrar automáticamente cuando llega una respuesta de WhatsApp

### Objetivo
Tener trazabilidad completa de cada prospecto sin depender de la memoria. Si alguien pregunta "¿cuándo le contactamos por última vez?", la respuesta está en esta tabla.

### Futuras mejoras
- [ ] Campo `canal` text — por dónde fue la acción (email, WhatsApp, llamada, reunión)
- [ ] Campo `usuario` text — quién realizó la acción (útil si hay equipo)
- [ ] Alertas automáticas: si un prospecto lleva +7 días en `waiting` sin log → notificación
- [ ] Dashboard de actividad semanal generado desde esta tabla

---

## 3. mensajes_whatsapp

### ¿Para qué sirve?
Guarda todos los mensajes de WhatsApp que entran o salen a través de OpenWA (`wa.palferia.me`). Permite ver el historial de conversación de cada prospecto directamente en el CRM.

### Campos

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | uuid | Identificador único |
| `created_at` | timestamptz | Fecha de inserción en la BD |
| `prospecto_id` | uuid | Referencia al prospecto (si el número está en la tabla prospectos) |
| `session_id` | text | Sesión de OpenWA (ej: `palferia-principal`) |
| `telefono` | text | Número de teléfono del contacto (sin @c.us) |
| `direccion` | text | `inbound` (mensaje recibido) o `outbound` (mensaje enviado) |
| `contenido` | text | Texto del mensaje |
| `timestamp_wa` | timestamptz | Timestamp original de WhatsApp |

### ¿Quién escribe en esta tabla?
- **n8n workflow `OpenWA → Supabase CRM`** → escribe automáticamente cada mensaje que entra o sale por OpenWA
- **Plugin palferia-ai-agent** (futuro) → escribirá también los mensajes generados por IA

### Cómo funciona el flujo actual
```
Mensaje WhatsApp entrante
    → OpenWA (wa.palferia.me)
    → Webhook n8n (openwa-messages)
    → Busca el número en prospectos
    → Guarda en mensajes_whatsapp con prospecto_id si existe
```

### Objetivo
Ver en el CRM todo el historial de WhatsApp de cada prospecto sin salir de la plataforma. En la ficha del prospecto debe aparecer el chat completo.

### Futuras mejoras
- [ ] Campo `es_bot` boolean — si el mensaje fue enviado por el agente IA (plugin)
- [ ] Campo `tipo_media` text — para mensajes con imagen, audio, documento
- [ ] Campo `transcripcion` text — transcripción del audio si se usa el plugin `voice-transcription`
- [ ] Vista de chat en el CRM con burbujas (inbound izquierda / outbound derecha)
- [ ] Integración con plugin `palferia-ai-agent` de OpenWA (fin de semana 23-24/08)

---

## 4. propuestas

### ¿Para qué sirve?
Guarda los metadatos de cada propuesta generada para un prospecto. El HTML de la propuesta vive en el VPS (`/public/propuestas/[slug].html`), y esta tabla guarda el enlace, el estado y la información de seguimiento.

### Campos

| Campo | Tipo | Descripción |
|---|---|---|
| `id` | uuid | Identificador único |
| `created_at` | timestamptz | Fecha de creación |
| `prospecto_id` | uuid | Prospecto al que pertenece |
| `slug` | text (único) | Token UUID en la URL (ej: `8f3d2a1b-cortinajes`) |
| `url` | text | URL pública completa de la propuesta |
| `titulo` | text | Título de la propuesta |
| `estado` | text | Estado actual (ver valores abajo) |
| `proyecto` | text | `COM-studio` o `ME-sport` |
| `skills_usadas` | text[] | Array de skills que generaron la propuesta |
| `notas_internas` | text | Notas para la vista `?interno` (prep reunión, etc.) |
| `fecha_envio` | date | Cuándo se compartió con el prospecto |

### Valores del campo `estado`

| Valor | Significado |
|---|---|
| `borrador` | Generada pero no enviada al prospecto |
| `enviada` | URL compartida con el prospecto |
| `vista` | El prospecto abrió la URL (futuro: tracking de visitas) |
| `aceptada` | El prospecto confirmó interés |
| `rechazada` | El prospecto rechazó la propuesta |

### Seguridad de las URLs

Las propuestas tienen URLs con token UUID imposible de adivinar:
```
✅ sales.palferia.me/propuestas/8f3d2a1b-9c4e-4f7a-cortinajes.html  → visible
❌ sales.palferia.me/propuestas/                                       → 403
❌ sales.palferia.me/propuestas/cortinajes.html                        → 404
```

El prospecto solo puede ver la propuesta que le enviaste. No puede ver otras ni listar el directorio.

### Dos vistas de cada propuesta

**Vista cliente** (URL normal):
- Propuesta completa, diseño profesional
- Calculadora ROI interactiva
- CTA para agendar llamada

**Vista interna** (`?interno` al final de la URL):
- Prep de reunión (puntos clave, contexto del prospecto)
- Objeciones con respuestas preparadas
- Calculadora ROI con sliders editables
- Cuestionario BPM para diagnóstico de procesos
- Entregables del plan seleccionado
- Próximos pasos post-reunión

### ¿Quién escribe en esta tabla?
- **CRM (sales.palferia.me)** → botón "Generar propuesta" en la ficha del prospecto (en desarrollo)
- **Claude Code** → cuando se genera la landing manualmente con los skills

### Skills que contribuyen a cada propuesta

| Situación del prospecto | Skills que se ejecutan |
|---|---|
| Sin web | `kit-auditoria-negocio` + `Orquestador` + `hormozi-skill` |
| Con web deficiente | `kit-auditoria-seo` + `kit-auditoria-negocio` + `hormozi-skill` |
| Con Instagram activo | `kit-instagram-web` + `kit-auditoria-negocio` |
| Academia deportiva (ME-sport) | `kit-auditoria-negocio` + `Orquestador` + `mantenimiento-ia` |

### Futuras mejoras
- [ ] Tracking de visitas — saber si el prospecto abrió la URL y cuántas veces
- [ ] Botón "Generar propuesta" en el CRM con detección automática del tipo de prospect
- [ ] Envío de la URL por WhatsApp o email desde el propio CRM
- [ ] Versiones de propuesta — poder actualizar sin cambiar la URL
- [ ] Caducidad opcional — la propuesta expira a los 30 días si no se acepta

---

## 5. Repositorio y accesos

### GitHub
- **Repo:** https://github.com/PalferIA-Ron/palferia-sales-crm
- **Branch principal:** `main`
- **Deploy automático:** GitHub Actions → push a main → rsync al VPS en segundos
- **SSH key local:** `/Users/macbook/.ssh/palferia_vps`
- **Comando deploy manual:**
  ```bash
  rsync -avz -e "ssh -i ~/.ssh/palferia_vps" public/ root@31.97.192.164:/var/www/sales.palferia.me/
  ```

### VPS
- **IP:** `31.97.192.164`
- **Contenedor CRM:** `root-sales-crm-1`
- **Ruta de archivos en VPS:** `/var/www/sales.palferia.me/`
- **Nginx config:** `/etc/nginx/conf.d/default.conf` (dentro del contenedor)

### Supabase
- **Proyecto:** `aqaiqmsypbwhgknbbmae`
- **URL:** `https://aqaiqmsypbwhgknbbmae.supabase.co`
- **Anon key (frontend):** en `public/index.html` y `public/crm.html` — es pública por diseño
- **Service role key (scripts locales):** en `.env.local` — NUNCA en GitHub

### Archivos clave del proyecto
```
palferia-sales-crm/
├── public/
│   ├── index.html              ← login
│   ├── crm.html                ← CRM completo
│   └── propuestas/             ← landings generadas (protegidas)
├── supabase/
│   ├── schema.sql              ← schema original
│   └── migration-propuestas.sql ← migración tablas nuevas
├── docs/
│   ├── manual-sales-palferia-me.md
│   ├── manual-wa-palferia-me.md
│   ├── manual-n8n.md
│   ├── manual-supabase-tablas.md  ← este archivo
│   ├── analisis-integracion-skills.md
│   └── roadmap-plugin-openwa.md
├── .env.local                  ← secrets locales (no en GitHub)
├── .gitignore                  ← protege .env.local
└── .github/workflows/deploy.yml ← deploy automático
```

---

## 6. Preguntas frecuentes

### ¿Puedo perder los datos de Supabase?
Supabase hace backups automáticos diarios. Además, todos los datos de código están en GitHub. Lo único que no está en GitHub son los datos de la BD (prospectos, mensajes, etc.) — esos viven en Supabase.

### ¿Qué pasa si borro un prospecto?
- Sus mensajes de WhatsApp se borran también (cascade delete)
- Su propuesta se borra también (cascade delete)
- Su log en pipeline_log se mantiene pero `prospecto_id` queda en null (set null)

### ¿Cómo añado un prospecto manualmente?
Desde el CRM → sección Prospectos → botón "Nuevo prospecto" → rellena el formulario.

### ¿Cómo añade prospectos el kit-prospeccion?
Automáticamente al finalizar una búsqueda. Verifica que no exista antes de insertar (por nombre + municipio), luego escribe en `prospectos` y en `pipeline_log`.

### ¿Cómo veo el historial de WhatsApp de un prospecto?
En el CRM → sección WhatsApp → busca el número. Próximamente estará integrado directamente en la ficha del prospecto.

### ¿Cómo comparto una propuesta con un cliente?
1. Genera la propuesta desde la ficha del prospecto
2. Copia la URL `sales.palferia.me/propuestas/[token].html`
3. Envíala por WhatsApp o email directamente desde el CRM (próximamente)

### ¿Puede el cliente ver otras propuestas de otros clientes?
No. Cada URL tiene un token UUID único e imposible de adivinar. Si intenta acortar la URL, recibe un error 403.

### ¿Dónde están los secrets y API keys?
- **Service role key de Supabase** → `.env.local` (solo en tu máquina, nunca en GitHub)
- **Anon key de Supabase** → en el HTML del CRM (es pública por diseño de Supabase)
- **API key de OpenWA** → en el nginx del VPS (no expuesta en el frontend)
- **API key de n8n** → en n8n (solo accesible desde el servidor)

### ¿Cómo hago un backup manual de la BD?
Supabase → Settings → Backups → Download backup. O desde la CLI:
```bash
supabase db dump --project-ref aqaiqmsypbwhgknbbmae > backup-$(date +%Y%m%d).sql
```
