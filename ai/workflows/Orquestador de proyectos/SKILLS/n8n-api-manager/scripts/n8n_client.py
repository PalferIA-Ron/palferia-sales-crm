#!/usr/bin/env python3
"""
n8n API Client
==============
Cliente reutilizable para interactuar con la API REST pública de n8n.

Lee credenciales de variables de entorno:
  - N8N_API_URL  (ej. https://n8n.tudominio.com  -- SIN /api/v1 al final)
  - N8N_API_KEY  (la API key generada en Settings > n8n API)

Uso como librería:
    from n8n_client import N8nClient
    client = N8nClient()
    workflows = client.list_workflows()

Uso como CLI:
    python n8n_client.py list
    python n8n_client.py get <workflow_id>
    python n8n_client.py create <path/to/workflow.json>
    python n8n_client.py update <workflow_id> <path/to/workflow.json>
    python n8n_client.py delete <workflow_id>
    python n8n_client.py activate <workflow_id>
    python n8n_client.py deactivate <workflow_id>
    python n8n_client.py executions [workflow_id]
    python n8n_client.py audit
"""
from __future__ import annotations

import json
import os
import sys
from typing import Any, Optional
from urllib.parse import urljoin

import requests


class N8nAPIError(Exception):
    """Error devuelto por la API de n8n."""

    def __init__(self, status_code: int, message: str, body: Any = None):
        self.status_code = status_code
        self.message = message
        self.body = body
        super().__init__(f"[{status_code}] {message}")


class N8nClient:
    """Cliente para la API REST pública de n8n (/api/v1)."""

    def __init__(
        self,
        base_url: Optional[str] = None,
        api_key: Optional[str] = None,
        timeout: int = 30,
    ):
        base_url = base_url or os.environ.get("N8N_API_URL")
        api_key = api_key or os.environ.get("N8N_API_KEY")

        if not base_url:
            raise ValueError(
                "Falta N8N_API_URL. Define la variable de entorno o pásala al constructor.\n"
                "Ejemplo: export N8N_API_URL=https://n8n.tudominio.com"
            )
        if not api_key:
            raise ValueError(
                "Falta N8N_API_KEY. Genera una en n8n: Settings > n8n API > Create API Key.\n"
                "Luego: export N8N_API_KEY=tu_key_aqui"
            )

        # Normalizamos: queremos que base_url sea https://host/api/v1/
        base_url = base_url.rstrip("/")
        if not base_url.endswith("/api/v1"):
            base_url = base_url + "/api/v1"
        self.base_url = base_url + "/"

        self.session = requests.Session()
        self.session.headers.update(
            {
                "X-N8N-API-KEY": api_key,
                "Accept": "application/json",
                "Content-Type": "application/json",
            }
        )
        self.timeout = timeout

    # ----------------------------------------------------------------------
    # Helpers internos
    # ----------------------------------------------------------------------
    def _request(
        self,
        method: str,
        path: str,
        params: Optional[dict] = None,
        json_body: Optional[dict] = None,
    ) -> Any:
        url = urljoin(self.base_url, path.lstrip("/"))
        try:
            resp = self.session.request(
                method,
                url,
                params=params,
                json=json_body,
                timeout=self.timeout,
            )
        except requests.RequestException as e:
            raise N8nAPIError(0, f"Error de conexión: {e}")

        if resp.status_code == 204:
            return None

        try:
            data = resp.json() if resp.text else None
        except ValueError:
            data = resp.text

        if not resp.ok:
            msg = data.get("message") if isinstance(data, dict) else str(data)
            raise N8nAPIError(resp.status_code, msg or resp.reason, data)

        return data

    # ----------------------------------------------------------------------
    # Workflows
    # ----------------------------------------------------------------------
    def list_workflows(
        self,
        active: Optional[bool] = None,
        tags: Optional[str] = None,
        name: Optional[str] = None,
        limit: int = 100,
        cursor: Optional[str] = None,
    ) -> dict:
        """GET /workflows - Lista workflows con filtros opcionales."""
        params: dict = {"limit": limit}
        if active is not None:
            params["active"] = "true" if active else "false"
        if tags:
            params["tags"] = tags
        if name:
            params["name"] = name
        if cursor:
            params["cursor"] = cursor
        return self._request("GET", "workflows", params=params)

    def list_all_workflows(self, **filters) -> list:
        """Itera paginación y devuelve TODOS los workflows en una lista."""
        out: list = []
        cursor = None
        while True:
            page = self.list_workflows(cursor=cursor, **filters)
            data = page.get("data", page) if isinstance(page, dict) else page
            if isinstance(data, list):
                out.extend(data)
            cursor = page.get("nextCursor") if isinstance(page, dict) else None
            if not cursor:
                break
        return out

    def get_workflow(self, workflow_id: str) -> dict:
        """GET /workflows/{id} - Devuelve un workflow completo (con nodes y connections)."""
        return self._request("GET", f"workflows/{workflow_id}")

    def create_workflow(self, workflow: dict) -> dict:
        """POST /workflows - Crea un workflow nuevo.

        El JSON debe contener al menos: name, nodes, connections, settings.
        No incluyas `active`, `id`, `tags` en la creación; añádelos después.
        """
        # n8n rechaza campos no permitidos en create. Limpiamos lo común.
        clean = self._clean_for_create(workflow)
        return self._request("POST", "workflows", json_body=clean)

    def update_workflow(self, workflow_id: str, workflow: dict) -> dict:
        """PUT /workflows/{id} - Actualiza un workflow existente."""
        clean = self._clean_for_update(workflow)
        return self._request("PUT", f"workflows/{workflow_id}", json_body=clean)

    def delete_workflow(self, workflow_id: str) -> dict:
        """DELETE /workflows/{id} - Borra un workflow."""
        return self._request("DELETE", f"workflows/{workflow_id}")

    def activate_workflow(self, workflow_id: str) -> dict:
        """POST /workflows/{id}/activate"""
        return self._request("POST", f"workflows/{workflow_id}/activate")

    def deactivate_workflow(self, workflow_id: str) -> dict:
        """POST /workflows/{id}/deactivate"""
        return self._request("POST", f"workflows/{workflow_id}/deactivate")

    def get_workflow_tags(self, workflow_id: str) -> list:
        """GET /workflows/{id}/tags"""
        return self._request("GET", f"workflows/{workflow_id}/tags")

    def update_workflow_tags(self, workflow_id: str, tag_ids: list[str]) -> list:
        """PUT /workflows/{id}/tags - Asigna tags (lista de {id}) a un workflow."""
        body = [{"id": tid} for tid in tag_ids]
        return self._request("PUT", f"workflows/{workflow_id}/tags", json_body=body)

    @staticmethod
    def _clean_for_create(workflow: dict) -> dict:
        """Quita campos que la API rechaza en POST /workflows."""
        forbidden = {
            "id", "active", "createdAt", "updatedAt", "versionId",
            "tags", "triggerCount", "shared", "pinData", "meta",
            "isArchived", "homeProject",
        }
        clean = {k: v for k, v in workflow.items() if k not in forbidden}
        # Campos mínimos requeridos
        clean.setdefault("settings", {"executionOrder": "v1"})
        clean.setdefault("connections", {})
        if "name" not in clean:
            raise ValueError("El workflow necesita un campo 'name'.")
        if "nodes" not in clean:
            raise ValueError("El workflow necesita un campo 'nodes' (puede ser []).")
        return clean

    @staticmethod
    def _clean_for_update(workflow: dict) -> dict:
        """Quita campos que la API rechaza en PUT /workflows/{id}."""
        forbidden = {
            "id", "active", "createdAt", "updatedAt", "versionId",
            "tags", "triggerCount", "shared", "pinData", "meta",
            "isArchived", "homeProject",
        }
        return {k: v for k, v in workflow.items() if k not in forbidden}

    # ----------------------------------------------------------------------
    # Executions
    # ----------------------------------------------------------------------
    def list_executions(
        self,
        workflow_id: Optional[str] = None,
        status: Optional[str] = None,  # success | error | waiting
        limit: int = 50,
        cursor: Optional[str] = None,
        include_data: bool = False,
    ) -> dict:
        """GET /executions"""
        params: dict = {"limit": limit, "includeData": "true" if include_data else "false"}
        if workflow_id:
            params["workflowId"] = workflow_id
        if status:
            params["status"] = status
        if cursor:
            params["cursor"] = cursor
        return self._request("GET", "executions", params=params)

    def get_execution(self, execution_id: str, include_data: bool = True) -> dict:
        """GET /executions/{id}"""
        params = {"includeData": "true" if include_data else "false"}
        return self._request("GET", f"executions/{execution_id}", params=params)

    def delete_execution(self, execution_id: str) -> dict:
        """DELETE /executions/{id}"""
        return self._request("DELETE", f"executions/{execution_id}")

    # ----------------------------------------------------------------------
    # Tags
    # ----------------------------------------------------------------------
    def list_tags(self, limit: int = 100) -> dict:
        return self._request("GET", "tags", params={"limit": limit})

    def create_tag(self, name: str) -> dict:
        return self._request("POST", "tags", json_body={"name": name})

    def delete_tag(self, tag_id: str) -> dict:
        return self._request("DELETE", f"tags/{tag_id}")

    # ----------------------------------------------------------------------
    # Credentials (sólo crear / borrar / listar tipos -- nunca leer secretos)
    # ----------------------------------------------------------------------
    def create_credential(self, name: str, cred_type: str, data: dict) -> dict:
        """POST /credentials - Crea una credencial.

        IMPORTANTE: data NUNCA se devuelve por la API en GET; sólo se envía aquí.
        """
        body = {"name": name, "type": cred_type, "data": data}
        return self._request("POST", "credentials", json_body=body)

    def delete_credential(self, credential_id: str) -> dict:
        return self._request("DELETE", f"credentials/{credential_id}")

    def get_credential_schema(self, cred_type: str) -> dict:
        """GET /credentials/schema/{credentialTypeName}"""
        return self._request("GET", f"credentials/schema/{cred_type}")

    # ----------------------------------------------------------------------
    # Audit
    # ----------------------------------------------------------------------
    def generate_audit(
        self,
        categories: Optional[list[str]] = None,
        days_abandoned: int = 90,
    ) -> dict:
        """POST /audit - Genera un audit de seguridad/operacional del instance.

        categories: subset of ["credentials","database","nodes","filesystem","instance"]
        """
        body: dict = {"additionalOptions": {"daysAbandonedWorkflow": days_abandoned}}
        if categories:
            body["additionalOptions"]["categories"] = categories
        return self._request("POST", "audit", json_body=body)

    # ----------------------------------------------------------------------
    # Variables
    # ----------------------------------------------------------------------
    def list_variables(self, limit: int = 100) -> dict:
        return self._request("GET", "variables", params={"limit": limit})

    # ----------------------------------------------------------------------
    # Connectivity check
    # ----------------------------------------------------------------------
    def ping(self) -> dict:
        """Verifica conexión y permisos haciendo una lista pequeña de workflows."""
        return self.list_workflows(limit=1)


# --------------------------------------------------------------------------
# CLI mínima
# --------------------------------------------------------------------------
def _print(obj: Any) -> None:
    print(json.dumps(obj, indent=2, ensure_ascii=False))


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print(__doc__)
        return 1

    try:
        client = N8nClient()
    except ValueError as e:
        print(f"❌ {e}", file=sys.stderr)
        return 2

    cmd = argv[1]
    args = argv[2:]

    try:
        if cmd == "ping":
            _print(client.ping())
        elif cmd == "list":
            _print(client.list_workflows())
        elif cmd == "list-all":
            _print(client.list_all_workflows())
        elif cmd == "get":
            _print(client.get_workflow(args[0]))
        elif cmd == "download":
            # download <id> [path]   --> guarda el workflow a un .json local
            wf = client.get_workflow(args[0])
            path = args[1] if len(args) > 1 else f"workflow_{args[0]}.json"
            with open(path, "w", encoding="utf-8") as f:
                json.dump(wf, f, indent=2, ensure_ascii=False)
            print(f"✅ Guardado en {path}")
        elif cmd == "create":
            with open(args[0], encoding="utf-8") as f:
                wf = json.load(f)
            _print(client.create_workflow(wf))
        elif cmd == "update":
            with open(args[1], encoding="utf-8") as f:
                wf = json.load(f)
            _print(client.update_workflow(args[0], wf))
        elif cmd == "delete":
            _print(client.delete_workflow(args[0]))
        elif cmd == "activate":
            _print(client.activate_workflow(args[0]))
        elif cmd == "deactivate":
            _print(client.deactivate_workflow(args[0]))
        elif cmd == "executions":
            wid = args[0] if args else None
            _print(client.list_executions(workflow_id=wid))
        elif cmd == "execution":
            _print(client.get_execution(args[0]))
        elif cmd == "audit":
            _print(client.generate_audit())
        elif cmd == "tags":
            _print(client.list_tags())
        else:
            print(f"Comando desconocido: {cmd}")
            print(__doc__)
            return 1
    except N8nAPIError as e:
        print(f"❌ API error [{e.status_code}]: {e.message}", file=sys.stderr)
        if e.body:
            print(json.dumps(e.body, indent=2, ensure_ascii=False), file=sys.stderr)
        return 3
    except FileNotFoundError as e:
        print(f"❌ Archivo no encontrado: {e}", file=sys.stderr)
        return 4
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))