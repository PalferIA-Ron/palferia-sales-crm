---
name: prospeccion
description: "Encuentra clientes potenciales buscando negocios de un nicho, analizando su presencia digital y generando un informe con datos de contacto y oportunidades. Usa esta skill cuando el usuario quiera buscar clientes, hacer prospección, encontrar leads, analizar negocios de un sector, o buscar empresas a las que ofrecerles servicios. Triggers: 'buscar clientes', 'prospección', 'encontrar leads', 'lista de clientes potenciales', 'a quién le vendo', 'encontrar empresas de [sector]', 'buscar negocios en [ciudad]', 'analizar competencia', 'scraping de negocios'."
---

# Prospección de Clientes

Le dices un sector + ubicación y Claude busca negocios reales, analiza su presencia digital, puntúa la oportunidad y genera un informe con los mejores prospectos y sus datos de contacto.

**Regla fundamental: solo datos reales.** Cada negocio, teléfono, web y dato de contacto debe ser real y verificado. No inventes negocios ni datos de contacto.

---

## Paso 1 — Definir la búsqueda

Pregunta al usuario:
- **¿Qué tipo de negocio buscas?** (restaurantes, clínicas, gimnasios, abogados, agencias, tiendas...)
- **¿En qué ciudad o zona?** (Barcelona, Madrid centro, Valencia, una provincia entera...)
- **¿Qué servicio les vas a ofrecer?** — esto afecta cómo se puntúa la oportunidad (si vendes webs, un negocio sin web es oportunidad máxima; si vendes SEO, una web sin optimizar es la oportunidad)
- **¿Cuántos prospectos necesitas?** (10, 25, 50)
- **¿Es para COM-studio o ME-sport?**
  - **COM-studio** → negocios locales generales (fontanería, restaurantes, clínicas, comercios, gestorías, inmobiliarias...)
  - **ME-sport** → academias deportivas, gimnasios, clubes, centros de entrenamiento, escuelas de deporte

Guarda la respuesta como campo `proyecto` (`COM-studio` o `ME-sport`) en el JSON de salida.

---

## Paso 2 — Buscar negocios reales

Usa las herramientas disponibles para encontrar negocios reales. Orden de prioridad:

### Opción 1 — WebSearch (siempre disponible)

Busca en Google con queries específicas:
- `"[nicho] en [ciudad]"` — resultados orgánicos
- `"[nicho] [ciudad] teléfono"` — para encontrar datos de contacto
- `"[nicho] [ciudad] opiniones"` — Google Business results
- `site:paginasamarillas.es [nicho] [ciudad]` — directorio

Haz varias búsquedas con variaciones para acumular negocios únicos.

### Opción 2 — Firecrawl MCP (si está configurado)

Si tiene Firecrawl, scrapea directorios directamente:
- Páginas Amarillas / QDQ / Yelp
- Google Maps (resultados de búsqueda)
- Directorios específicos del sector

### Opción 3 — Playwright (si está instalado)

Navega a directorios y extrae listados de negocios con sus datos.

### Qué extraer de cada negocio

- **Nombre** del negocio
- **Web** (URL si tiene)
- **Teléfono**
- **Email** (si está visible)
- **Dirección**
- **Google Maps / Google Business** (si aparece)
- **Redes sociales** (Instagram, Facebook, etc.)

**Si no puedes encontrar suficientes negocios automáticamente**, dile al usuario cuántos encontraste y pregunta si quiere que busques de otra forma o si tiene URLs que quiera analizar directamente.

---

## Paso 3 — Analizar la presencia digital

Para cada negocio encontrado que tenga web, analízala con WebFetch:

### Checklist de análisis

- **¿Tiene web?** — si no tiene, oportunidad máxima para servicios de web
- **¿HTTPS?** — ¿tiene certificado SSL?
- **¿Responsive?** — ¿tiene meta viewport?
- **¿SEO básico?** — ¿tiene title, meta description, h1?
- **¿Velocidad?** — tiempo de respuesta del servidor (curl)
- **¿Redes sociales?** — buscar links a Instagram, Facebook, LinkedIn, etc. en la web
- **¿Google Business?** — ¿tiene ficha con reseñas?
- **¿Diseño moderno?** — ¿se ve como una web de 2024+ o parece de 2015?
- **¿Contenido?** — ¿tiene blog, páginas de servicios, fotos?

### Puntuación de oportunidad

Puntúa cada negocio de 0-100 según el servicio que ofrece el usuario:

**Si vende webs/diseño:**
- Sin web = 95-100
- Web antigua + sin responsive + sin HTTPS = 80-94
- Web aceptable pero fea/lenta = 50-79
- Web moderna = 0-49

**Si vende SEO:**
- Sin meta tags + sin h1 + sin content = 90-100
- SEO parcial (title pero sin description) = 60-89
- SEO básico cubierto = 30-59
- SEO bien hecho = 0-29

**Si vende marketing/redes:**
- Sin redes sociales = 90-100
- Redes con pocos seguidores/sin actividad = 60-89
- Redes activas pero sin estrategia = 30-59
- Marketing digital completo = 0-29

Adapta el scoring al servicio que ofrece el usuario.

---

## Paso 4 — Generar el informe HTML

Dashboard visual con todos los prospectos. Libertad creativa total en diseño.

### Contenido obligatorio

1. **Resumen ejecutivo** — Total encontrados, distribución por nivel de oportunidad (gráfico), top 5 recomendados

2. **Tabla de prospectos** — Ordenada por oportunidad, con:
   - Nombre del negocio (link a su web si tiene)
   - Teléfono y email (si encontrados)
   - Dirección
   - Score de oportunidad (barra visual de color)
   - Nivel digital (bajo/medio/alto con badge)
   - Problemas detectados (lista corta)
   - Link a Google Maps si está disponible

3. **Ficha detallada de los top 5-10** — Para los mejores prospectos:
   - Análisis completo de su presencia digital
   - 3 problemas concretos encontrados
   - Propuesta de valor personalizada para ese negocio
   - Mensaje de contacto en frío listo para enviar (personalizado con datos reales del negocio y problemas detectados)

4. **Estadísticas del nicho** — Vista general del sector:
   - % sin web
   - % sin HTTPS
   - % sin SEO
   - % sin redes sociales
   - Conclusión sobre la oportunidad del nicho

5. **Datos exportables** — Tabla de contactos con botón para copiar todos los emails/teléfonos

### Sobre los mensajes de contacto

Los mensajes deben ser:
- **Personalizados** con el nombre del negocio y un problema real encontrado
- **Concretos** — no genéricos, que el destinatario sienta que has mirado su web de verdad
- **Cortos** — máximo 5-6 líneas
- **Sin presión** — ofrecer valor, no vender agresivamente

---

## Paso 5 — Guardar archivos

- Guarda como `prospeccion-[nicho]-[ciudad].html`
- Guarda también `prospeccion-[nicho]-[ciudad].json` con los datos crudos
- El JSON debe seguir exactamente este esquema por prospecto:

```json
{
  "nombre": "Nombre del negocio",
  "municipio": "Ciudad",
  "sector": "Fontanería",
  "score": 28,
  "web": "https://ejemplo.com",
  "instagram": "@cuenta",
  "email": "info@ejemplo.com",
  "telefono": "+34961234567",
  "pain": "Sin WhatsApp, sin formulario presupuesto",
  "proyecto": "COM-studio",
  "semana": 1
}
```

---

## Paso 6 — Guardar en Supabase CRM

**Lee las credenciales del archivo `.env.local`** en el directorio raíz del proyecto `palferia-sales-crm`. Si no existe o `SUPABASE_SERVICE_KEY` dice `REEMPLAZAR_...`, avisa al usuario y salta este paso.

Para cada prospecto del JSON, ejecuta:

### 6.1 — Verificar si ya existe

```bash
curl -s "https://aqaiqmsypbwhgknbbmae.supabase.co/rest/v1/prospectos?nombre=eq.[NOMBRE]&municipio=eq.[MUNICIPIO]&select=id" \
  -H "apikey: $SUPABASE_SERVICE_KEY" \
  -H "Authorization: Bearer $SUPABASE_SERVICE_KEY"
```

- Si devuelve un array no vacío → prospecto ya existe, **saltar insert**, anotar como "ya existía"
- Si devuelve `[]` → continuar con el insert

### 6.2 — Insertar prospecto nuevo

```bash
curl -s -X POST "https://aqaiqmsypbwhgknbbmae.supabase.co/rest/v1/prospectos" \
  -H "apikey: $SUPABASE_SERVICE_KEY" \
  -H "Authorization: Bearer $SUPABASE_SERVICE_KEY" \
  -H "Content-Type: application/json" \
  -H "Prefer: return=representation" \
  -d '{
    "nombre":    "[nombre]",
    "municipio": "[municipio]",
    "sector":    "[sector]",
    "score":     [score],
    "web":       "[web o null]",
    "instagram": "[instagram o null]",
    "email":     "[email o null]",
    "telefono":  "[telefono o null]",
    "pain":      "[pain]",
    "proyecto":  "[COM-studio o ME-sport]",
    "semana":    [semana],
    "estado":    "identified"
  }'
```

Guarda el `id` devuelto por Supabase.

### 6.3 — Registrar en pipeline_log

```bash
curl -s -X POST "https://aqaiqmsypbwhgknbbmae.supabase.co/rest/v1/pipeline_log" \
  -H "apikey: $SUPABASE_SERVICE_KEY" \
  -H "Authorization: Bearer $SUPABASE_SERVICE_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "proyecto":          "[COM-studio o ME-sport]",
    "prospecto_id":      "[id devuelto en 6.2]",
    "prospecto_nombre":  "[nombre]",
    "accion":            "Identificado via kit-prospeccion v3",
    "resultado":         "Score [score]/100 — [pain]"
  }'
```

### 6.4 — Resumen final

Muestra al usuario:
```
✅ Supabase actualizado:
   • X prospectos insertados
   • Y ya existían (sin duplicar)
   • Z errores (detalle si los hay)
```

---

## Paso 7 — Presentar resultados

1. Cuántos negocios encontraste y analizaste
2. Distribución de oportunidades
3. Top 3 prospectos en una frase
4. Resumen de Supabase (del paso 6)
5. Pregunta si quiere profundizar en alguno o generar propuesta

No muestres precios sugeridos ni consejos de venta.
