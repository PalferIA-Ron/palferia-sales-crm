---
name: extension-chrome
description: Crea extensiones de Chrome completas y funcionales con Manifest V3. Genera todos los archivos necesarios listos para instalar en 2 minutos sin configuración extra.
version: 1.0.0
author: PalferIA
---

# Creador de Extensiones Chrome

Crea extensiones de Chrome completas con Manifest V3, listas para instalar directamente desde Chrome.

## Flujo

### 1. Entender qué debe hacer la extensión
Preguntar si no está claro:
- ¿Qué hace la extensión? (función principal)
- ¿Interactúa con páginas web, con el navegador, o es independiente?
- ¿Necesita un popup? ¿Tiene configuración?
- ¿Funciona en todas las webs o solo en algunas?

### 2. Elegir la arquitectura

Según lo que necesite, usar los componentes adecuados de Manifest V3:

| Componente | Cuándo usarlo |
|---|---|
| `popup.html` | La extensión tiene interfaz al hacer click en el icono |
| `content_script.js` | Necesita leer o modificar páginas web |
| `background.js` (Service Worker) | Necesita ejecutarse en segundo plano |
| `options.html` | Tiene configuración persistente |

### 3. Generar todos los archivos

Crear una carpeta con el nombre de la extensión (en kebab-case) y generar:

**Siempre:**
- `manifest.json` con Manifest V3
- Iconos: `icons/icon16.png`, `icons/icon48.png`, `icons/icon128.png` (generar con canvas o SVG inline si no hay assets)

**Según arquitectura:**
- `popup.html` + `popup.css` + `popup.js`
- `content.js`
- `background.js`
- `options.html` + `options.js`

### 4. Estándares de calidad

**manifest.json:**
- `manifest_version: 3` (siempre V3)
- Permisos mínimos necesarios (no pedir más de lo que se usa)
- `host_permissions` solo si accede a URLs específicas

**Código:**
- JavaScript moderno (ES2020+), sin jQuery ni dependencias externas
- Usar `chrome.storage.local` para persistir datos (no localStorage en service workers)
- `chrome.runtime.sendMessage` para comunicación entre componentes

**Diseño del popup:**
- CSS propio, sin frameworks
- Ancho recomendado: 320–400px
- Diseño limpio y funcional, no minimalista extremo

### 5. Instruir la instalación

Al terminar, dar siempre estas instrucciones:
```
1. Abre Chrome → chrome://extensions/
2. Activa "Modo desarrollador" (esquina superior derecha)
3. Click en "Cargar extensión sin empaquetar"
4. Selecciona la carpeta [nombre-extension]
5. La extensión aparece en la barra de Chrome
```

## Reglas

- Código completo y funcional — nada de "aquí iría la lógica"
- Probar mentalmente el flujo antes de entregar (¿todos los archivos referenciados existen?)
- Si la extensión necesita permisos sensibles (tabs, history, cookies), advertirlo al usuario
- No usar `eval()` ni código dinámico inline (viola Content Security Policy de Chrome)
