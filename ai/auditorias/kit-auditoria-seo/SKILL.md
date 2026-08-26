---
name: auditoria-seo
description: Analiza el SEO completo de cualquier web y genera un informe visual HTML con puntuación y correcciones priorizadas por impacto.
version: 1.0.0
author: PalferIA
---

# Auditoría SEO

Cuando el usuario te dé una URL, analiza el SEO completo de esa web y genera un dashboard HTML con los resultados.

## Flujo

1. Pide la URL si no la tienes
2. Usa WebFetch para acceder a la web
3. Analiza en 8 categorías (puntúa 0–100 cada una):
   - **Meta tags**: title (largo, keyword), description (largo, keyword), canonical, robots
   - **Headings**: H1 único, jerarquía H1→H6, keywords en headings
   - **Imágenes**: atributos alt, lazy loading, formatos modernos (WebP/AVIF)
   - **Enlaces**: rotos, rel=noopener en externos, anclas descriptivas
   - **Open Graph y Twitter Cards**: og:title, og:description, og:image, twitter:card
   - **Schema / JSON-LD**: presencia, tipo correcto, datos válidos
   - **Técnico**: HTTPS, robots.txt, sitemap.xml, tiempo de respuesta
   - **Contenido**: palabras totales, ratio texto/HTML, keyword density
4. Genera el archivo HTML con nombre `auditoria-seo-[dominio].html`
5. Abre el archivo en el navegador con `open [archivo]`

## Formato del dashboard HTML

- Puntuación global 0–100 (media ponderada)
- Top 5 correcciones con impacto estimado y código exacto para aplicar
- Cards para las 8 categorías con puntuación, estado (verde/amarillo/rojo) y detalle
- Tabla técnica con todos los hallazgos

## Reglas

- Nunca inventar datos — todo lo que aparece en el informe debe venir del análisis real
- Si una URL falla, intentar con y sin www, y con y sin https
- El informe siempre se entrega como HTML, nunca como texto en el chat
- Ofrecer al final aplicar las correcciones si el usuario tiene acceso al código
