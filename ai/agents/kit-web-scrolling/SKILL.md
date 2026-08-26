---
name: web-scrolling
description: Crea webs profesionales con animaciones de scroll para cualquier negocio. Usa datos reales del cliente y genera un HTML premium con efectos visuales avanzados.
version: 1.0.0
author: PalferIA
---

# Web Premium con Animaciones de Scroll

Crea webs profesionales con animaciones de scroll (scroll-triggered, parallax, reveal) para cualquier tipo de negocio.

## Datos que necesitas recopilar

Preguntar de forma conversacional (no como formulario):
1. **Nombre y sector del negocio**
2. **Servicios o productos que ofrece**
3. **Precios** (si los quiere mostrar)
4. **Datos de contacto** (email, teléfono, ubicación)
5. **Colores de marca** (si no tiene, Claude propone opciones acordes al sector)
6. **Fotos o vídeo** (si hay archivos en `assets/`, usarlos; si no, usar placeholders profesionales)
7. **Testimonios** (si los tiene)
8. **¿Quiere el efecto vídeo-scroll?** (si hay `assets/hero.mp4`)

Solo lo que no se puede deducir del sector y el nombre.

## Efecto vídeo con scroll (si hay `assets/hero.mp4`)

Si el usuario pide el efecto y tiene `assets/hero.mp4`:
- El vídeo avanza fotograma a fotograma sincronizado con el scroll del usuario
- Similar al efecto de Apple en sus páginas de producto
- Usar `<video>` con JavaScript que actualiza `currentTime` en base a `scrollY`

## Estructura de secciones (adaptar al sector)

**Siempre incluir:**
- Hero con headline fuerte + CTA principal
- Servicios/productos con cards animadas
- Propuesta de valor / diferenciadores
- Contacto con formulario o datos directos

**Incluir si hay datos:**
- Testimonios / casos de éxito
- Portfolio o galería
- Precios / tarifas
- Equipo / sobre nosotros
- FAQs

**Omitir** las secciones para las que no hay datos reales.

## Animaciones de scroll obligatorias

Implementar con JavaScript puro (Intersection Observer API):

- **Fade-in**: elementos aparecen al entrar en viewport
- **Slide-in**: elementos entran desde los lados
- **Stagger**: listas de elementos aparecen en cascada
- **Parallax suave**: en el hero (fondo se mueve más lento que el contenido)
- **Counter**: números que cuentan al aparecer (si hay estadísticas)

No usar librerías externas (GSAP, AOS, etc.) — JS puro.

## Estándares técnicos

- HTML5 semántico + CSS3 + JS ES2020
- Responsive: móvil-first (320px → 768px → 1200px+)
- Sin frameworks ni dependencias externas
- Tiempo de carga: todo inline en un solo archivo `.html`
- Formulario de contacto: con validación básica (no necesita backend para el HTML)

## Proceso de entrega

1. Generar el archivo `web-[nombre-negocio].html`
2. Guardarlo con Write
3. Abrirlo con `open web-[nombre-negocio].html`
4. Preguntar qué quiere cambiar e iterar hasta que esté satisfecho

## Reglas

- Solo usar datos reales del usuario — nunca inventar servicios, precios ni testimonios
- Si no hay fotos, usar CSS con gradientes/formas geométricas como placeholder — NO imágenes de Unsplash ni externas
- El CSS debe ser de nivel premium: variables CSS, transiciones suaves, tipografía cuidada
- Si el usuario quiere cambios, aplicarlos y volver a abrir el archivo
