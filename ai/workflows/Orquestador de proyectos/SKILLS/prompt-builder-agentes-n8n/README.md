# Prompt Builder para Agentes de n8n

## ¿Qué es esta skill?

Esta es una skill de Claude que te ayuda a **crear prompts profesionales y listos para usar en agentes de n8n** sin necesidad de configurar n8n manualmente.

Actúa como un consultor experto en automatización que:
- ✅ Te hace preguntas guiadas sobre tu caso de uso
- ✅ Recopila información de forma estructurada
- ✅ Genera un prompt final en Markdown
- ✅ El prompt está listo para copiar y pegar en tu agente de n8n

## Cómo usarla

### Paso 1: Mención tu idea

Simplemente dile a Claude algo como:

> "Quiero un agente que clasifique emails de soporte"
> 
> "Necesito automatizar solicitudes de cambio en mi CRM"
>
> "Tengo un agente que debe redactar respuestas a clientes"

### Paso 2: Responde las preguntas

Claude te hará preguntas sobre:
- Qué debe hacer exactamente el agente
- Qué información recibirá
- Qué debe devolver
- Qué reglas debe seguir
- Qué herramientas usará
- Cómo manejar errores
- Ejemplos reales

Puedes responder con detalle, vagamente, o solo parcialmente. Claude se adaptará.

### Paso 3: Obtén el prompt final

Cuando tengas suficiente información, Claude generará un prompt final en Markdown que puedes:
- **Copiar completamente**
- **Pegar directamente en un agente de n8n**
- **Usar sin modificaciones**

## Ejemplo: Caso de uso real

### Usuario
> "Necesito un agente que revise solicitudes de cambio de datos en mi CRM"

### Claude (primera pregunta)
> Entiendo. Empecemos con algunos detalles:
> 
> 1. ¿Qué datos pueden cambiar? (nombre, email, teléfono, dirección, tags?)
> 2. ¿El agente debe validar que los cambios sean correctos?
> 3. ¿Requiere aprobación de un humano antes de aplicar?

### Usuario
> 1. Pueden cambiar: email, teléfono, dirección, estado
> 2. Sí, debe validar formato (email válido, teléfono con formato correcto)
> 3. Cambios menores son automáticos, pero cambios de estado requieren revisión

### Claude (siguiente pregunta)
> Perfecto. Ahora:
> 
> 1. ¿Qué cuenta como "cambio menor"?
> 2. ¿El agente logueará los cambios en algún lugar?
> 3. ¿Qué pasa si hay un error de validación?

### ... y así continúa

Cuando tengas información suficiente, Claude genera:

```markdown
# Rol del agente

Eres un procesador de cambios de CRM especializado...

# Objetivo principal

Validar, ejecutar y registrar cambios de datos de contactos...

# Entradas disponibles

- ID del contacto
- Campo a cambiar
- Nuevo valor
- Usuario que solicita el cambio

# Tarea

1. Valida el formato del nuevo valor
2. Si es válido y es cambio menor, ejecuta
3. Si requiere aprobación, crea ticket de revisión
...

# Reglas de comportamiento

- Valida antes de ejecutar
- Registra TODOS los cambios
- Rechaza datos inválidos
...

# Ejemplos

Entrada: ID=12345, campo=email, valor=nuevo@email.com, tipo=cambio_menor

Salida:
```json
{
  "estado": "éxito",
  "cambio_aplicado": true,
  "timestamp": "2025-05-27T10:30:00Z"
}
```

# ... etc
```

**Listo para copiar y pegar en n8n.**

## Casos de uso comunes

### 1. Clasificar o categorizar
- Clasificar emails por urgencia
- Categorizar tickets por tipo
- Priorizar tareas
- Etiquetar contenido

### 2. Procesar solicitudes
- Solicitudes de cambio de datos
- Reembolsos o devoluciones
- Nuevos clientes
- Modificaciones de pedidos

### 3. Redactar contenido
- Respuestas automáticas a clientes
- Emails de confirmación
- Resúmenes de conversaciones
- Reportes

### 4. Tomar decisiones
- Aprobar/rechazar solicitudes
- Escalar a humanos
- Enrutar a equipos
- Aplicar reglas de negocio

### 5. Extraer o transformar datos
- Obtener información de texto no estructurado
- Normalizar formatos
- Crear resúmenes
- Traducir entre formatos

## Lo que NO hace esta skill

❌ **No configura n8n.** Eso lo haces tú en tu workspace.

❌ **No crea workflows.** Solo crea el prompt para el agente.

❌ **No se conecta a n8n.** No accede a tu sistema.

❌ **No ejecuta nada.** Solo ayuda a formular el prompt.

## Estructura del prompt generado

Todos los prompts generados siguen esta estructura:

```
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

Esto asegura que el agente entienda exactamente qué hacer.

## Tips para mejores resultados

### ✅ Sé específico cuando puedas
> "Necesito que valide emails con formato correcto y rechace dominios temporales"
> 
> Es mejor que: "Necesito un validador"

### ✅ Comparte ejemplos reales
> "Por ejemplo, un cliente reporta 'Mi cuenta no funciona desde ayer', eso sería Crítico"
>
> Es mejor que: "Solo clasifícalo por urgencia"

### ✅ Menciona restricciones importantes
> "No debe hacer público ningún email de clientes"
>
> "Máximo 300 caracteres en la respuesta"

### ✅ Describe el contexto empresarial
> "Somos una plataforma SaaS con 1000 clientes, el tiempo de respuesta es crítico"
>
> Ayuda a Claude entender por qué importan ciertos detalles

### ✅ Sé honesto sobre lo que sabes
> "Aún no sé exactamente qué datos tendremos disponibles, pero probablemente: nombre, email y descripción del problema"
>
> Es perfectamente válido. Claude puede ayudarte a clarificar.

## Preguntas frecuentes

### ¿Puedo pedir solo un prompt parcial?
Sí. Puedes decir "Hazme un prompt pero solo hasta la fase de entradas" o "Genera el prompt final con lo que ya sabes".

### ¿Qué pasa si no sé todos los detalles?
Perfecto. Claude preguntará y ayudará a clarificar. Es normal no saberlo todo de inicio.

### ¿El prompt funcionará perfectamente en n8n?
Debería sí. Pero es posible que necesites pequeños ajustes cuando lo pongas en práctica. El prompt es una base sólida, pero cada implementación es única.

### ¿Puedo hacer una nueva versión del prompt?
Absolutamente. Puedes decir "Dame una versión más breve" o "Hazlo más técnico" o "Ignora la regla X y agrégale Y".

### ¿Funciona en otros idiomas?
Esta skill está en español, pero Claude puede generar prompts en cualquier idioma si lo solicitas.

## Roadmap

Futuras mejoras podrían incluir:
- [ ] Plantillas predefinidas para casos comunes
- [ ] Integración directa con n8n (solo lectura/verificación)
- [ ] Validador de prompts
- [ ] Historial de prompts anteriores
- [ ] Generación de test cases automáticos
- [ ] Documentación en otros idiomas

## Soporte

Si la skill no funciona como esperas:
1. Sé más específico en tu descripción
2. Comparte ejemplos reales
3. Menciona exactamente qué quieres que cambie

Claude iterará hasta que esté perfecto.

---

**Versión:** 1.0  
**Creada:** 2025-05-27  
**Última actualización:** 2025-05-27  
**Estado:** Producción ✅