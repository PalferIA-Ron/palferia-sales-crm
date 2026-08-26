#!/usr/bin/env python3
"""
Workflow Skeleton Builder
=========================
Construye el JSON mínimo de un workflow listo para POST /workflows.

NO es un generador mágico. Es un helper para crear esqueletos consistentes que
Claude puede luego personalizar nodo por nodo.

Uso típico desde Claude:
    1) Llamar a build_skeleton(name="...", trigger="webhook"|"schedule"|"manual"|"chat")
    2) Ir añadiendo nodos con add_node(...) y conectándolos con connect(...)
    3) Validar con validate(workflow_json) → lista de errores
    4) Enviar con n8n_client.create_workflow(workflow_json)

Reglas de los IDs:
    - Cada nodo necesita un `id` único (UUID) y un `name` único en el workflow.
    - Las `connections` se indexan por `name` del nodo origen.
"""
from __future__ import annotations

import json
import sys
import uuid
from typing import Any


# --------------------------------------------------------------------------
# Catálogo mínimo de triggers y nodos comunes
# --------------------------------------------------------------------------
TRIGGERS = {
    "manual": {
        "type": "n8n-nodes-base.manualTrigger",
        "typeVersion": 1,
        "parameters": {},
    },
    "webhook": {
        "type": "n8n-nodes-base.webhook",
        "typeVersion": 2,
        "parameters": {
            "httpMethod": "POST",
            "path": "my-webhook",
            "responseMode": "onReceived",
            "options": {},
        },
    },
    "schedule": {
        "type": "n8n-nodes-base.scheduleTrigger",
        "typeVersion": 1.2,
        "parameters": {
            "rule": {
                "interval": [{"field": "hours", "hoursInterval": 1}]
            }
        },
    },
    "chat": {
        "type": "@n8n/n8n-nodes-langchain.chatTrigger",
        "typeVersion": 1.1,
        "parameters": {"options": {}},
    },
    "error": {
        "type": "n8n-nodes-base.errorTrigger",
        "typeVersion": 1,
        "parameters": {},
    },
}


def _new_id() -> str:
    return str(uuid.uuid4())


def make_node(
    name: str,
    node_type: str,
    parameters: dict | None = None,
    type_version: float | int = 1,
    position: tuple[int, int] = (0, 0),
    credentials: dict | None = None,
    notes: str | None = None,
    on_error: str | None = None,  # "stopWorkflow" | "continueRegularOutput" | "continueErrorOutput"
    retry_on_fail: bool = False,
) -> dict:
    """Crea un nodo válido para n8n."""
    node: dict[str, Any] = {
        "id": _new_id(),
        "name": name,
        "type": node_type,
        "typeVersion": type_version,
        "position": [position[0], position[1]],
        "parameters": parameters or {},
    }
    if credentials:
        node["credentials"] = credentials
    if notes:
        node["notes"] = notes
    if on_error:
        node["onError"] = on_error
    if retry_on_fail:
        node["retryOnFail"] = True
        node["maxTries"] = 3
        node["waitBetweenTries"] = 1000
    return node


def build_skeleton(
    name: str,
    trigger: str = "manual",
    description: str | None = None,
    error_workflow_id: str | None = None,
) -> dict:
    """Genera un workflow vacío con un trigger inicial.

    Devuelve el dict listo para client.create_workflow(...).
    """
    if trigger not in TRIGGERS:
        raise ValueError(f"Trigger desconocido: {trigger}. Usa: {list(TRIGGERS)}")
    t = TRIGGERS[trigger]
    trigger_node = make_node(
        name=trigger.capitalize() + " Trigger",
        node_type=t["type"],
        parameters=t["parameters"],
        type_version=t["typeVersion"],
        position=(0, 0),
        notes=description,
    )

    workflow: dict[str, Any] = {
        "name": name,
        "nodes": [trigger_node],
        "connections": {},
        "settings": {
            "executionOrder": "v1",
            "saveManualExecutions": True,
            "saveDataErrorExecution": "all",
            "saveDataSuccessExecution": "all",
        },
    }
    if error_workflow_id:
        workflow["settings"]["errorWorkflow"] = error_workflow_id
    return workflow


def add_node(workflow: dict, node: dict) -> dict:
    """Añade un nodo al workflow. Asegura unicidad de name e id."""
    names = {n["name"] for n in workflow["nodes"]}
    if node["name"] in names:
        raise ValueError(f"Ya existe un nodo llamado {node['name']!r}")
    workflow["nodes"].append(node)
    return node


def connect(
    workflow: dict,
    from_node: str,
    to_node: str,
    from_output: str = "main",
    from_index: int = 0,
    to_index: int = 0,
) -> None:
    """Conecta from_node[from_output][from_index] -> to_node entrada to_index."""
    names = {n["name"] for n in workflow["nodes"]}
    if from_node not in names:
        raise ValueError(f"Nodo origen no existe: {from_node}")
    if to_node not in names:
        raise ValueError(f"Nodo destino no existe: {to_node}")

    conns = workflow.setdefault("connections", {})
    src = conns.setdefault(from_node, {})
    out_list = src.setdefault(from_output, [])
    while len(out_list) <= from_index:
        out_list.append([])
    out_list[from_index].append(
        {"node": to_node, "type": from_output, "index": to_index}
    )


def validate(workflow: dict) -> list[str]:
    """Valida estructura mínima. Devuelve lista de errores (vacía si ok)."""
    errors: list[str] = []
    if not workflow.get("name"):
        errors.append("Falta 'name'.")
    nodes = workflow.get("nodes")
    if not isinstance(nodes, list) or not nodes:
        errors.append("'nodes' debe ser una lista no vacía.")
        return errors

    ids: set[str] = set()
    names: set[str] = set()
    for i, n in enumerate(nodes):
        for required in ("id", "name", "type", "typeVersion", "position", "parameters"):
            if required not in n:
                errors.append(f"Nodo #{i} ({n.get('name','?')}) falta campo: {required}")
        if n.get("id") in ids:
            errors.append(f"id duplicado: {n['id']}")
        ids.add(n.get("id"))
        if n.get("name") in names:
            errors.append(f"name duplicado: {n['name']}")
        names.add(n.get("name"))

    connections = workflow.get("connections", {})
    for src, outs in connections.items():
        if src not in names:
            errors.append(f"connection con origen inexistente: {src}")
        for _otype, branches in (outs or {}).items():
            for branch in branches or []:
                for c in branch or []:
                    if c.get("node") not in names:
                        errors.append(f"connection apunta a nodo inexistente: {c.get('node')}")
    return errors


# --------------------------------------------------------------------------
# Demo / autocheck
# --------------------------------------------------------------------------
if __name__ == "__main__":
    wf = build_skeleton(
        name="Demo Skeleton",
        trigger="schedule",
        description="Workflow de demostración creado por workflow_builder.py",
    )
    add_node(
        wf,
        make_node(
            name="Set",
            node_type="n8n-nodes-base.set",
            type_version=3.4,
            parameters={
                "assignments": {
                    "assignments": [
                        {"id": "1", "name": "hello", "type": "string", "value": "world"}
                    ]
                }
            },
            position=(280, 0),
        ),
    )
    connect(wf, "Schedule Trigger", "Set")
    errs = validate(wf)
    if errs:
        print("Errores:", file=sys.stderr)
        for e in errs:
            print(" -", e, file=sys.stderr)
        sys.exit(1)
    json.dump(wf, sys.stdout, indent=2, ensure_ascii=False)
    print()