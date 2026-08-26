---
name: auditoria-meta-ads
description: Audita campañas de Facebook/Instagram Ads y sus landing pages. Detecta incoherencias, problemas de copy y oportunidades de mejora. Entrega un informe HTML.
version: 1.0.0
author: PalferIA
---

# Auditoría Meta Ads + Landing Pages

Cuando el usuario quiera auditar sus Meta Ads, solicita los datos necesarios y genera un informe HTML completo.

## Datos que necesitas recopilar

1. **Nombre de la página de Facebook o negocio** (para buscar en la Biblioteca de Meta)
2. **URL de la landing page** (si la tienen)
3. **Qué venden y a quién** (producto/servicio y público objetivo)

## Flujo de análisis

### 1. Buscar anuncios activos
- Usa WebFetch en `https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ES&q=[nombre-negocio]`
- Si no funciona directamente, busca con WebSearch: `site:facebook.com/ads/library [nombre-negocio]`
- Extrae: creatividades, copy, hooks, CTAs, formatos, tiempo activos

### 2. Analizar la landing page
- Usa WebFetch en la URL de la landing
- Evalúa: headline, propuesta de valor, social proof, formulario, estructura persuasiva
- Detecta: Facebook Pixel, eventos de conversión, Analytics

### 3. Analizar coherencia Ad ↔ Landing
- Message match: ¿el anuncio y la landing hablan de lo mismo?
- Oferta: ¿coincide lo que promete el anuncio con lo que ofrece la landing?
- Tono y visual: ¿son coherentes?

### 4. Evaluar el copy
- ¿Habla de beneficios o características?
- ¿Tiene hooks potentes en los primeros 3 segundos?
- ¿Los CTAs son claros y con urgencia?
- ¿Responde objeciones del cliente?

## Formato de salida — OBLIGATORIO

**Siempre genera un archivo HTML.** Nunca entregues el análisis solo como texto.

- Nombre: `auditoria-meta-ads-[nombre-negocio].html`
- Guárdalo con la herramienta Write
- Ábrelo con `open [archivo]`

### Secciones del HTML
- Resumen ejecutivo con puntuación global (0–100)
- Análisis de anuncios activos (creatividad, copy, hooks)
- Análisis de la landing page
- Puntuación de coherencia Ad ↔ Landing
- Top 5 mejoras con mayor impacto (con ejemplos de copy mejorado)
- Análisis de tracking (Pixel, Analytics)

## Reglas

- Solo analizar datos reales obtenidos con WebSearch/WebFetch
- Si no encuentra anuncios activos, indicarlo claramente y analizar solo la landing
- Proporcionar siempre ejemplos concretos de mejora, no solo recomendaciones genéricas
