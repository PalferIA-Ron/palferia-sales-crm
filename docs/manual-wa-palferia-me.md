# Manual de uso: Panel de WhatsApp — wa.palferia.me

Este manual explica cómo usar el panel de gestión de WhatsApp de PalferIA, basado en OpenWA. No se necesitan conocimientos técnicos. Sigue los pasos con cuidado, especialmente al conectar números nuevos.

---

## Acceso al panel

### Cómo entrar

1. Abre tu navegador web (Chrome, Firefox o Safari).
2. Escribe en la barra de direcciones: `https://wa.palferia.me`
3. Pulsa **Enter**.
4. El sistema te pedirá una **API Key** de acceso.
5. Introduce la clave: `M4rtin091121+`
6. Pulsa **Acceder** o **Confirmar**.

💡 Guarda esta URL en tus marcadores del navegador para acceder rápidamente.

⚠️ La API Key es como una contraseña. No la compartas con personas que no deban tener acceso al sistema.

### Qué es OpenWA

**OpenWA** es el sistema que permite conectar uno o varios números de WhatsApp Business al servidor de PalferIA. Desde este panel puedes:

- Conectar números de WhatsApp (creando "sesiones")
- Ver el estado de cada número conectado
- Enviar mensajes manualmente
- Configurar notificaciones automáticas (webhooks) para que los mensajes fluyan hacia el CRM

---

## Gestión de sesiones

### Qué es una sesión

Una **sesión** representa un número de WhatsApp conectado al sistema. Cada número físico de WhatsApp Business que quieras usar necesita su propia sesión. Una sesión activa permite enviar y recibir mensajes desde ese número a través de OpenWA.

### Cómo crear una sesión nueva

1. Desde el panel principal de `https://wa.palferia.me`, pulsa el botón **New Session**.
2. Escribe un **nombre descriptivo** para identificar la sesión. Usa nombres claros y sin espacios, por ejemplo:
   - `palferia-principal`
   - `cortinajes-valls`
   - `tecniluispa`
3. Pulsa **Crear** o **Create**.
4. La sesión aparece en la lista con el estado **created**.

### Cómo conectar el número de WhatsApp a la sesión

Una vez creada la sesión, hay que vincularla con el móvil:

1. Localiza la sesión recién creada en la lista.
2. Pulsa el botón **Start** o **Iniciar** junto a esa sesión.
3. Espera unos segundos. El estado cambiará a **qr_ready** y aparecerá un código QR en pantalla.
4. Coge el móvil que tiene el número de WhatsApp Business que quieres conectar.
5. Abre **WhatsApp** en el móvil.
6. Ve a **Ajustes** (o los tres puntos en Android) → **Dispositivos vinculados** → **Vincular un dispositivo**.
7. Apunta la cámara del móvil al código QR que aparece en la pantalla del ordenador.
8. WhatsApp escaneará el código automáticamente.
9. En pocos segundos, el estado de la sesión pasará a **connected**.

⚠️ El código QR caduca en aproximadamente 60 segundos. Si no lo escaneas a tiempo, vuelve a pulsar **Start** para generar uno nuevo.

⚠️ Si el móvil pierde la conexión a internet o se reinicia, es posible que la sesión se desconecte. En ese caso tendrás que repetir el proceso de escaneo del QR.

💡 Mantén el móvil con batería y conexión a internet para que la sesión permanezca activa de forma continua.

### Estados de una sesión

| Estado | Significado |
|---|---|
| **created** | La sesión ha sido creada pero aún no se ha iniciado |
| **qr_ready** | Se ha generado el QR, está esperando que el móvil lo escanee |
| **connected** | El número está vinculado y activo. Puede enviar y recibir mensajes |
| **disconnected** | El número se ha desconectado. Hay que re-escanear el QR para reconectar |

### Cómo desconectar o eliminar una sesión

**Para desconectar** (sin eliminarla permanentemente):

1. Localiza la sesión en la lista.
2. Pulsa el botón **Stop** o **Detener**.
3. La sesión pasará al estado **disconnected**.

**Para eliminar definitivamente:**

1. Localiza la sesión en la lista.
2. Pulsa el botón **Eliminar** o el icono de papelera.
3. Confirma la acción cuando el sistema lo solicite.

⚠️ Si eliminas una sesión, perderás su configuración y deberás crear una nueva y volver a escanear el QR. No hay forma de recuperarla.

---

## Enviar mensajes desde el panel

Desde el panel de OpenWA también puedes enviar mensajes manualmente a cualquier número:

1. Selecciona la sesión activa (en estado **connected**) desde la que quieres enviar.
2. Busca el contacto en la lista, o introduce el número manualmente.
3. **Formato del número**: escribe el número sin el símbolo `+` ni espacios, incluyendo el prefijo del país. Por ejemplo, para un número español: `34612345678` (el 34 es el prefijo de España).
4. Escribe el mensaje en el campo de texto.
5. Pulsa **Enviar**.

💡 Para números de otros países, usa el prefijo correspondiente. Por ejemplo, México sería `521XXXXXXXXXX`.

⚠️ Solo puedes enviar mensajes desde sesiones en estado **connected**. Si la sesión está desconectada, los mensajes no se enviarán.

---

## Webhooks

### Qué es un webhook

Un **webhook** es una notificación automática que el sistema envía a otra aplicación cuando ocurre algo. En este caso, cada vez que llega un nuevo mensaje de WhatsApp a una sesión conectada, OpenWA puede avisar automáticamente al CRM o a n8n para que procese ese mensaje.

### Webhook configurado en PalferIA

El webhook activo para recibir mensajes de WhatsApp y procesarlos en n8n es:

```
https://n8n.srv905238.hstgr.cloud/webhook/openwa-messages
```

### Cuándo y cómo configurar el webhook

El webhook debe configurarse **cada vez que crees una sesión nueva**. Pasos:

1. Accede a la configuración de la sesión recién creada.
2. Busca la sección de **Webhooks** o **Eventos**.
3. Introduce la URL del webhook: `https://n8n.srv905238.hstgr.cloud/webhook/openwa-messages`
4. Marca el evento a escuchar: **message** (para recibir todos los mensajes entrantes).
5. Guarda la configuración.

⚠️ Si no configuras el webhook, los mensajes de WhatsApp no llegarán al CRM automáticamente. Tendrías que copiarlos a mano.

💡 Verifica que el webhook está activo enviando un mensaje de prueba al número conectado. Luego comprueba en n8n que aparece una nueva ejecución del workflow.

---

## Multi-sesión para clientes de PalferIA

### Cómo funciona el sistema multi-sesión

Cada cliente de PalferIA puede tener su propia sesión conectada con su número de WhatsApp Business particular. Esto permite que cada negocio gestione sus propias conversaciones de forma independiente desde el mismo servidor.

### Convención de nombres para sesiones de clientes

Usa siempre el formato: `nombre-cliente` (en minúsculas, sin espacios, usando guiones). Ejemplos:

- `cortinajes-valls`
- `tecniluispa`
- `palferia-principal`

### Requisitos por sesión

Cada sesión de cliente necesita:

1. Un **número de WhatsApp Business** propio y exclusivo (no puede compartirse entre sesiones).
2. Un **móvil** o número activo donde esté instalado ese WhatsApp.
3. La **configuración del webhook** apuntando a la URL de n8n.

💡 Si un cliente quiere usar su propio número de WhatsApp para recibir mensajes a través del sistema de PalferIA, solo necesita escanear el QR una vez desde su móvil.

---

## Limites y advertencias importantes

⚠️ **Límite de mensajes diarios**: No envíes más de **200-300 mensajes por día** desde un mismo número. WhatsApp puede bloquear el número si detecta un volumen inusual de mensajes en poco tiempo.

⚠️ **Prohibido el spam masivo**: Este sistema está pensado para comunicaciones comerciales legítimas y personalizadas, no para envíos masivos no solicitados. El uso abusivo puede resultar en el bloqueo permanente del número.

⚠️ **Sin copia de seguridad de sesiones**: Si borras una sesión, no hay forma de recuperarla. Tendrás que crear una nueva y volver a escanear el QR desde el móvil.

⚠️ **Desconexiones por inactividad del móvil**: Si el móvil asociado a una sesión se apaga, pierde internet o cierra la aplicación de WhatsApp, la sesión puede desconectarse. Mantén el móvil encendido y con datos o WiFi activos.

💡 Si un número se bloquea, deberás usar otro número de teléfono para crear una nueva sesión. No hay forma de desbloquear un número baneado por WhatsApp desde este sistema.
