# Orquestador de Proyectos de Automatización

Este proyecto convierte unas notas de reunión con un cliente en un proyecto de automatización completo: brief técnico, arquitectura, prompts de agentes, workflows en n8n e informe final para el cliente.

## Comportamiento al iniciar

Cuando el usuario abra esta carpeta y escriba cualquier cosa (incluido "hola", "empezar", "tengo las notas"), responde con este mensaje de bienvenida:

> **Orquestador de Proyectos activado**
>
> Voy a convertir las notas de tu reunión en un proyecto de automatización completo.
>
> El proceso sigue 9 fases automáticas:
> análisis → brief técnico → arquitectura → naming de workflows → prompts de agentes → creación en n8n → auditoría → mejoras → informe PDF para el cliente.
>
> **Pega aquí las notas de la reunión y empezamos por la Fase 1.**

Después de recibir las notas, ejecuta el proceso completo siguiendo el documento `Orquestador de proyectos.md`.

## Skills disponibles

Este orquestador usa tres skills internas según la fase:

- **mantenimiento-ia** — Fase 2: recopilar y estructurar la información del proyecto.
- **prompt-builder-agentes-n8n** — Fase 5: crear los prompts de producción para los agentes de texto.
- **n8n-api-manager** — Fases 6, 7 y 8: crear, auditar y mejorar los workflows en n8n.

Las skills están en la carpeta `SKILLS/`. Úsalas en el momento indicado por el loop, no antes.

## Reglas de ejecución

- Sigue las fases en orden. No te saltes ninguna.
- Máximo 2 iteraciones de auditoría y mejora (Fase 8). Nunca más.
- Si falta información del cliente, haz supuestos razonables, márcalos como "supuesto" y continúa.
- Si falta una credencial crítica, documéntala como pendiente y detén la ejecución.
- No repitas llamadas idénticas a una skill si ya obtuvo respuesta válida.
- Al entregar el informe final (Fase 9), detén el proceso completamente.

## Lo que genera al finalizar

- Brief técnico estructurado del proyecto.
- Arquitectura de automatización con flujo, componentes y datos.
- Nombres de workflows versionados listos para n8n.
- Prompts de producción para los agentes de texto.
- Workflows creados en el servidor n8n.
- Resultado de auditoría de cada workflow.
- **Propuesta HTML para el cliente** — desplegada en `sales.palferia.me/propuestas/[slug].html`
- **Setter tool HTML interno** — desplegado en `sales.palferia.me/setter/[slug].html` (contraseña: setter/Palferia2026), con 9 secciones: resumen reunión, auditoría dummies, ROI + calculadora, plan & calculadora descuento, objeciones, tips negociación, entregables, mapa proceso, notas Gemini.

## Referencia completa

Todo el detalle de cada fase está en `Orquestador de proyectos.md`.
