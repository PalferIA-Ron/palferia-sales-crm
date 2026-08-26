---
name: auditoria-negocio-digital
description: Audita la presencia digital completa de un negocio: web, redes sociales, oferta, precios, embudo de ventas y reputación. Genera un informe HTML detallado.
version: 1.0.0
author: PalferIA
---

# Auditoría de Negocio Digital

Cuando el usuario quiera auditar su negocio digital, recoge los datos necesarios y genera un informe HTML completo con hallazgos y recomendaciones.

## Datos que necesitas recopilar

1. **URL de la web**
2. **Redes sociales** (Instagram, TikTok, LinkedIn, YouTube, Facebook — las que tenga)
3. **Qué vende y a qué precio**

## Flujo de análisis

### Siempre buscar información actualizada
Usa WebSearch y WebFetch para obtener datos reales antes de generar el informe. No usar conocimiento previo sobre el negocio.

### 1. Web
- UX y usabilidad (navegación, estructura, velocidad percibida)
- CTAs: cuántos, dónde están, si son claros
- Formularios: fricción, campos, confirmación
- Propuesta de valor: ¿está clara en los primeros 5 segundos?
- HTTPS, responsive, velocidad de carga

### 2. Redes sociales
Para cada red que tenga:
- Bio: ¿está completa y optimizada?
- Contenido: tipo, frecuencia, calidad
- Engagement: ratio likes/seguidores, comentarios
- Coherencia con la web y otras redes

### 3. Oferta y precios
- ¿Son claros o hay que buscarlos?
- ¿Son coherentes entre canales (web, Instagram, etc.)?
- ¿Están bien posicionados respecto al mercado?

### 4. Embudo de ventas
- ¿Cómo llegan los clientes? (SEO, redes, paid, referidos)
- ¿Dónde se pierde la gente en el proceso de compra?
- ¿Hay seguimiento post-contacto?

### 5. Reputación
- Reseñas en Google, Trustpilot, etc. (buscar con WebSearch)
- Testimonios publicados
- Menciones en prensa o blogs

### 6. Coherencia de marca
- Mensaje y tono consistentes entre todos los canales
- Paleta visual coherente
- Nombre y handle consistentes

### 7. Competencia (si el usuario proporciona competidores)
- Comparativa en los mismos criterios
- Qué hacen mejor y peor

## Formato de salida — OBLIGATORIO

**El informe siempre se entrega en HTML.** Nunca como texto en el chat.

- Nombre: `auditoria-negocio-[nombre].html`
- Guárdalo con Write y ábrelo con `open [archivo]`

### Secciones del HTML
- Puntuación global y por categoría (0–100)
- Hallazgos críticos (lo que hay que arreglar ya)
- Análisis por área con evidencias reales
- Top 10 acciones priorizadas por impacto/esfuerzo
- Comparativa con competidores (si aplica)

## Reglas

- Solo datos reales obtenidos en el análisis — nunca inventar métricas
- Si una URL no carga, indicarlo y continuar con lo que sí se puede analizar
- Priorizar siempre lo que más impacto tiene en ventas
