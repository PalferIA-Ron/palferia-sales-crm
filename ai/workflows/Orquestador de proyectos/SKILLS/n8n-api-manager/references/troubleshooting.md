# Troubleshooting n8n API

## Errores frecuentes y soluciones

### `401 Unauthorized` / "X-N8N-API-KEY header missing"

- La variable `N8N_API_KEY` no está exportada en el entorno donde se ejecuta el script.
- Comprueba: `echo $N8N_API_KEY` (debe mostrar la key, no estar vacía).
- En n8n Cloud: la key se llama igual pero la **Base URL** es `https://<sub>.app.n8n.cloud`.

### `400 Bad Request` al crear/actualizar un workflow

Causas típicas y orden de chequeo:

1. **Campos prohibidos**: enviaste `id`, `active`, `tags`, `createdAt`, `updatedAt`, `versionId`, `triggerCount`, `shared`, `pinData`, `meta`, `isArchived`, `homeProject`. La API los rechaza. La función `_clean_for_create` del cliente los quita.
2. **Falta `name`** o **falta `nodes`** (aunque sea vacío). `nodes` debe ser `[]` como mínimo.
3. **`connections` apunta a un nodo inexistente** (por `name`). Las connections se indexan por `name`, no por `id`.
4. **`typeVersion` desfasado**: por ejemplo `Set v1` ya no existe; usa `3.4`. Si la versión está incorrecta n8n a veces devuelve 400.
5. **IDs duplicados** entre nodos.

### `404 Not Found` al activar un workflow

- Confirma el id con `GET /workflows`. La id en la UI (URL del editor) coincide.
- Si el workflow está archivado (`isArchived: true`) no se puede activar; primero desarchivar desde la UI.

### El workflow se crea pero está vacío en la UI

- Lo más común: olvidaste `connections` (entrega `{}` al menos).
- O las `connections` referencian por `id` en vez de por `name`.

### `429 Too Many Requests`

- Aplica backoff: espera 2-5 segundos y reintenta.
- Si auditas muchos workflows, espacia las llamadas (la skill ya lo hace en `list_all_workflows`).

### `Could not find property option` en un nodo

- Estás usando un `typeVersion` incompatible con los `parameters`. Soluciones:
  1. Crea el nodo en la UI, copia su JSON y úsalo de plantilla.
  2. Sube/baja `typeVersion` consultando `node_catalog.md`.

### Conexiones IA (AI Agent) no funcionan

- Los sub-nodos (modelo, memoria, herramientas) NO se conectan con `main` sino con tipos especiales:
  - Modelo: `ai_languageModel`
  - Memoria: `ai_memory`
  - Herramientas: `ai_tool`
  - Output parser: `ai_outputParser`
- La connection va **desde** el sub-nodo **hacia** el AI Agent (no al revés).

### `executionOrder: "v0" deprecated"`

- Pon siempre `settings.executionOrder = "v1"` en workflows nuevos.

### El workflow funciona en la UI pero falla por API

- Mira `executions/{id}` con `?includeData=true`: el campo `data.resultData.error` tiene el detalle del fallo por nodo.
- Si el workflow tiene **credenciales asignadas por id**, y la id no existe en este servidor (típico al importar de otro entorno), aparecen errores `credential not found`. La API no resuelve credenciales por nombre.

### Comandos de diagnóstico rápido

```bash
# ¿Mi conexión funciona?
python scripts/n8n_client.py ping

# ¿Qué workflows tengo?
python scripts/n8n_client.py list-all

# Ver workflow concreto
python scripts/n8n_client.py get <id>

# Últimas ejecuciones con errores
python scripts/n8n_client.py executions <workflow_id>

# Auditoría completa
python scripts/audit_workflow.py --all
```

## Diferencias self-hosted vs Cloud

| Aspecto | Self-hosted | Cloud |
|---------|-------------|-------|
| Base URL | `https://<tu-host>/api/v1` | `https://<sub>.app.n8n.cloud/api/v1` |
| API key | Settings → n8n API | Igual |
| Endpoint `/audit` | ✅ | ✅ |
| Source control | Sólo Enterprise | Sólo Enterprise |
| Disponibilidad API en plan free | N/A | ❌ (necesita Pro) |