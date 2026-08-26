#!/usr/bin/env python3
"""
Workflow Diff Helper
====================
Compara dos versiones de un workflow (el actual y el editado) y devuelve un
resumen humano de los cambios. Pensado para que Claude lo muestre ANTES de
ejecutar el PUT, para que el usuario pueda aprobar conscientemente.

Uso:
    python workflow_diff.py current.json edited.json

O como librería:
    from workflow_diff import diff_workflows, render_diff
    changes = diff_workflows(current, edited)
    print(render_diff(changes))
"""
from __future__ import annotations

import json
import sys
from typing import Any


def _nodes_by_name(nodes: list[dict]) -> dict[str, dict]:
    return {n.get("name"): n for n in nodes if n.get("name")}


def _node_signature(node: dict) -> dict:
    """Campos relevantes para detectar 'cambio' (ignora `position`)."""
    return {
        "type": node.get("type"),
        "typeVersion": node.get("typeVersion"),
        "parameters": node.get("parameters"),
        "credentials": node.get("credentials"),
        "onError": node.get("onError"),
        "retryOnFail": node.get("retryOnFail"),
        "maxTries": node.get("maxTries"),
        "waitBetweenTries": node.get("waitBetweenTries"),
        "notes": node.get("notes"),
        "disabled": node.get("disabled"),
    }


def diff_workflows(current: dict, edited: dict) -> dict:
    """Devuelve un dict con added/removed/modified de nodos y cambios meta."""
    cur_nodes = _nodes_by_name(current.get("nodes", []))
    new_nodes = _nodes_by_name(edited.get("nodes", []))

    added = [n for name, n in new_nodes.items() if name not in cur_nodes]
    removed = [n for name, n in cur_nodes.items() if name not in new_nodes]

    modified: list[dict] = []
    for name, new in new_nodes.items():
        if name not in cur_nodes:
            continue
        cur = cur_nodes[name]
        if _node_signature(cur) != _node_signature(new):
            changes = []
            sig_cur = _node_signature(cur)
            sig_new = _node_signature(new)
            for k in sig_cur:
                if sig_cur[k] != sig_new[k]:
                    changes.append(
                        {
                            "field": k,
                            "before": sig_cur[k],
                            "after": sig_new[k],
                        }
                    )
            modified.append({"name": name, "changes": changes})

    # Cambios en metadata
    meta_changes = []
    for field in ("name", "settings"):
        if current.get(field) != edited.get(field):
            meta_changes.append(
                {"field": field, "before": current.get(field), "after": edited.get(field)}
            )

    # Cambios en connections (sólo si difieren globalmente; el detalle es ruidoso)
    connections_changed = current.get("connections") != edited.get("connections")

    return {
        "added": added,
        "removed": removed,
        "modified": modified,
        "meta_changes": meta_changes,
        "connections_changed": connections_changed,
    }


def _short(value: Any, max_len: int = 80) -> str:
    s = json.dumps(value, ensure_ascii=False) if not isinstance(value, str) else value
    if s is None:
        return "None"
    if len(s) > max_len:
        return s[:max_len] + "…"
    return s


def render_diff(d: dict) -> str:
    lines: list[str] = []
    total = (
        len(d["added"]) + len(d["removed"]) + len(d["modified"]) + len(d["meta_changes"])
    )
    if total == 0 and not d["connections_changed"]:
        return "Sin cambios detectados."

    lines.append(
        f"📋 Cambios: +{len(d['added'])} nuevos · "
        f"-{len(d['removed'])} eliminados · "
        f"~{len(d['modified'])} modificados · "
        f"{'🔗 conexiones cambiadas' if d['connections_changed'] else '🔗 conexiones intactas'}"
    )

    if d["meta_changes"]:
        lines.append("\n## Metadata")
        for c in d["meta_changes"]:
            lines.append(
                f"  ~ {c['field']}: {_short(c['before'])}  →  {_short(c['after'])}"
            )

    if d["added"]:
        lines.append("\n## ➕ Nodos añadidos")
        for n in d["added"]:
            lines.append(f"  + {n.get('name')} ({n.get('type')} v{n.get('typeVersion')})")

    if d["removed"]:
        lines.append("\n## ➖ Nodos eliminados")
        for n in d["removed"]:
            lines.append(f"  - {n.get('name')} ({n.get('type')})")

    if d["modified"]:
        lines.append("\n## ✏️ Nodos modificados")
        for m in d["modified"]:
            lines.append(f"  ~ {m['name']}:")
            for c in m["changes"]:
                lines.append(
                    f"      · {c['field']}: {_short(c['before'])}  →  {_short(c['after'])}"
                )

    return "\n".join(lines)


def main() -> int:
    if len(sys.argv) != 3:
        print("Uso: python workflow_diff.py <current.json> <edited.json>")
        return 1
    with open(sys.argv[1], encoding="utf-8") as f:
        current = json.load(f)
    with open(sys.argv[2], encoding="utf-8") as f:
        edited = json.load(f)
    d = diff_workflows(current, edited)
    print(render_diff(d))
    return 0


if __name__ == "__main__":
    sys.exit(main())