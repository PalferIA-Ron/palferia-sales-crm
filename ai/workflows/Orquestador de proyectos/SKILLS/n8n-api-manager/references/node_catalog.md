# Catálogo de nodos comunes de n8n

Esta es una hoja de referencia con los tipos de nodos más usados y sus
parámetros clave. **No es exhaustiva**: para nodos exóticos consulta la UI de
n8n y copia el JSON desde "Download" en el menú del workflow.

## Triggers

| Nodo | type | Cuándo usar |
|------|------|-------------|
| Manual Trigger | `n8n-nodes-base.manualTrigger` | Ejecución manual desde la UI (pruebas). |
| Schedule Trigger | `n8n-nodes-base.scheduleTrigger` | Ejecutar cada X minutos/horas/días o por cron. |
| Webhook | `n8n-nodes-base.webhook` | Recibir HTTP POST/GET externo. |
| Error Trigger | `n8n-nodes-base.errorTrigger` | Capturar errores de otros workflows. |
| Chat Trigger | `@n8n/n8n-nodes-langchain.chatTrigger` | Interfaz de chat para agentes IA. |
| Execute Sub-workflow Trigger | `n8n-nodes-base.executeWorkflowTrigger` | Hacer reutilizable un workflow como sub-flujo. |
| Form Trigger | `n8n-nodes-base.formTrigger` | Formulario web hosteado por n8n. |

### Ejemplo: Schedule Trigger (cada hora)

```json
{
  "type": "n8n-nodes-base.scheduleTrigger",
  "typeVersion": 1.2,
  "parameters": {
    "rule": {
      "interval": [{"field": "hours", "hoursInterval": 1}]
    }
  }
}
```

### Ejemplo: Webhook

```json
{
  "type": "n8n-nodes-base.webhook",
  "typeVersion": 2,
  "parameters": {
    "httpMethod": "POST",
    "path": "incoming-leads",
    "responseMode": "lastNode",
    "options": {}
  }
}
```

## Core / utilitarios

| Nodo | type | Notas |
|------|------|-------|
| Set / Edit Fields | `n8n-nodes-base.set` (v3.4+) | Definir o modificar campos. |
| IF | `n8n-nodes-base.if` (v2) | Bifurcación true/false. |
| Switch | `n8n-nodes-base.switch` (v3) | Múltiples ramas. |
| Merge | `n8n-nodes-base.merge` (v3) | Unir ramas. |
| Loop / Split In Batches | `n8n-nodes-base.splitInBatches` (v3) | Procesar en lotes. |
| Filter | `n8n-nodes-base.filter` (v2) | Filtrar items. |
| Code | `n8n-nodes-base.code` (v2) | JS/Python custom. |
| HTTP Request | `n8n-nodes-base.httpRequest` (v4.2) | Llamadas REST arbitrarias. |
| Wait | `n8n-nodes-base.wait` (v1.1) | Pausa o espera webhook. |
| Execute Sub-workflow | `n8n-nodes-base.executeWorkflow` (v1.2) | Llamar a otro workflow. |
| Respond to Webhook | `n8n-nodes-base.respondToWebhook` (v1.1) | Devolver respuesta a un Webhook. |

### Ejemplo: HTTP Request endurecido

```json
{
  "type": "n8n-nodes-base.httpRequest",
  "typeVersion": 4.2,
  "parameters": {
    "method": "POST",
    "url": "https://api.ejemplo.com/v1/resource",
    "sendHeaders": true,
    "headerParameters": {
      "parameters": [{"name": "Content-Type", "value": "application/json"}]
    },
    "sendBody": true,
    "specifyBody": "json",
    "jsonBody": "={{ JSON.stringify($json) }}",
    "options": {
      "timeout": 10000,
      "response": {"response": {"fullResponse": false, "neverError": false}}
    }
  },
  "credentials": {
    "httpHeaderAuth": {"id": "1", "name": "Mi API Auth"}
  },
  "retryOnFail": true,
  "maxTries": 3,
  "waitBetweenTries": 2000,
  "onError": "continueRegularOutput"
}
```

## IA / LangChain

| Nodo | type | Notas |
|------|------|-------|
| AI Agent | `@n8n/n8n-nodes-langchain.agent` | Agente con herramientas. |
| Basic LLM Chain | `@n8n/n8n-nodes-langchain.chainLlm` | Llamada simple a LLM. |
| Chat Trigger | `@n8n/n8n-nodes-langchain.chatTrigger` | Trigger conversacional. |
| OpenAI Chat Model | `@n8n/n8n-nodes-langchain.lmChatOpenAi` | Sub-nodo: modelo. |
| Anthropic Chat Model | `@n8n/n8n-nodes-langchain.lmChatAnthropic` | Sub-nodo: modelo. |
| Simple Memory | `@n8n/n8n-nodes-langchain.memoryBufferWindow` | Sub-nodo: memoria. |
| Structured Output Parser | `@n8n/n8n-nodes-langchain.outputParserStructured` | Forzar JSON. |

Los nodos de IA usan **sub-nodos**: se conectan con `ai_languageModel`,
`ai_memory`, `ai_tool`, etc. en lugar de `main`.

### Ejemplo: AI Agent + OpenAI

Estructura conceptual:

```
Chat Trigger ─main─▶ AI Agent
                       ▲ ai_languageModel
                       │
                  OpenAI Chat Model
```

```json
// AI Agent
{
  "type": "@n8n/n8n-nodes-langchain.agent",
  "typeVersion": 2,
  "parameters": {
    "promptType": "auto",
    "options": {"systemMessage": "Eres un asistente útil."}
  }
}

// Conexión hacia el AI Agent desde el modelo:
"OpenAI Chat Model": {
  "ai_languageModel": [
    [{"node": "AI Agent", "type": "ai_languageModel", "index": 0}]
  ]
}
```

## Patrón: Workflow con manejo de errores

Estructura recomendada:

1. **Workflow principal**: lógica de negocio.
2. **Workflow de errores separado**: empieza con `Error Trigger`, envía notificación (Slack/email).
3. En el workflow principal: `Settings → Error Workflow` apunta al de errores.

Además, para nodos críticos:
- `retryOnFail: true` con 2-3 reintentos y `waitBetweenTries` 1000-2000 ms.
- `onError: "continueErrorOutput"` para ramificar el flujo en caso de error y manejarlo localmente.

## Patrón: Modularizar con sub-workflows

Cuando un workflow supera ~15 nodos, extrae fragmentos a sub-workflows:

- Sub-workflow: empieza con `Execute Sub-workflow Trigger`, define `inputSource` y los campos esperados.
- Workflow padre: usa `Execute Sub-workflow` apuntando al ID del sub-workflow.

Ventajas: reutilización, tests aislados, ejecuciones independientes en logs.

## Convenciones para construir workflows desde la API

1. **Cada nodo necesita `id` único** (UUID v4).
2. **Los `name` también deben ser únicos** dentro del workflow.
3. **`position` es `[x, y]`**, normalmente separados ~280 px en X.
4. **`connections` se indexa por `name` del nodo origen**, no por id:
   ```json
   "connections": {
     "Schedule Trigger": {
       "main": [[ {"node": "Set", "type": "main", "index": 0} ]]
     }
   }
   ```
5. **`settings.executionOrder: "v1"`** es lo estándar desde n8n ≥ 1.0.
6. **No incluyas `id`, `active`, `tags`, `createdAt`, `updatedAt`** al crear.

## Cómo descubrir el JSON de un nodo desconocido

Cuando dudes del formato exacto de un nodo (por ejemplo, un Postgres con
columnas específicas):

1. Crea el nodo manualmente en la UI de n8n.
2. Selecciona el nodo → menú **⋯** → **Copy** (copia el JSON al portapapeles).
3. Pégalo aquí; la skill lo usará como plantilla.

Alternativa: exporta el workflow entero (menú workflow → **Download**) y léelo.