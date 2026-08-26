# Mejores prácticas para usar Prompt Builder Agentes n8n

## Cómo formular tu solicitud inicial

### Opción 1: Descripción simple y clara

**Usa esto cuando tienes una idea clara:**

> "Necesito un agente que valide emails de clientes y rechace dominios temporales"

✅ **Qué está bien:**
- Es una frase corta y directa
- Define el objetivo claro (validar emails)
- Menciona un criterio importante (rechazar temporales)

### Opción 2: Contexto más rico

**Usa esto cuando el contexto importa:**

> "Tengo un workflow de onboarding de clientes en n8n que recibe formularios. Quiero que el agente verifique que el email sea válido, que no sea un dominio temporal, y que luego consulte nuestra base de datos para ver si ese cliente ya existe. Si existe, debe alertar; si no, debe crear el contacto automáticamente."

✅ **Qué está bien:**
- Explica el contexto (onboarding de clientes)
- Describe el flujo completo
- Menciona herramientas (base de datos)
- Especifica el flujo de decisión (existe/no existe)

### Opción 3: Solicitud con restricciones

**Usa esto cuando tienes limitaciones importantes:**

> "Necesito un agente que clasifique solicitudes de soporte. Crítico = cliente sin acceso al servicio, Alto = funcionalidad importante rota, Normal = característica no disponible, Bajo = todo lo demás. IMPORTANTE: no debo mostrar datos personales en los logs, y todo debe estar en JSON para integración con un nodo anterior."

✅ **Qué está bien:**
- Especifica criterios precisos
- Menciona restricciones importantes (privacidad)
- Define el formato exacto (JSON)
- Usa énfasis para lo crítico

## Cómo responder las preguntas de Claude

### Cuando sabes la respuesta exacta

**Claude pregunta:**
> ¿Qué información tendrá disponible el agente del email?

**Responde así:**
> Tendrá: De, Asunto, Cuerpo, Fecha, y si es posible, nombre del cliente desde nuestra base de datos.

✅ **Bien porque:**
- Es específico
- Es concreto (no vago)
- Menciona fuentes (base de datos)

### Cuando tienes una idea aproximada

**Claude pregunta:**
> ¿Qué debe hacer el agente si el cliente no existe?

**Responde así:**
> No estoy 100% seguro, pero probablemente devolver error porque no queremos crear clientes desde el agente. ¿Suena bien?

✅ **Bien porque:**
- Eres honesto sobre la incertidumbre
- Ofreces tu mejor suposición
- Invitas a Claude a ayudarte

### Cuando necesitas ayuda para decidir

**Claude pregunta:**
> ¿El agente debe solo clasificar o también tomar acciones (enviar email, crear ticket)?

**Responde así:**
> No estoy seguro de cuál es mejor práctica. ¿Qué me recomiendas? Probablemente solo clasificar para mantenerlo simple.

✅ **Bien porque:**
- Pides consejo
- Expresas una preferencia (mantener simple)
- Aceptas orientación

### Cuando necesitas aclarar

**Claude pregunta:**
> ¿Cuáles son los campos que pueden cambiar en el CRM?

**Responde así:**
> Buena pregunta. Campos "seguros": email, teléfono, dirección. Campos "críticos" que necesitan aprobación: estado de cliente, plan de servicio. Campos que NUNCA se cambian: fecha de creación, ID cliente.

✅ **Bien porque:**
- Eres específico
- Categorizes los campos
- Mencionas reglas de negocio

## Tácticas para obtener mejores resultados

### 1. Empieza con el caso de uso más simple

**Malo:**
> "Necesito un sistema que maneje todo el flujo de soporte: clasificación, asignación, escalado, redacción de respuestas, tracking de satisfacción y reportes"

**Mejor:**
> "Empecemos con solo la clasificación de urgencia. Una vez que eso funcione, podemos agregar asignación."

✅ **Por qué funciona mejor:**
- Prompts simples = mejor calidad
- Puedes iterar
- Menos confusión

### 2. Comparte ejemplos reales (o aproximados)

**Malo:**
> "Necesito procesar solicitudes de cambio"

**Mejor:**
> Ejemplo de solicitud:
> ```
> Cliente: John Smith
> Cambio solicitado: Email
> Valor actual: john@old.com
> Valor nuevo: john@company.com
> Tipo de cambio: Menor
> ```
>
> Ejemplo de respuesta esperada:
> ```json
> {
>   "estado": "aprobado",
>   "timestamp": "...",
>   "notificacion": "Email actualizado. Se envió confirmación a john@company.com"
> }
> ```

✅ **Por qué funciona mejor:**
- Claude ve exactamente qué esperas
- Evita malinterpretaciones
- El prompt resultante es más preciso

### 3. Sé explícito sobre lo que NO debe hacer

**Malo:**
> "El agente debe ser cuidadoso con datos sensibles"

**Mejor:**
> "El agente debe:
> - NO copiar el cuerpo completo del email en logs
> - NO mostrar números de tarjeta de crédito
> - NO revelar qué proveedor usa el cliente
> - NO crear registros de intentos fallidos en el CRM público"

✅ **Por qué funciona mejor:**
- Protege realmente tus datos
- Evita olvidos
- El prompt es más seguro

### 4. Menciona decisiones difíciles

**Malo:**
> "El agente debe decidir si aprobar o rechazar"

**Mejor:**
> "El agente debe decidir si aprobar o rechazar. Caso difícil: cliente VIP con histórico de reembolsos frecuentes. ¿Aún aprobamos automáticamente o escalamos? Creo que aprobamos porque son VIP, pero confirma que tiene sentido."

✅ **Por qué funciona mejor:**
- Ayuda a Claude a pensar en edge cases
- Documento tus propias dudas
- Consegues guía experta

### 5. Sugiere mejoras durante el proceso

**Malo:**
> [Solo responde lo que preguntas]

**Mejor:**
> "Respondo lo que preguntas, pero se me ocurre: ¿el agente podría detectar automáticamente qué tipo de cambio es (menor/crítico) en lugar de que lo especifique el usuario? Sería más eficiente."

✅ **Por qué funciona mejor:**
- Colaboras en el diseño
- Claude mejora el agente
- El resultado es más inteligente

## Patrones de preguntas útiles para Claude

### Si necesitas aclaración
> "¿Podrías darme un ejemplo de lo que significa 'urgencia Alta'? Me cuesta decidir entre Alto y Crítico."

### Si quieres iterar
> "¿Cómo cambiaría el prompt si agregamos la capacidad de enviar emails automáticos?"

### Si quieres validar
> "¿El prompt que generaste cubre los 3 ejemplos que di? Déjame verificar..."

### Si quieres optimizar
> "¿El prompt es muy largo? ¿Puedo reducirlo sin perder información?"

### Si necesitas ayuda en diseño
> "No sé si debería tomar esta decisión automáticamente o escalar a un humano. ¿Qué dice la mejor práctica?"

## Errores comunes y cómo evitarlos

### Error 1: No compartir contexto importante

**Mal:**
> "Necesito un agente para procesar solicitudes"

**Bien:**
> "Necesito un agente para procesar solicitudes de cambio de datos de clientes en nuestro CRM. Estos cambios vienen de un formulario web y afectan qué información ven nuestros sales. Por eso importa validación y auditoría."

### Error 2: Ser demasiado vago

**Mal:**
> "El agente debe ser inteligente y saber qué hacer"

**Bien:**
> "El agente debe:
> 1. Verificar que el email sea válido
> 2. Si no es válido, rechazar
> 3. Si es válido pero es dominio temporal, rechazar
> 4. Si es válido y permanente, continuar"

### Error 3: Cambiar de opinión constantemente

**Evita decir:**
> "Espera, cambié de idea sobre cómo debería funcionar..."

**Mejor:**
> "Estaba pensando X, pero ahora creo que Y sería mejor. ¿Cuál tiene más sentido?"

Claude puede iterar, pero es más eficiente si tienes una dirección clara.

### Error 4: No revisar lo generado

**Mal:**
> [Aceptar el prompt sin verlo]

**Bien:**
> "Perfecto, déjame revisar si el prompt cubre todos los casos:
> - Caso A: ✅
> - Caso B: Falta mencionar X
> - Caso C: ✅
>
> ¿Puedes agregar la mención de X en Caso B?"

### Error 5: Olvidar el contexto n8n

Recuerda que el prompt es para **un agente de n8n**. Menciona si:
- Usará nodos específicos (HTTP, Database, Email, etc.)
- Necesita integración con herramientas externas
- Tiene límites de tiempo o recursos
- Debe seguir un formato específico que otro nodo espera

## Checklist antes de copiar el prompt a n8n

Antes de pegar el prompt en tu agente n8n, verifica:

- ✅ ¿Entiendo cada sección?
- ✅ ¿Los ejemplos se parecen a mis datos reales?
- ✅ ¿El formato de salida es lo que esperaba?
- ✅ ¿Faltan casos especiales que debería mencionar?
- ✅ ¿Hay restricciones que olvidé mencionar?
- ✅ ¿El tono y el nivel de detalle son apropiados?
- ✅ ¿Cubre todos los flujos de decisión?

Si algo no está bien, pide a Claude que lo ajuste:

> "En la sección de Manejo de Errores, agrégale también qué hacer si [caso especial que no cubrimos]"

## Iteración rápida

Si necesitas mejorar el prompt después de usarlo en n8n:

**Di a Claude:**
> "Probé el prompt en n8n y encontré que [problema]. Además, necesito que [mejora]. ¿Puedes actualizar el prompt?"

Claude puede revisar, cambiar y entregar una versión mejorada en minutos.

---

**Recuerda:** Cuanta más información específica proporciones, mejor será el prompt resultante. No temas ser detallado o dar ejemplos largos; eso es exactamente lo que Claude necesita.
