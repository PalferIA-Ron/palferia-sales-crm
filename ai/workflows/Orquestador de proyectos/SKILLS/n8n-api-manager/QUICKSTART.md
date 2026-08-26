# Quickstart — n8n API Manager

Tres pasos para empezar a operar tu n8n desde Claude.

## Paso 1 — Generar la API key en n8n

1. Entra a tu n8n: `https://n8n.srv1267531.hstgr.cloud`
2. **Settings → n8n API → Create an API key**
3. Dale un nombre descriptivo (p.ej. `claude-skill`) y guarda la key — solo se muestra una vez.

## Paso 2 — Exportar las variables de entorno

En el entorno donde Claude ejecuta los scripts (Claude Code, terminal local, etc.):

```bash
export N8N_API_URL="https://n8n.srv1267531.hstgr.cloud"
export N8N_API_KEY="pega_aquí_tu_api_key"
```

Para que persistan entre sesiones, añádelas a tu `~/.bashrc` o `~/.zshrc`.

> ⚠️ Nunca subas tu `N8N_API_KEY` a git ni la pegues en el chat con Claude.
> La skill la lee directamente del entorno y nunca te la pedirá si está definida.

## Paso 3 — Verificar conexión

```bash
python /home/claude/n8n-api-manager/scripts/n8n_client.py ping
```

Si todo va bien, verás un JSON con tu primer workflow (o `"data": []` si tu servidor está vacío). Si falla:

- **`Falta N8N_API_URL`** → las variables no están exportadas en esta shell.
- **`401 Unauthorized`** → la API key es incorrecta o fue revocada.
- **`Error de conexión`** → la URL es incorrecta o el servidor no responde.

## Las 4 cosas que puedes pedirle a Claude desde el minuto 0

### 📋 Listar y explorar
> "Lista mis workflows activos."
> 
> "Muéstrame el workflow llamado X."

Claude ejecuta `list` / `get`.

### 🔍 Auditar
> "Audita todos mis workflows y dime qué mejorar."
> 
> "Revisa solo el flujo de leads."

Claude ejecuta `audit_workflow.py` y presenta hallazgos por severidad.

### ✏️ Editar
> "En el workflow X, añade un timeout de 10s a todos los HTTP Request."
> 
> "Quita el nodo Y del workflow Z."

Claude hace `get → editar → diff → confirmación → PUT`. Verás los cambios antes de aplicarlos.

### 🆕 Crear
> "Crea un workflow que reciba un webhook con un lead y lo mande a Slack."

Claude te hace 2-4 preguntas mínimas, construye el JSON con `workflow_builder.py`, lo valida y lo crea **inactivo** para que lo revises en la UI antes de activarlo.

## Atajos útiles

| Quieres... | Pídele a Claude |
|---|---|
| Ver cuántas ejecuciones han fallado hoy | "Cuántas ejecuciones con error tengo" |
| Backup local de un workflow | "Descárgame el workflow X a un archivo" |
| Comparar dos versiones | "Compara la versión actual con esta editada" |
| Audit nativo de n8n (no el mío) | "Lánzame el audit oficial de n8n" |
| Diagnosticar un fallo | "Por qué falla el workflow X últimamente" |

## Cosas que NO funcionarán (limitaciones reales)

- **Disparar ejecuciones desde la API** — n8n no expone ese endpoint. Para lanzar un workflow desde fuera, ese workflow debe empezar con un `Webhook trigger`.
- **Leer secretos de credenciales** — la API nunca devuelve `data` de credenciales por seguridad. Sólo puedes crear/borrar.
- **Bulk delete de workflows** — Claude pedirá confirmación por cada uno. Es intencionado.
- **Editar workflows activos sin avisar** — siempre verás un diff y confirmarás antes del PUT.