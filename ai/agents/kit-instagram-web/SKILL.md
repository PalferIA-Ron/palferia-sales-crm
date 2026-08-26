---
name: instagram-a-web
description: Convierte un perfil de Instagram en una web de marca personal profesional. Extrae datos reales del perfil, suma seguidores de otras redes y genera un HTML premium.
version: 1.0.0
author: PalferIA
---

# Instagram → Web Profesional

Convierte un perfil de Instagram en una web de marca personal profesional usando datos reales.

## Datos a recopilar

**Automáticamente (via WebFetch/Playwright):**
- Foto de perfil, bio, número de seguidores, posts destacados
- Presencia en otras redes (Threads, TikTok, YouTube, LinkedIn)
- Testimonios publicados en redes o webs

**Preguntar al usuario (solo lo que no se puede obtener):**
- ¿A qué te dedicas y qué servicios ofreces?
- ¿Cuál es tu email de contacto?
- ¿Tienes colores de marca? (si no, Claude propone opciones)
- ¿Hay algo más que quieras destacar en la web?

## Verificar Node.js

```bash
node --version 2>/dev/null && echo "Node.js OK" || echo "NO_NODE"
```

Si no tiene Node.js: pedir los datos manualmente en lugar de hacer scraping automático.
Si tiene Node.js: instalar Playwright y acceder al perfil automáticamente.

## Flujo de generación

### 1. Obtener datos del perfil
- WebFetch/Playwright en `https://www.instagram.com/[handle]/`
- Extraer: foto, bio, seguidores, siguiendo, número de posts
- Descargar hasta 9 fotos recientes para el mini-grid

### 2. Buscar en otras redes
Buscar con WebSearch:
- `[handle] site:tiktok.com` → seguidores TikTok
- `[handle] site:youtube.com` → suscriptores
- `[handle] site:linkedin.com` → conexiones
- `[handle] site:threads.net` → seguidores Threads

Sumar todos para mostrar "seguidores totales".

### 3. Buscar testimonios
- WebSearch: `"[nombre]" testimonios OR reseñas OR "me ayudó" OR "recomiendo"`
- Si no hay en redes, omitir la sección de testimonios

### 4. Generar la web HTML

Archivo: `web-[handle].html`

**Secciones obligatorias:**
- **Hero**: foto de perfil, nombre, título profesional, bio, botón CTA
- **Stats**: seguidores totales de todas las plataformas, número de posts
- **Mini-grid Instagram**: 6–9 fotos reales del perfil
- **Servicios**: lo que ofrece el usuario
- **Sobre mí**: historia/propuesta de valor
- **Contacto**: email + links a redes sociales

**Secciones opcionales (incluir si hay datos):**
- Testimonios reales
- Portfolio o trabajos destacados
- Press/menciones

**Estilo:**
- Diseño premium adaptado al tipo de marca (fotógrafo, coach, influencer, consultor...)
- Responsive (móvil, tablet, escritorio)
- Colores de marca del usuario o paleta propuesta por Claude
- Sin librerías externas — HTML/CSS/JS puro

### 5. Guardar y abrir
- Guardar con Write
- Abrir con `open web-[handle].html`
- Preguntar qué quiere cambiar e iterar

## Reglas

- Solo usar datos reales — nunca inventar seguidores, testimonios ni servicios
- Si una imagen de Instagram no carga externamente, usar placeholder con la URL original como data-src
- Si el perfil es privado o no carga, pedir los datos manualmente al usuario
- El resultado final es el HTML, no texto en el chat
