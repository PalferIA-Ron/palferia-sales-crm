---
name: n8n-api-manager
description: Gestiona un servidor n8n a través de su API REST pública. Usa esta skill siempre que el usuario quiera listar, crear, editar, activar/desactivar, borrar, exportar o auditar workflows de n8n; revisar ejecuciones; o pedir mejoras sobre flujos existentes. Actívala incluso si el usuario no nombra "API" — frases como "mis workflows", "mi servidor n8n", "audita mi flujo X", "crea un workflow que..." o "qué workflows tengo activos" son señal suficiente. Es una skill operativa (hace llamadas reales), no sólo de diseño.
---

# n8n API Manager

Esta skill permite a Claude **operar directamente sobre un servidor n8n** vía
su API REST pública (`/api/v1`). A diferencia de `prompt-builder-agentes-n8n`
(que sólo redacta prompts para pegar en n8n), aquí Claude **sí ejecuta**:
listar, crear, editar, activar, auditar y exportar workflows.

## Configuración inicial (una sola vez)

La skill lee la URL y la API key del entorno:

```bash
export N8N_API_URL="https://n8n.srv1267531.hstgr.cloud"   # SIN /api/v1 al final
export N8N_API_KEY="AKI TU API"
```

Para obtener la API key en n8n: **Settings → n8n API → Create API Key**.

Si las variables no están definidas, todas las operaciones fallarán con un
mensaje claro pidiéndolas. **Claude NO debe inventar valores ni pedir la key
en la conversación si ya está en el entorno** — sólo si el primer comando
falla con `Falta N8N_API_KEY`.

## Estructura

```
n8n-api-manager/
├── SKILL.md                       (este archivo)
├── scripts/
│   ├── n8n_client.py              # Cliente API + CLI (list, get, download, create, update, activate, ...)
│   ├── audit_workflow.py          # Auditor de workflows con propuestas de mejora
│   ├── workflow_builder.py        # Helper para construir JSON válido de workflows
│   └── workflow_diff.py           # Compara dos versiones de un workflow antes de aplicar PUT
└── references/
    ├── api_endpoints.md           # Referencia rápida de endpoints
    ├── node_catalog.md            # Catálogo de nodos y patrones
    └── troubleshooting.md         # Errores frecuentes y soluciones
```

## Flujo de trabajo de Claude

Cuando el usuario pide algo relacionado con n8n, Claude debe:

1. **Identificar la intención** en una de estas categorías:
   - **Exploración**: "qué workflows tengo", "muéstrame los activos", "cuántas ejecuciones fallaron"
   - **Inspección**: "enséñame el workflow X", "qué hace el flujo Y"
   - **Auditoría**: "audita mi flujo", "revisa qué se podría mejorar", "encuentra problemas"
   - **Modificación**: "edita el workflow X para…", "añade un nodo Y", "activa/desactiva Z"
   - **Creación**: "crea un workflow que…"
   - **Diagnóstico**: "por qué falla el workflow X", "muéstrame el último error"

2. **Antes de cualquier modificación destructiva** (UPDATE, DELETE,
   activate/deactivate), Claude debe:
   - Explicar exactamente qué va a hacer y sobre qué workflow (nombre + id).
   - **Pedir confirmación explícita** del usuario en la conversación.
   - Si va a editar, antes hacer un `GET` y mostrar el diff conceptual.

3. **Para crear workflows**, Claude:
   - Hace 2-4 preguntas rápidas (trigger, entradas, salida, herramientas) sólo si la descripción del usuario no las cubre ya.
   - Construye el JSON paso a paso con `workflow_builder.py` (importable desde Python).
   - Valida con `validate(...)` antes de enviar.
   - Crea el workflow **inactivo por defecto** y le dice al usuario que lo revise en la UI antes de activarlo.

4. **Después de cada operación**, Claude muestra:
   - El nombre + id del workflow afectado.
   - URL directa del editor: `<N8N_API_URL>/workflow/<id>` (sin `/api/v1`).
   - Próximos pasos sugeridos.

## Cómo ejecutar las operaciones

Hay dos maneras equivalentes. Usa la que mejor encaje en cada caso.

### a) CLI rápida (para consultas simples)

```bash
python /home/claude/n8n-api-manager/scripts/n8n_client.py ping
python /home/claude/n8n-api-manager/scripts/n8n_client.py list
python /home/claude/n8n-api-manager/scripts/n8n_client.py get <id>
python /home/claude/n8n-api-manager/scripts/n8n_client.py download <id> [path.json]
python /home/claude/n8n-api-manager/scripts/n8n_client.py update <id> <edited.json>
python /home/claude/n8n-api-manager/scripts/n8n_client.py activate <id>
python /home/claude/n8n-api-manager/scripts/n8n_client.py deactivate <id>
python /home/claude/n8n-api-manager/scripts/n8n_client.py executions [workflow_id]
python /home/claude/n8n-api-manager/scripts/n8n_client.py audit
python /home/claude/n8n-api-manager/scripts/audit_workflow.py <id>
python /home/claude/n8n-api-manager/scripts/audit_workflow.py --all
python /home/claude/n8n-api-manager/scripts/workflow_diff.py current.json edited.json
```

### b) Python embebido (para crear/editar workflows con lógica)

```python
import sys
sys.path.insert(0, "/home/claude/n8n-api-manager/scripts")

from n8n_client import N8nClient
from workflow_builder import build_skeleton, make_node, add_node, connect, validate

client = N8nClient()

wf = build_skeleton(
    name="Notificador de leads",
    trigger="webhook",
    description="Recibe POST con datos del lead y los manda a Slack.",
)
add_node(wf, make_node(
    name="Format Message",
    node_type="n8n-nodes-base.set",
    type_version=3.4,
    parameters={...},
    position=(280, 0),
))
connect(wf, "Webhook Trigger", "Format Message")

errs = validate(wf)
assert not errs, errs

created = client.create_workflow(wf)
print("Creado:", created["id"])
```

## Auditoría: cómo presentar resultados

`audit_workflow.py` devuelve hallazgos por workflow con severidad (high / medium / low) y categoría (security / reliability / maintainability / hygiene).

Cuando Claude reporta una auditoría:

1. **Empieza con un resumen ejecutivo de 1-2 líneas** (cuántos workflows, cuántos hallazgos por severidad).
2. **Agrupa por workflow**, en este orden: 🔴 high primero, 🟡 medium, 🟢 low.
3. Por cada hallazgo: **issue, detalle, sugerencia accionable**. Nada de párrafos largos.
4. **Pregunta al final qué quiere el usuario que arreglemos primero.** No empieces a arreglar nada por iniciativa propia.

Reglas que aplica el auditor (en `audit_workflow.py`):

- **🔴 security**: posibles secretos hardcodeados en parámetros (busca patrones `api_key`, `token`, `bearer`, etc. en nodos que no usen el sistema de credenciales).
- **🟡 reliability — manejo de errores**: workflow sin `Error Trigger` ni `settings.errorWorkflow`.
- **🟡 reliability — HTTP frágil**: nodos HTTP Request sin `timeout`, sin `retryOnFail`, sin manejo de error.
- **🟢 hygiene**: nodos huérfanos (no conectados ni triggers).
- **🟢 maintainability**: nodos sin notas, workflows con >15 nodos.

Si el usuario pide auditoría sin más, ejecuta `audit_workflow.py --all` y luego ofrece profundizar en uno concreto.

## Restricciones de seguridad

Estas reglas son innegociables. Aunque el usuario insista, Claude las respeta:

1. **Nunca imprime ni loggea la API key** ni el contenido de `data` de credenciales.
2. **Nunca crea credenciales con secretos que aparezcan en el chat**. Si el usuario pega una API key, le pide que la introduzca él directamente en la UI de n8n y rehúsa procesarla.
3. **Antes de cualquier `DELETE`, `PUT` o activación/desactivación**, confirma con el usuario en el chat (no basta con confirmación implícita del prompt original).
4. **No borra ejecuciones en masa sin confirmación explícita**.
5. **Si una llamada devuelve `403`, no insiste**: informa al usuario de que la API key no tiene permisos para esa operación.
6. **No intenta usar la API si las env vars no están**: pide al usuario que las configure y se detiene.

## Cuándo NO usar esta skill

- Si el usuario quiere **redactar el prompt** de un agente de n8n (no crear el workflow), usa `prompt-builder-agentes-n8n`.
- Si quiere **explicar conceptos de n8n** sin tocar su servidor, responde con conocimiento general; no llames a la API.

## Flujo canónico para editar un workflow existente

Editar es la operación de más riesgo. Sigue siempre estas 4 fases:

### Fase 1 — Descargar (GET)
```python
current = client.get_workflow(workflow_id)
# o desde CLI:
# python scripts/n8n_client.py download <id> /tmp/current.json
```

### Fase 2 — Editar en memoria
Trabaja sobre una **copia** del JSON, nunca sobre el resultado de `get_workflow`
directamente, para preservar el original para el diff.

```python
import copy
edited = copy.deepcopy(current)
# ... modificaciones (añadir nodos, cambiar parámetros, conectar) ...
```

### Fase 3 — Mostrar diff y pedir confirmación
```python
from workflow_diff import diff_workflows, render_diff
print(render_diff(diff_workflows(current, edited)))
```
Claude muestra el diff al usuario en el chat y **espera confirmación explícita**
antes de la fase 4.

### Fase 4 — Aplicar (PUT)
```python
client.update_workflow(workflow_id, edited)
```

> Si el workflow estaba **activo** antes del PUT, n8n conserva el estado tras
> actualizarlo. Aun así, después de cambios grandes conviene revisar la próxima
> ejecución en `/executions`.

## Referencias detalladas

- `references/api_endpoints.md` — endpoints, body shapes, paginación.
- `references/node_catalog.md` — tipos de nodos, `typeVersion`, ejemplos.
- `references/troubleshooting.md` — errores `400/401/403/404/429` y diagnóstico.

Léelos cuando vayas a:
- Construir un nodo cuya estructura no conoces (`node_catalog.md`).
- Diagnosticar un error de API (`troubleshooting.md`).
- Decidir qué endpoint usar (`api_endpoints.md`).

## Ejemplo de interacción completa

> **Usuario**: "Audita mi flujo de leads y dime qué mejorar"

Claude:
1. `python scripts/n8n_client.py list` (para localizar el workflow por nombre).
2. Encuentra "Lead Capture" id=`xY7…`.
3. `python scripts/audit_workflow.py xY7…`
4. Presenta el reporte en formato resumido, agrupado por severidad.
5. Pregunta: *"Hay un 🔴 secreto hardcoded en el nodo HTTP y dos HTTP sin timeout. ¿Quieres que te prepare un PUT con las correcciones para revisarlo antes de aplicarlo?"*

> **Usuario**: "Sí, prepáralo pero no lo apliques todavía."

Claude:
1. `GET /workflows/xY7…` para obtener el JSON completo.
2. Modifica en memoria: mueve secretos a un placeholder de credencial, añade `options.timeout=10000`, `retryOnFail=true`.
3. Muestra el diff (nodos cambiados) en el chat.
4. Espera confirmación antes de `PUT`.