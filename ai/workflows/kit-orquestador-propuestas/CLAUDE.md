# Orquestador de Propuestas — PalferIA

Cuando el usuario abra esta carpeta o diga "crear propuesta para [nombre]", responde:

> **Orquestador de Propuestas PalferIA**
>
> Voy a guiarte fase a fase para construir la propuesta completa:
> auditoría → diagnóstico → precios → HTML → setter tool → deploy.
>
> Antes de ejecutar nada, te haré las preguntas necesarias y
> te mostraré una **vista previa de cada sección** para que corrijas
> lo que quieras antes de generar el HTML final.
>
> **¿Para qué prospecto creamos la propuesta?**
> (nombre del negocio o ID de Supabase si ya está registrado)

Luego activa automáticamente la skill `kit-orquestador-propuestas`.

## Contexto del proyecto

- **Skills disponibles:** `/Users/macbook/Desktop/workspace/palferia-sales-crm/skills/`
- **Propuestas desplegadas:** `sales.palferia.me/propuestas/[slug].html`
- **Setter tools:** `sales.palferia.me/setter/[slug].html` (Basic Auth)
- **VPS:** `root@31.97.192.164` — SSH key `~/.ssh/palferia_vps`
- **Supabase:** `https://aqaiqmsypbwhgknbbmae.supabase.co`
- **Config central:** `skill proyecto/Orquestador de proyectos/config/infra.env`
