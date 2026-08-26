#!/usr/bin/env python3
"""
n8n Workflow Auditor
====================
Audita uno o varios workflows de n8n y devuelve un análisis estructurado con
hallazgos y propuestas de mejora.

Uso:
    python audit_workflow.py <workflow_id>        # auditar uno
    python audit_workflow.py --all                # auditar todos
    python audit_workflow.py --all --inactive     # incluye inactivos
    python audit_workflow.py <workflow_id> --json # salida solo JSON

El análisis NO modifica el workflow; solo lee y devuelve recomendaciones que
Claude puede luego usar para proponer mejoras al usuario.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from typing import Any

# permitir importar n8n_client.py del mismo directorio
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from n8n_client import N8nClient, N8nAPIError  # noqa: E402


# --------------------------------------------------------------------------
# Reglas de auditoría
# --------------------------------------------------------------------------
def _node_type_counts(nodes: list[dict]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for n in nodes:
        t = n.get("type", "unknown")
        counts[t] = counts.get(t, 0) + 1
    return counts


def _has_error_handler(workflow: dict) -> bool:
    """¿Tiene Error Trigger o errorWorkflow configurado en settings?"""
    settings = workflow.get("settings") or {}
    if settings.get("errorWorkflow"):
        return True
    for n in workflow.get("nodes", []):
        if n.get("type") == "n8n-nodes-base.errorTrigger":
            return True
    return False


def _disconnected_nodes(workflow: dict) -> list[str]:
    """Nodos que no aparecen ni como origen ni como destino en `connections`."""
    nodes = workflow.get("nodes", [])
    connections = workflow.get("connections", {}) or {}

    referenced: set[str] = set()
    for src, outs in connections.items():
        referenced.add(src)
        # outs es típicamente {"main": [[{"node": "...", ...}, ...], ...]}
        for _output_type, conn_list in (outs or {}).items():
            for branch in (conn_list or []):
                for conn in (branch or []):
                    if isinstance(conn, dict) and conn.get("node"):
                        referenced.add(conn["node"])

    triggers_or_starts = {
        "n8n-nodes-base.manualTrigger",
        "n8n-nodes-base.scheduleTrigger",
        "n8n-nodes-base.webhook",
        "n8n-nodes-base.errorTrigger",
        "n8n-nodes-base.cron",
        "n8n-nodes-base.start",
        "n8n-nodes-base.emailReadImap",
        "n8n-nodes-base.executeWorkflowTrigger",
        "n8n-nodes-langchain.chatTrigger",
    }

    disconnected = []
    for n in nodes:
        name = n.get("name")
        if name in referenced:
            continue
        # Triggers no necesitan estar referenciados como destino
        if n.get("type") in triggers_or_starts:
            continue
        disconnected.append(name)
    return disconnected


def _hardcoded_secrets_risks(nodes: list[dict]) -> list[dict]:
    """Heurística: busca strings que parezcan claves/tokens en parámetros."""
    suspicious_patterns = ["api_key", "apikey", "token", "secret", "password", "bearer "]
    findings: list[dict] = []
    for n in nodes:
        params = n.get("parameters") or {}
        flat = json.dumps(params, ensure_ascii=False).lower()
        for pat in suspicious_patterns:
            if pat in flat and "credentials" not in (n.get("credentials") or {}):
                # Sólo marcamos si NO usa el sistema de credentials de n8n
                findings.append(
                    {
                        "node": n.get("name"),
                        "type": n.get("type"),
                        "pattern": pat,
                        "hint": "Posible secreto en `parameters`. Mueve a Credentials.",
                    }
                )
                break
    return findings


def _missing_node_notes(nodes: list[dict]) -> int:
    """Cuántos nodos NO tienen 'notes' (documentación interna)."""
    return sum(1 for n in nodes if not n.get("notes"))


def _http_request_observations(nodes: list[dict]) -> list[dict]:
    """Observaciones sobre nodos HTTP Request: timeouts, retries, error handling."""
    obs: list[dict] = []
    for n in nodes:
        if n.get("type") != "n8n-nodes-base.httpRequest":
            continue
        params = n.get("parameters") or {}
        options = params.get("options") or {}

        issues: list[str] = []
        if not options.get("timeout"):
            issues.append("Sin timeout configurado (puede colgar el workflow).")
        if n.get("retryOnFail") is not True and not options.get("retry"):
            issues.append("Sin retry configurado (peticiones de red son frágiles).")
        if n.get("continueOnFail") is None and not n.get("onError"):
            issues.append("Sin manejo de error: un fallo aborta todo el flujo.")
        if issues:
            obs.append({"node": n.get("name"), "issues": issues})
    return obs


def _detect_long_chains(workflow: dict, threshold: int = 15) -> bool:
    """Heurística: si el workflow tiene > threshold nodos, sugiere modularizar."""
    return len(workflow.get("nodes", [])) > threshold


def audit_one(workflow: dict) -> dict:
    """Devuelve un dict con hallazgos para un workflow concreto."""
    nodes = workflow.get("nodes", [])
    findings: list[dict] = []

    if not _has_error_handler(workflow):
        findings.append(
            {
                "severity": "medium",
                "category": "reliability",
                "issue": "Sin manejo de errores",
                "detail": (
                    "El workflow no tiene un Error Trigger ni `settings.errorWorkflow`. "
                    "Si falla en producción, no avisará a nadie."
                ),
                "suggestion": (
                    "Crear un workflow de errores separado y configurarlo en "
                    "Workflow > Settings > Error Workflow."
                ),
            }
        )

    disc = _disconnected_nodes(workflow)
    if disc:
        findings.append(
            {
                "severity": "low",
                "category": "hygiene",
                "issue": "Nodos desconectados",
                "detail": f"{len(disc)} nodos sin conexiones: {', '.join(disc[:5])}"
                + (" ..." if len(disc) > 5 else ""),
                "suggestion": "Elimina nodos huérfanos o conéctalos al flujo.",
            }
        )

    secrets = _hardcoded_secrets_risks(nodes)
    if secrets:
        findings.append(
            {
                "severity": "high",
                "category": "security",
                "issue": "Posibles secretos hardcodeados",
                "detail": f"{len(secrets)} nodo(s) con parámetros que parecen contener secretos.",
                "items": secrets,
                "suggestion": (
                    "Mueve las credenciales al sistema de Credentials de n8n y "
                    "referéncialas desde el nodo (campo `credentials`)."
                ),
            }
        )

    http_obs = _http_request_observations(nodes)
    if http_obs:
        findings.append(
            {
                "severity": "medium",
                "category": "reliability",
                "issue": "Nodos HTTP Request sin endurecer",
                "detail": f"{len(http_obs)} nodo(s) HTTP Request sin timeout/retry/error-handling.",
                "items": http_obs,
                "suggestion": (
                    "Para cada HTTP Request: define `Options > Timeout`, activa "
                    "`Retry On Fail` con 2-3 reintentos y backoff, y decide "
                    "`On Error` (Continue / Continue (using error output) / Stop)."
                ),
            }
        )

    no_notes = _missing_node_notes(nodes)
    if no_notes and len(nodes) > 5:
        findings.append(
            {
                "severity": "low",
                "category": "maintainability",
                "issue": "Nodos sin notas",
                "detail": f"{no_notes}/{len(nodes)} nodos sin notas internas.",
                "suggestion": (
                    "Añade notas a los nodos clave (negocio/decisión) y Sticky Notes "
                    "explicando el propósito de cada bloque del flujo."
                ),
            }
        )

    if _detect_long_chains(workflow):
        findings.append(
            {
                "severity": "low",
                "category": "maintainability",
                "issue": "Workflow grande",
                "detail": f"{len(nodes)} nodos. Workflows largos son difíciles de mantener.",
                "suggestion": (
                    "Considera extraer fragmentos a sub-workflows usando "
                    "`Execute Sub-workflow`."
                ),
            }
        )

    return {
        "id": workflow.get("id"),
        "name": workflow.get("name"),
        "active": workflow.get("active"),
        "node_count": len(nodes),
        "node_types": _node_type_counts(nodes),
        "findings": findings,
        "findings_summary": {
            "high": sum(1 for f in findings if f["severity"] == "high"),
            "medium": sum(1 for f in findings if f["severity"] == "medium"),
            "low": sum(1 for f in findings if f["severity"] == "low"),
        },
    }


# --------------------------------------------------------------------------
# Renderizado humano
# --------------------------------------------------------------------------
SEV_EMOJI = {"high": "🔴", "medium": "🟡", "low": "🟢"}


def render_text(report: dict) -> str:
    lines: list[str] = []
    lines.append(f"# Workflow: {report['name']}  (id={report['id']})")
    lines.append(
        f"  - {'🟢 ACTIVO' if report['active'] else '⚪ inactivo'}"
        f"  · {report['node_count']} nodos"
    )
    s = report["findings_summary"]
    lines.append(f"  - Hallazgos: 🔴 {s['high']}  🟡 {s['medium']}  🟢 {s['low']}")
    lines.append("")
    if not report["findings"]:
        lines.append("✅ Sin hallazgos. Workflow limpio.")
        return "\n".join(lines)
    for f in report["findings"]:
        emoji = SEV_EMOJI.get(f["severity"], "•")
        lines.append(f"## {emoji} [{f['category']}] {f['issue']}")
        lines.append(f"   {f['detail']}")
        lines.append(f"   💡 {f['suggestion']}")
        lines.append("")
    return "\n".join(lines)


# --------------------------------------------------------------------------
# Entrypoint
# --------------------------------------------------------------------------
def main() -> int:
    parser = argparse.ArgumentParser(description="Audita workflows de n8n.")
    parser.add_argument("workflow_id", nargs="?", help="ID del workflow (o usa --all).")
    parser.add_argument("--all", action="store_true", help="Audita todos los workflows.")
    parser.add_argument(
        "--inactive",
        action="store_true",
        help="Al usar --all, incluye workflows inactivos. Por defecto solo activos.",
    )
    parser.add_argument("--json", action="store_true", help="Salida JSON cruda.")
    args = parser.parse_args()

    try:
        client = N8nClient()
    except ValueError as e:
        print(f"❌ {e}", file=sys.stderr)
        return 2

    reports: list[dict] = []
    try:
        if args.all:
            wfs = client.list_all_workflows(
                active=None if args.inactive else True
            )
            for stub in wfs:
                # `list` ya trae el workflow completo en la API actual,
                # pero por compatibilidad hacemos GET por id si faltan nodes.
                if "nodes" not in stub and stub.get("id"):
                    stub = client.get_workflow(stub["id"])
                reports.append(audit_one(stub))
        elif args.workflow_id:
            wf = client.get_workflow(args.workflow_id)
            reports.append(audit_one(wf))
        else:
            parser.print_help()
            return 1
    except N8nAPIError as e:
        print(f"❌ API error [{e.status_code}]: {e.message}", file=sys.stderr)
        return 3

    if args.json:
        print(json.dumps(reports, indent=2, ensure_ascii=False))
    else:
        for r in reports:
            print(render_text(r))
            print("-" * 70)
        # Resumen global
        total_h = sum(r["findings_summary"]["high"] for r in reports)
        total_m = sum(r["findings_summary"]["medium"] for r in reports)
        total_l = sum(r["findings_summary"]["low"] for r in reports)
        print(
            f"\n🔎 Total: {len(reports)} workflow(s). "
            f"Hallazgos -> 🔴 {total_h}  🟡 {total_m}  🟢 {total_l}"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())