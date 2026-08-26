# Manual de uso: Automatizaciones — n8n

Este manual explica cómo usar n8n, el sistema de automatización que conecta WhatsApp con el CRM de PalferIA. No se necesitan conocimientos de programación para entender lo esencial: cómo ver si todo funciona y cómo detectar problemas.

---

## Acceso

### Cómo entrar a n8n

1. Abre tu navegador web (Chrome, Firefox o Safari).
2. Escribe en la barra de direcciones: `https://n8n.srv905238.hstgr.cloud`
3. Pulsa **Enter**.
4. Introduce tus credenciales de acceso (email y contraseña que configuraste al instalar n8n).
5. Pulsa **Sign in** o **Entrar**.

💡 Guarda esta URL en tus marcadores del navegador. Solo necesitarás entrar aquí cuando quieras revisar si las automatizaciones están funcionando correctamente.

---

## Qué es n8n

**n8n** es un automatizador visual. Permite conectar aplicaciones entre sí sin necesidad de programar. Funciona con bloques visuales llamados **nodos**, que se conectan entre sí como si fueran piezas de un flujo.

En PalferIA, n8n se usa principalmente para:

- Recibir mensajes de WhatsApp a través de OpenWA
- Procesarlos y guardarlos en la base de datos del CRM (Supabase)
- Hacer que esos mensajes aparezcan en `https://sales.palferia.me` en la sección WhatsApp

---

## Workflow activo: OpenWA → Supabase CRM

### Nombre del workflow

El workflow principal se llama: **"OpenWA → Supabase CRM"**

### Qué hace este workflow

Cada vez que alguien envía un mensaje de WhatsApp a un número conectado en OpenWA:

1. OpenWA detecta el mensaje y avisa a n8n.
2. n8n procesa el mensaje (extrae el número, el texto, la fecha, etc.).
3. n8n busca si ese número pertenece a algún prospecto registrado en el CRM.
4. Guarda el mensaje en la base de datos.
5. El mensaje aparece en la sección WhatsApp de `https://sales.palferia.me`.

### Cómo ver si el workflow está activo

1. Entra a n8n en `https://n8n.srv905238.hstgr.cloud`.
2. En el menú lateral izquierdo, haz clic en **Workflows**.
3. Localiza el workflow **"OpenWA → Supabase CRM"** en la lista.
4. Comprueba que el **toggle** (interruptor) que aparece a la derecha del nombre está en color **verde**.
   - Verde = activo, procesando mensajes.
   - Gris = inactivo, no procesará mensajes hasta que lo actives.

⚠️ Si el toggle está gris, el workflow está desactivado. Los mensajes de WhatsApp no llegarán al CRM hasta que lo reactives. Haz clic en el toggle para activarlo.

### Cómo ver las ejecuciones del workflow

Cada vez que llega un mensaje de WhatsApp, el workflow se ejecuta una vez. Puedes ver el historial de ejecuciones para saber si todo va bien:

1. Abre el workflow **"OpenWA → Supabase CRM"** haciendo clic en su nombre.
2. Haz clic en la pestaña **Executions** (Ejecuciones) en la parte superior.
3. Verás una lista con todas las ejecuciones recientes.

**Interpretación del resultado:**

| Color | Significado |
|---|---|
| **Verde** | La ejecución fue exitosa. El mensaje se guardó correctamente en el CRM. |
| **Rojo** | Hubo un error. El mensaje puede no haberse guardado. Hay que investigarlo. |

💡 Las ejecuciones verdes son la normalidad. Solo actúa cuando veas ejecuciones rojas.

---

## Nodos del workflow explicados

El workflow está compuesto por 6 nodos que se ejecutan en secuencia. Aquí se explica qué hace cada uno en lenguaje sencillo:

### 1. Webhook OpenWA
Este es el punto de entrada. **Recibe el aviso de OpenWA** cuando llega un nuevo mensaje de WhatsApp. Actúa como una "puerta" que escucha en la URL:
```
https://n8n.srv905238.hstgr.cloud/webhook/openwa-messages
```

### 2. Responder OK
Inmediatamente después de recibir el mensaje, este nodo **envía una confirmación a OpenWA** diciéndole que n8n ha recibido la notificación correctamente. Es importante para que OpenWA no reintente el envío repetidamente.

### 3. Solo mensajes
Este nodo actúa como un **filtro**. OpenWA puede enviar distintos tipos de eventos (conexiones, desconexiones, etc.). Este nodo deja pasar únicamente los eventos de tipo **"message"** (mensaje real). El resto se descarta.

### 4. Extraer campos
Este nodo **lee el contenido del mensaje** y extrae la información relevante:
- Número de teléfono del remitente
- Texto del mensaje
- Dirección (si es entrante o saliente)
- Fecha y hora del mensaje

### 5. Buscar prospecto
Con el número de teléfono extraído, este nodo **consulta la base de datos de Supabase** para ver si ese número pertenece a algún prospecto registrado en el CRM. Si lo encuentra, obtiene el ID del prospecto para asociarlo al mensaje.

### 6. Guardar en Supabase
El último nodo **guarda el mensaje en la base de datos** (tabla `mensajes_whatsapp` de Supabase). A partir de ese momento, el mensaje aparece en la sección WhatsApp de `https://sales.palferia.me`.

---

## Cómo crear un workflow nuevo (conceptos básicos)

Si en algún momento necesitas crear una automatización nueva:

1. En el menú lateral izquierdo de n8n, haz clic en el botón **"+"** (o en **New Workflow**).
2. Se abrirá un lienzo en blanco.
3. Haz clic en el botón **"+"** del centro del lienzo o en **Add node** para añadir el primer nodo.
4. Busca **Webhook** en el buscador de nodos y selecciónalo. Este será el punto de inicio (trigger) del workflow.
5. Configura el webhook según lo que necesites recibir.
6. Para añadir más nodos, haz clic en el botón **"+"** que aparece al final de cada nodo ya colocado.
7. Conecta los nodos arrastrando desde el punto de salida de uno hasta el punto de entrada del siguiente.
8. Cuando el workflow esté listo, actívalo con el **toggle** que aparece en la esquina superior derecha del editor.

💡 Puedes probar un workflow sin activarlo usando el botón **Test Workflow** o **Execute Workflow**. Esto ejecuta el flujo manualmente para comprobar que funciona antes de ponerlo en producción.

---

## Credenciales configuradas

### Supabase API Header

Para que n8n pueda acceder a la base de datos del CRM (Supabase), está configurada una credencial llamada **Supabase API Header**. Esta credencial contiene la `apikey` necesaria para autenticarse.

### Cómo usar las credenciales en un nodo nuevo

Cuando añadas un nodo de tipo **HTTP Request** que necesite llamar a Supabase:

1. En la configuración del nodo, busca la sección de **Authentication** o **Headers**.
2. Selecciona la opción **Predefined Credential Type** o **Use existing credential**.
3. Elige la credencial **Supabase API Header** de la lista.
4. El nodo usará automáticamente la clave correcta sin que tengas que escribirla manualmente.

⚠️ Nunca escribas claves API directamente en los nodos de texto libre. Usa siempre las credenciales guardadas para mantener la seguridad.

---

## Cuándo revisar n8n

Deberías entrar a n8n en estas situaciones:

### Si un mensaje de WhatsApp no aparece en el CRM

1. Entra a `https://n8n.srv905238.hstgr.cloud`.
2. Ve a **Workflows** y abre **"OpenWA → Supabase CRM"**.
3. Comprueba que el workflow está **activo** (toggle verde).
4. Haz clic en la pestaña **Executions**.
5. Busca si hay una ejecución reciente que corresponda al momento en que se envió el mensaje.
6. Si la ejecución aparece en **rojo**, haz clic sobre ella para ver el detalle del error.

### Si hay ejecuciones rojas

1. Haz clic sobre la ejecución roja en la lista.
2. Se abrirán los nodos del workflow mostrando cuál falló (aparecerá marcado en rojo).
3. Haz clic en el nodo fallido para ver el mensaje de error detallado.
4. Lee el error. Los más comunes son:
   - **Error de conexión**: Supabase o OpenWA no estaban disponibles en ese momento. Suele resolverse solo.
   - **Error de autenticación**: La API key puede haber caducado o cambiado.
   - **Datos inesperados**: El formato del mensaje no era el esperado.

💡 Si el error se repite con frecuencia, es señal de que algo ha cambiado en la configuración. Contacta con el administrador técnico para revisarlo.

### Si el workflow está desactivado

1. Ve a **Workflows** en el menú lateral.
2. Localiza **"OpenWA → Supabase CRM"**.
3. Haz clic en el **toggle** para activarlo. Pasará a color verde.
4. Verifica que las próximas ejecuciones aparecen correctamente.

---

## URL de referencia del webhook

El webhook que usa OpenWA para enviar los mensajes a n8n es:

```
https://n8n.srv905238.hstgr.cloud/webhook/openwa-messages
```

Esta URL debe estar configurada en cada sesión de OpenWA que crees en `https://wa.palferia.me`. Si una sesión nueva no tiene esta URL configurada en sus webhooks, sus mensajes no llegarán al CRM automáticamente.

💡 Cuando crees una sesión nueva en OpenWA, lo primero que debes hacer después de conectarla es configurar este webhook. Consulta el manual de `wa.palferia.me` para ver los pasos exactos.
