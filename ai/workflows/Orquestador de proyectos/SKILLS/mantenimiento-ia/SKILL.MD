---
name: mantenimiento-ia
description: >
  Calcula el precio y el alcance del mantenimiento mensual para soluciones de IA (chatbots, agentes de voz, automatizaciones con n8n, integraciones con CRM, WhatsApp, etc.) a partir de las notas de una reunión con un cliente. También genera contratos de mantenimiento profesionales listos para firmar cuando el cliente acepta la propuesta.

  Activa esta skill SIEMPRE que el usuario mencione: calcular mantenimiento, precio de mantenimiento, cuánto cobrar por mantenimiento, propuesta de mantenimiento, contrato de mantenimiento, notas de cliente IA, presupuesto recurrente, cuota mensual IA, o cuando comparta notas de una reunión con un potencial cliente de soluciones IA. También actívala cuando el usuario diga que un cliente ha aceptado una propuesta y necesita formalizar el contrato.
---

# Skill: Mantenimiento IA — Propuesta y Contrato

Esta skill tiene **dos modos de uso**:

- **MODO A — Propuesta**: El usuario comparte notas de una reunión → se analiza, se hacen preguntas si faltan datos, y se genera la propuesta de mantenimiento con precio justificado.
- **MODO B — Contrato**: El usuario comparte una propuesta aceptada → se genera un contrato profesional listo para firmar.

---

## Cómo detectar el modo

| Señal en el mensaje del usuario | Modo |
|---|---|
| "Te paso las notas de la reunión con..." | MODO A |
| "Aquí mis apuntes del cliente..." | MODO A |
| "¿Cuánto cobro de mantenimiento a...?" | MODO A |
| "El cliente ha aceptado", "quiero el contrato", "formalizar" | MODO B |
| Pega una propuesta previa generada por esta skill | MODO B |

Si no queda claro, pregunta: *"¿Quieres calcular el mantenimiento o generar el contrato para una propuesta ya aceptada?"*

---

## MODO A — Generar Propuesta de Mantenimiento

### Paso 1: Leer el SOP completo

Antes de analizar nada, lee `/mnt/skills/user/mantenimiento-ia/references/sop-mantenimiento.md` para tener todos los criterios de precio en contexto.

### Paso 2: Analizar las notas del usuario

Extrae de las notas toda la información disponible sobre estas variables:

**Variables críticas (sin estas no se puede calcular):**
- [ ] Tipo de solución (chatbot texto, agente de voz, automatización, combinación)
- [ ] Canal(es): WhatsApp, web, Instagram, teléfono, email, otros
- [ ] Complejidad del agente: FAQ / Cualificación / Agendamiento / Operativo / Crítico (niveles 1-5)
- [ ] Integraciones activas (CRM, calendario, Stripe, n8n, etc.)
- [ ] Volumen estimado de conversaciones o llamadas/mes

**Variables importantes (afectan el precio):**
- [ ] Criticidad del sistema para el negocio (¿si falla, pierde ventas/clientes?)
- [ ] Sector del negocio
- [ ] Disponibilidad requerida (horario normal vs. urgencias)
- [ ] Costes de infraestructura propios (¿paga el cliente sus herramientas o van incluidas?)

### Paso 3: Identificar datos que faltan

Si faltan variables críticas, haz las preguntas necesarias **en un solo bloque** (no en mensajes separados). Sé directo y conciso. Ejemplo:

> Para ajustar bien la propuesta, necesito algunos datos que no veo en tus notas:
> 1. ¿Qué volumen de conversaciones/llamadas espera manejar al mes?
> 2. ¿Las herramientas (n8n, OpenAI, etc.) las pagas tú o el cliente?
> 3. ¿Qué tan crítico es el sistema? Si falla unas horas, ¿pierden ventas directas?

### Paso 4: Calcular el mantenimiento

Aplica la fórmula del SOP:

```
Mantenimiento mensual =
  costes fijos herramientas
+ costes variables estimados
+ horas de soporte previstas × 60 €/h
+ horas de optimización × 60 €/h
+ margen de seguridad (15-20%)
+ beneficio
```

Después, compara el resultado con los planes de referencia del SOP y:
- Si el cálculo cae dentro de un plan → recomienda ese plan con el precio de referencia.
- Si la complejidad o criticidad justifica un precio mayor → recomienda el precio más alto y justifícalo explícitamente.

**Regla de precio hacia arriba**: Siempre que haya 3 o más de estos factores, recomienda el plan inmediatamente superior y justifícalo:
- Agente de nivel 4 o 5
- 3 o más integraciones críticas
- Agente de voz incluido
- Sistema crítico para ventas/operaciones
- Varios canales activos

### Paso 5: Generar la propuesta

Presenta la propuesta con esta estructura:

---

**PROPUESTA DE MANTENIMIENTO — [NOMBRE CLIENTE / SECTOR]**

**Solución**: [descripción breve]
**Canales**: [lista]
**Integraciones**: [lista]
**Complejidad**: Nivel [X] — [nombre]
**Volumen estimado**: [X conversaciones/llamadas al mes]

---

**PLAN RECOMENDADO: [NOMBRE PLAN] — [PRECIO]€/mes**

*(Si se recomienda precio superior al de referencia, incluir aquí la justificación en 2-3 líneas)*

**El mantenimiento incluye:**
- [Lista detallada adaptada a este cliente]
- Soporte con tiempo de respuesta de [X] horas en horario laboral [HORARIO]
- [X] horas mensuales para ajustes incluidas
- Revisión [mensual/quincenal] de conversaciones y optimización
- Informe mensual de actividad y oportunidades

**No incluye** (se presupuesta aparte si se necesita):
- [Lista adaptada]

**Consumos de herramientas**: [incluidos / se facturan aparte según uso]

---

**Desglose de cálculo interno** *(para tu referencia, no enviar al cliente)*:
| Concepto | €/mes |
|---|---|
| Costes herramientas | [X] € |
| Consumos estimados | [X] € |
| Soporte ([X]h × 60€) | [X] € |
| Optimización ([X]h × 60€) | [X] € |
| Margen seguridad | [X] € |
| Beneficio | [X] € |
| **Total calculado** | **[X] €** |
| **Precio comercial** | **[X] €/mes** |

---

Termina siempre con:
> ¿Quieres ajustar algún punto antes de presentarlo? Y cuando el cliente lo acepte, dime y te genero el contrato listo para firmar.

---

## MODO B — Generar Contrato de Mantenimiento

### Paso 1: Leer la plantilla de contrato

Lee `/mnt/skills/user/mantenimiento-ia/references/plantilla-contrato.md` para tener la estructura base.

### Paso 2: Solicitar datos que falten para el contrato

Si no están en la propuesta aceptada, pregunta **en un solo bloque**:

> Para generar el contrato necesito estos datos que no tengo:
> - Tus datos: nombre/razón social, NIF, dirección, email
> - Datos del cliente: nombre/razón social, NIF, dirección, email, persona que firma
> - Forma de pago (transferencia, domiciliación, etc.) y día de cobro
> - Ciudad y fecha del contrato
> - Duración inicial del contrato (recomendado: 6 o 12 meses)
> - Días de preaviso para cancelación (recomendado: 30 días)

### Paso 3: Generar el contrato

Sustituye todos los campos `[PLACEHOLDER]` de la plantilla con los datos reales.

Adapta específicamente:
- **Cláusula 2**: Incluye exactamente lo que tiene la propuesta aceptada.
- **Cláusula 3**: Excluye exactamente lo que no estaba en la propuesta.
- **Cláusula 4**: Refleja el precio, forma de pago y tratamiento de consumos variables.

### Paso 4: Entregar el contrato

Genera el contrato como archivo `.md` en `/mnt/user-data/outputs/contrato-mantenimiento-[cliente].md` y preséntalo al usuario.

Indica siempre al final:
> *Recomendación: revisa con tu asesor legal antes de la firma, especialmente si trabajas con datos sensibles o en sectores regulados.*

---

## Reglas generales de esta skill

1. **Nunca inventes datos** — si falta información, pregunta.
2. **Haz todas las preguntas en un solo bloque**, nunca en mensajes separados.
3. **Recomienda siempre precio hacia arriba si está justificado** — explica el porqué.
4. **Separa siempre costes de uso del servicio de mantenimiento** — es el error más común.
5. **El contrato siempre refleja exactamente lo de la propuesta** — sin añadir ni quitar.
6. **Tono profesional pero directo** — el usuario es freelance/agencia, no el cliente final.