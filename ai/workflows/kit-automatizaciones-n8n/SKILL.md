---
name: automatizaciones-n8n
description: Crea workflows de automatización profesionales en n8n. Conecta con tu instancia n8n via API o genera JSON importable. Busca entre 2.700+ templates probados.
version: 1.0.0
author: PalferIA
---

# Automatizaciones n8n

Diseña e implementa workflows de automatización para n8n, conectando directamente a una instancia o generando JSON importable.

## Conexión con n8n (opcional pero recomendado)

Si el usuario quiere conectar su n8n:
1. Pedir URL de la instancia (ej: `https://mi-n8n.dominio.com` o `http://localhost:5678`)
2. Pedir API key (Settings → API → Create API Key en n8n)
3. Guardar en `.mcp.json` local del proyecto

Si no quiere conectar: generar workflows como JSON importable igualmente.

## Verificar Node.js antes de instalar herramientas

```bash
node --version 2>/dev/null && echo "Node.js OK" || echo "NO_NODE"
```

Si no tiene Node.js: informar que es necesario para conexión directa, ofrecer continuar con JSON igualmente.

## Flujo de diseño de workflow

### 1. Entender la automatización
Preguntar:
- ¿Qué dispara el workflow? (webhook, schedule, evento, manual)
- ¿Qué datos entran y de dónde?
- ¿Qué transformaciones o lógica se aplica?
- ¿A dónde van los datos o qué acción se ejecuta al final?
- ¿Hay casos de error que manejar?

### 2. Diseñar la arquitectura
- Dibujar el flujo nodo a nodo antes de implementar
- Identificar los nodos n8n necesarios (Webhook, HTTP Request, If, Set, Code, Gmail, Slack, etc.)
- Detectar si se necesitan credenciales externas

### 3. Implementar

**Con n8n conectado via API:**
- Crear el workflow directamente en la instancia
- Verificar que los nodos están correctamente configurados
- Activar el workflow si el usuario lo pide

**Sin conexión:**
- Generar el JSON completo del workflow siguiendo el schema de n8n
- El JSON debe ser importable directamente desde n8n UI

### 4. Documentar
- Explicar qué hace cada nodo
- Indicar qué credenciales hay que configurar
- Dar instrucciones de prueba

## Patrones de workflow comunes

- **Webhook → Procesar → Notificar**: recibir datos externos, transformar, enviar a Slack/email
- **Schedule → Obtener datos → Guardar**: cron jobs para reportes automáticos
- **Formulario → CRM → Email**: automatizar captación de leads
- **API → Filtrar → Múltiples destinos**: distribuir datos a varios sistemas

## Reglas

- Siempre validar que el JSON generado es sintácticamente correcto
- Explicar claramente qué credenciales necesita el usuario configurar
- Si el workflow es complejo, dividirlo en partes y confirmar cada parte antes de continuar
- Usar los nodos nativos de n8n siempre que existan antes de recurrir a HTTP Request genérico
