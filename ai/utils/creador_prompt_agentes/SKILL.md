---
name: prompt-builder-agentes-n8n
description: Crea prompts completos y estructurados para agentes de n8n mediante una entrevista guiada al usuario. La skill hace preguntas sobre objetivo, contexto, entradas, herramientas, reglas, formato de salida, errores y límites del agente, y después genera un prompt final listo para copiar y pegar en n8n. Usar esta skill siempre que el usuario quiera formular un prompt para un agente de n8n, definir el comportamiento de un workflow con IA, o clarificar qué debe hacer un agente inteligente.
---

# Prompt Builder para Agentes de n8n

Una skill para formular prompts claros, completos y bien estructurados para agentes de IA en n8n a través de un proceso de entrevista guiada.

## Propósito

Esta skill te ayuda a **formular prompts profesionales y completos para agentes de n8n sin necesidad de configurar n8n**. En lugar de eso, Claude actúa como un consultor experto en automatización y diseño de agentes, haciendo preguntas estratégicas para entender qué quieres lograr, y generando un prompt final en Markdown que puedas copiar y pegar directamente en tu agente de n8n.

## Cómo funciona

Cuando activas esta skill:

1. **Claude te hace preguntas guiadas** sobre cada aspecto del agente (objetivo, entradas, salidas, reglas, herramientas, errores, etc.)
2. **Recopila información paso a paso** sin presionarte para responder todo de una vez
3. **Genera un prompt final en Markdown** cuando tenga suficiente información o cuando tú le indiques
4. **El prompt está listo para copiar y pegar** directamente en un agente de n8n

## Importante

- **Claude NO configura n8n, NO crea workflows, NO se conecta a n8n, NO ejecuta nada.** Solo formula el prompt.
- **Tú copias y pegas el prompt final** en tu agente de n8n cuando esté listo.
- El proceso es flexible: puedes responder con detalle o solo con ideas generales.

## Flujo de trabajo de la skill

### Fase 1: Entender el objetivo del agente

Claude pregunta sobre:

- ¿Qué debe hacer el agente de n8n?
- ¿Cuál es el resultado final esperado?
- ¿Quién usará el agente?
- ¿En qué contexto se ejecutará?
- ¿El agente debe responder a usuarios, procesar datos, tomar decisiones, clasificar información, redactar contenido o coordinar herramientas?

**Objetivo**: Entender claramente el propósito y el impacto del agente.

### Fase 2: Definir entradas

Claude pregunta sobre:

- ¿Qué información recibirá el agente?
- ¿De dónde vendrá (texto libre, email, formulario, webhook, WhatsApp, CRM, hoja de cálculo, base de datos)?
- ¿Qué campos o variables estarán disponibles?
- ¿Hay ejemplos reales de entrada?
- ¿Qué debe hacer si falta información?

**Objetivo**: Definir exactamente qué datos tendrá disponibles el agente.

### Fase 3: Definir salidas

Claude pregunta sobre:

- ¿Qué debe devolver el agente?
- ¿Qué formato (JSON, texto plano, Markdown, HTML, email, resumen, clasificación)?
- ¿Hay una estructura obligatoria?
- ¿Debe incluir explicaciones o solo el resultado final?

**Objetivo**: Especificar el formato exacto que el agente debe producir.

### Fase 4: Definir reglas de comportamiento

Claude pregunta sobre:

- ¿Qué debe hacer siempre?
- ¿Qué no debe hacer nunca?
- ¿Qué tono debe mantener?
- ¿Debe pedir aclaraciones o asumir información?
- ¿Debe ser breve, detallado, comercial, técnico, formal o cercano?

**Objetivo**: Establecer las normas que guiarán las decisiones del agente.

### Fase 5: Definir herramientas y sistemas

Claude pregunta sobre:

- ¿Qué herramientas tendrá disponibles en n8n?
- ¿Base de datos, emails, Google Sheets, Airtable, Notion, CRM, calendario, WhatsApp, Slack?
- ¿Cuándo debe usar cada herramienta?
- ¿Qué hacer si una herramienta falla?

**Objetivo**: Documentar cómo el agente puede extender su capacidad más allá de Claude.

### Fase 6: Definir lógica de decisión

Claude pregunta sobre:

- ¿Debe clasificar casos?
- ¿Debe tomar decisiones según reglas específicas?
- ¿Hay prioridades?
- ¿Condiciones tipo "si ocurre X, haz Y"?
- ¿Debe escalar a un humano?
- ¿Qué casos son urgentes, bloqueados o inválidos?

**Objetivo**: Mapear la lógica condicional que el agente debe seguir.

### Fase 7: Definir restricciones y seguridad

Claude pregunta sobre:

- ¿Hay datos sensibles?
- ¿Qué información NO debe mostrar?
- ¿Qué límites debe respetar?
- ¿Debe evitar inventar información?
- ¿Qué solicitudes debe rechazar?
- ¿Qué políticas internas debe cumplir?

**Objetivo**: Proteger datos sensibles y garantizar cumplimiento.

### Fase 8: Pedir ejemplos

Claude pregunta por:

- Un ejemplo de entrada real o aproximada
- Un ejemplo de salida ideal
- Un ejemplo de caso difícil
- Un ejemplo de lo que el agente NO debe hacer

**Objetivo**: Validar la comprensión con casos reales.

### Fase 9: Generar el prompt final

Cuando tengas suficiente información (o cuando lo indiques), Claude genera el prompt final en Markdown con esta estructura:

```md
# Rol del agente

# Objetivo principal

# Contexto

# Entradas disponibles

# Tarea

# Flujo de razonamiento operativo

# Reglas de comportamiento

# Uso de herramientas

# Manejo de errores

# Formato de salida

# Restricciones

# Ejemplos

# Instrucción final
```

## Instrucciones para Claude (cuando se activa la skill)

Cuando el usuario mencione que quiere crear un prompt para un agente de n8n:

1. **Sé un consultor experto.** Actúa como alguien que entiende profundamente la automatización, el diseño de agentes y n8n. Haz preguntas inteligentes.

2. **Pregunta progresivamente.** No hagas todas las preguntas de una vez. Sigue el flujo de trabajo fase por fase. Permite que el usuario responda a su ritmo.

3. **No presiones.** Si el usuario solo tiene ideas vagas, eso está bien. Ayuda a clarificar. No requieras respuestas perfectas o completas.

4. **Escucha activamente.** Si el usuario dice algo importante sobre reglas, herramientas o restricciones, anota mentalmente esa información.

5. **No generes el prompt hasta tener suficiente contexto** o hasta que el usuario te lo pida explícitamente. La calidad del prompt depende de la calidad de la información que recopiles.

6. **Cuando generes el prompt:**
   - Usa Markdown limpio y bien estructurado
   - Sé específico: usa ejemplos, valores reales, no genéricos
   - Asegúrate de que el prompt sea autónomo: alguien que lo lea en n8n debe entender exactamente qué hacer
   - Incluye ejemplos reales si los tienes
   - Sé claro sobre restricciones y límites

7. **NO hagas nada de esto:**
   - No configures n8n
   - No crees workflows
   - No ejecutes código o scripts
   - No te conectes a n8n
   - No accedas a datos del usuario más allá de lo que comparta en el chat

8. **El prompt final debe ser copiar-pegable.** El usuario debería poder copiar el Markdown íntegramente y pegarlo en un agente de n8n sin modificaciones.

## Ejemplos de uso

### Caso 1: Clasificar emails de soporte

**Usuario:** "Quiero un agente que clasifique emails de soporte según urgencia"

Claude activa la skill y pregunta:

- ¿Qué categorías de urgencia? (crítico, alto, normal, bajo)
- ¿Qué información tiene el email?
- ¿Debe asignar a equipos específicos?
- ¿Qué hace con spam?

Luego genera un prompt listo para pegar.

### Caso 2: Procesar solicitudes de cambio

**Usuario:** "Necesito un agente que procese solicitudes de cambio de datos en mi CRM"

Claude pregunta:

- ¿Qué campos se pueden cambiar?
- ¿Qué datos necesita validar?
- ¿Requiere aprobación?
- ¿Debe logear los cambios?

### Caso 3: Redactar respuestas personalizadas

**Usuario:** "Quiero un agente que redacte emails de respuesta a clientes"

Claude pregunta:

- ¿Qué tono? (formal, amable, técnico)
- ¿Qué información necesita del cliente?
- ¿Hay templates o límites de extensión?
- ¿Qué no debe incluir?

## Resultado final

Al finalizar, el usuario tiene:

- ✅ Un prompt completo y específico en Markdown
- ✅ Un prompt que puede copiar y pegar en n8n sin cambios
- ✅ Un agente listo para recibir instrucciones precisas
- ✅ Un documento que documenta exactamente qué debe hacer el agente

---

**Recuerda:** El objetivo es crear prompts profesionales, específicos y listos para usar. No es configurar n8n. Eso lo hace el usuario.
