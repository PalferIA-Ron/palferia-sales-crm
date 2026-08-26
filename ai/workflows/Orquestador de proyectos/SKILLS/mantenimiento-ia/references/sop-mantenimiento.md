# SOP: Cálculo de Mantenimiento de Soluciones IA

## Los 5 bloques del mantenimiento

### 1. Infraestructura
Hosting, n8n, Supabase, OpenAI/Claude/ElevenLabs/Retell, WhatsApp API, número telefónico, herramientas externas, logs, monitorización, backups.
**Regla**: Separar siempre "costes de uso" y "servicio de mantenimiento".

### 2. Soporte
**Incluye**: Resolver errores, revisar automatizaciones caídas, ajustar comportamientos incorrectos, atender dudas del cliente, revisar envíos fallidos, comprobar integraciones.
**No incluye**: Nuevos funnels, nuevos canales, rediseño del agente, nuevas integraciones, cambios de modelo de negocio, landing pages, formación semanal.
**Regla clave**: "Mantenimiento corrige y optimiza lo existente. Desarrollo crea cosas nuevas."

### 3. Optimización
Revisión de conversaciones, detección de preguntas mal respondidas, mejora del prompt, ajuste de tono, nuevas FAQs, mejora de cualificación de leads, mejora de derivación a humano, reducción de respuestas innecesarias, mejora de ratio de cita o conversión.

### 4. Reporting
Número de conversaciones, leads cualificados, citas generadas, llamadas atendidas/perdidas, tiempo ahorrado, preguntas frecuentes, errores detectados, oportunidades perdidas, recomendaciones de mejora.

### 5. Riesgo y responsabilidad
Cuanto más crítico sea el sistema, más caro debe ser el mantenimiento. No se cobra solo por tiempo, se cobra por responsabilidad.

---

## Variables de cálculo

### Variable 1: Número de canales
- Solo 1 canal (WhatsApp, webchat, etc.) → factor bajo
- 2-3 canales → factor medio
- 4+ canales o voz → factor alto

### Variable 2: Volumen de conversaciones (texto)
| Volumen mensual | Tipo |
|---|---|
| 0-300 | Básico |
| 300-1.000 | Profesional |
| 1.000-3.000 | Avanzado |
| +3.000 | Personalizado |

### Variable 2b: Volumen de llamadas (voz)
| Volumen mensual | Tipo |
|---|---|
| 0-100 | Básico |
| 100-500 | Profesional |
| 500-1.500 | Avanzado |
| +1.500 | Personalizado |

### Variable 3: Complejidad del agente
- **Nivel 1 - FAQ**: Responde preguntas frecuentes
- **Nivel 2 - Cualificación**: Hace preguntas, filtra leads, deriva
- **Nivel 3 - Agendamiento**: Consulta disponibilidad y agenda citas
- **Nivel 4 - Operativo**: Actualiza CRM, crea tareas, envía documentos, genera presupuestos
- **Nivel 5 - Crítico**: Interviene en ventas, pagos, incidencias o procesos importantes

### Variable 4: Integraciones
Cada integración crítica añade una capa de mantenimiento.
Integraciones posibles: Google Calendar, GHL, HubSpot, Airtable, Supabase, Stripe, WhatsApp Cloud API, Retell, ElevenLabs, Make, n8n, Gmail, Google Sheets.

### Variable 5: Nivel de soporte
| Plan | Tiempo de respuesta |
|---|---|
| Básico | 48-72 h laborables |
| Pro | 24-48 h laborables |
| Premium | 24 h laborables |
| Crítico | Soporte prioritario |

---

## Modelos de precio

### Modelo 1: Fijo + consumos aparte (recomendado por defecto)
- Setup: 1.500€ - 5.000€
- Mantenimiento: 250€ - 1.500€/mes
- Consumos: aparte según uso

### Modelo 2: Con bolsa incluida
- Precio fijo que incluye X conversaciones + X horas de ajustes
- Exceso se factura aparte

### Modelo 3: Fijo + variable por resultado
- Base fija + variable por cita/lead/venta atribuida
- Solo cuando se puede medir bien el resultado

---

## Fórmula práctica

```
Mantenimiento mensual =
  costes fijos de herramientas
+ costes variables estimados
+ horas de soporte previstas × tarifa/hora (60€)
+ horas de optimización × tarifa/hora (60€)
+ margen de seguridad
+ beneficio
```

---

## Planes de referencia

### Plan Básico — 250€/mes
- Supervisión básica, corrección de errores
- Hasta 1 hora mensual de ajustes
- Soporte por email
- Revisión mensual ligera
- Consumos aparte
- **Ideal para**: Chatbots FAQ, bajo volumen, pocas integraciones

### Plan Profesional — 490€/mes
- Supervisión del sistema
- Hasta 3 horas mensuales de ajustes
- Revisión de conversaciones + optimización del prompt
- Informe mensual
- Soporte prioritario en horario laboral
- Consumos aparte
- **Ideal para**: WhatsApp, cualificación de leads, agendamiento, integración CRM/calendario

### Plan Avanzado — 900€/mes
- Hasta 6 horas mensuales de ajustes
- Revisión quincenal
- Optimización de flujos + informe avanzado
- Monitorización de incidencias + reunión mensual
- Consumos aparte
- **Ideal para**: Agente de voz, varios canales, varias integraciones, alto volumen

### Plan Crítico — desde 1.500€/mes
- Soporte prioritario + monitorización frecuente
- Revisión semanal + optimización continua
- Informes avanzados + bolsa amplia de horas
- Plan de contingencia
- **Ideal para**: Centros con muchas llamadas, equipos comerciales, franquicias, alto volumen de leads, automatizaciones críticas

---

## Qué incluye y qué no incluye (modelo de contrato)

### Siempre incluido:
- Supervisión básica del sistema
- Corrección de errores
- Ajustes menores del prompt
- Revisión mensual de conversaciones
- Actualización de FAQs existentes
- Soporte dentro del horario acordado
- Informe mensual de actividad
- Hasta X horas mensuales de ajustes

### Nunca incluido por defecto:
- Nuevos canales
- Nuevas integraciones
- Rediseño completo del agente
- Nuevas automatizaciones
- Cambios estratégicos del proceso comercial
- Formación recurrente al equipo
- Soporte fuera de horario
- Consumos extraordinarios
- Herramientas externas no incluidas inicialmente
- Cambios provocados por modificaciones en sistemas de terceros

**Cláusula clave**: "Todo lo que no esté incluido expresamente, se presupuestará aparte."