# Referencia API n8n (v1)

Resumen práctico de los endpoints que la skill utiliza. Para el detalle completo
consulta `https://docs.n8n.io/api/api-reference/`.

## Autenticación

Todas las llamadas requieren la cabecera:

```
X-N8N-API-KEY: <tu_api_key>
```

La key se genera en n8n: **Settings → n8n API → Create API Key**.

**Base URL**: `https://<tu-dominio>/api/v1`

## Workflows

| Método  | Endpoint                          | Descripción |
|---------|-----------------------------------|-------------|
| GET     | `/workflows`                      | Listar workflows. Filtros: `active`, `tags`, `name`, `limit`, `cursor`, `projectId`. |
| GET     | `/workflows/{id}`                 | Obtener workflow completo (con `nodes`, `connections`, `settings`). |
| POST    | `/workflows`                      | Crear workflow nuevo. |
| PUT     | `/workflows/{id}`                 | Reemplazar workflow completo. |
| DELETE  | `/workflows/{id}`                 | Borrar workflow. |
| POST    | `/workflows/{id}/activate`        | Activar workflow. |
| POST    | `/workflows/{id}/deactivate`      | Desactivar workflow. |
| GET     | `/workflows/{id}/tags`            | Listar tags del workflow. |
| PUT     | `/workflows/{id}/tags`            | Reemplazar tags (body: `[{"id": "..."}]`). |
| PUT     | `/workflows/{id}/transfer`        | Transferir a otro proyecto. |

### Campos prohibidos en POST/PUT

n8n rechaza estos campos en `create`/`update`:

```
id, active, createdAt, updatedAt, versionId, tags,
triggerCount, shared, pinData, meta, isArchived, homeProject
```

- Para activar/desactivar usa los endpoints específicos.
- Las tags se asignan con `PUT /workflows/{id}/tags`.

### Esqueleto mínimo para crear un workflow

```json
{
  "name": "Mi Workflow",
  "nodes": [
    {
      "id": "uuid-v4",
      "name": "Manual Trigger",
      "type": "n8n-nodes-base.manualTrigger",
      "typeVersion": 1,
      "position": [0, 0],
      "parameters": {}
    }
  ],
  "connections": {},
  "settings": {
    "executionOrder": "v1"
  }
}
```

## Executions

| Método  | Endpoint                     | Descripción |
|---------|------------------------------|-------------|
| GET     | `/executions`                | Listar ejecuciones. Filtros: `workflowId`, `status` (`success`/`error`/`waiting`), `includeData`, `limit`, `cursor`. |
| GET     | `/executions/{id}`           | Obtener una ejecución. Con `?includeData=true` devuelve los datos por nodo. |
| DELETE  | `/executions/{id}`           | Borrar ejecución. |

> n8n **no** expone un endpoint público para *disparar* ejecuciones directamente
> sobre un workflow. Para lanzar workflows desde fuera usa un **Webhook trigger**
> o el **n8n CLI**. La skill respeta esta limitación.

## Credentials

| Método  | Endpoint                                  | Descripción |
|---------|-------------------------------------------|-------------|
| POST    | `/credentials`                            | Crear credencial. Body: `{name, type, data}`. |
| DELETE  | `/credentials/{id}`                       | Borrar credencial. |
| GET     | `/credentials/schema/{credentialTypeName}`| Obtener el esquema de un tipo de credencial. |

> Por seguridad, la API **no permite leer** los secretos de las credenciales ni
> listarlas con sus datos. Sólo crear/borrar/inspeccionar tipos.

## Audit

| Método  | Endpoint  | Descripción |
|---------|-----------|-------------|
| POST    | `/audit`  | Genera un audit de seguridad/operacional. |

Body opcional:
```json
{
  "additionalOptions": {
    "daysAbandonedWorkflow": 90,
    "categories": ["credentials","database","nodes","filesystem","instance"]
  }
}
```

## Tags, Variables, Users, Source Control

- `/tags` (CRUD)
- `/variables` (CRUD)
- `/users` (admin only)
- `/source-control/pull`, `/source-control/push` (Enterprise)

## Paginación

Endpoints de listado devuelven:

```json
{
  "data": [ ... ],
  "nextCursor": "ABC123..."
}
```

Para siguiente página: `?cursor=ABC123...`.

## Códigos de error frecuentes

| Código | Causa habitual |
|--------|----------------|
| 401    | API key ausente o inválida. |
| 403    | Permisos insuficientes (la API key es de un usuario sin acceso). |
| 404    | Workflow / ejecución no existe. |
| 400    | Body inválido (campo prohibido, falta `name`, JSON malformado). |
| 429    | Rate limit. Espera y reintenta. |