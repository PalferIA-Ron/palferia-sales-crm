# Planes y Precios — PalferIA

> **Fuente oficial actualizada:** `~/.claude/skills/kit-pricing-planes.md`
> Este archivo contiene los planes base. La skill global incluye además módulos adicionales
> (landing, SEO, GEO/AEO, Meta Ads, Google Ads, RRSS, ChatGPT Ads) con precios de mercado ES 2026.



## COM-studio — Negocios locales

### Inversión inicial (setup, pago único)

| Plan | Precio cliente | Coste interno | Floor mínimo | Qué incluye |
|------|---------------|---------------|-------------|-------------|
| **Vecino Digital** | 1.200 € | 550 € | 900 € | Superchatbot multicanal IA + landing SEO + WhatsApp Business + configuración |
| **Autopilot 30** | 3.100 € | 1.400 € | 2.400 € | CRM de ventas con IA + automatización de captación + integraciones + Vecino Digital incluido |
| **Socio Digital** | 4.900 € | 2.200 € | 3.800 € | Sistema omnicanal completo + agente de voz + multi-canal + Autopilot incluido |

### Cuota mensual (administración y mantenimiento)

| Plan | Precio cliente | Coste interno | Floor mínimo | Horas incluidas | Respuesta |
|------|---------------|---------------|-------------|-----------------|-----------|
| Básico | 250 €/mes | — | — | 1 h/mes | 48-72h |
| Profesional | 490 €/mes | — | — | 3 h/mes | 24-48h |
| Avanzado | 900 €/mes | — | — | 6 h/mes | 24h |
| Crítico | 1.500 €+/mes | — | — | bolsa amplia | prioritario |

**Regla clave:** El setup (inversión inicial) y la cuota mensual son contratos separados.
El setup se cobra una vez. La cuota mensual es recurrente e independiente.
Nunca mezclar ambos en el mismo número.

---

## ME-sport — Academias deportivas

### Inversión inicial

| Plan | Precio cliente | Coste interno | Qué incluye |
|------|---------------|---------------|-------------|
| **Sprint IA** | 1.800 € | 800 € | Agente WhatsApp + gestión de altas + recordatorios automatizados |
| **Equipo IA** | 3.500 € | 1.600 € | Sprint + CRM socios + agente de captación + reportes |
| **Liga IA** | 5.500 € | 2.500 € | Equipo + múltiples sedes + agente de voz + integración app |

### Cuota mensual

Igual que COM-studio. Usar los mismos planes de mantenimiento (Básico/Profesional/Avanzado/Crítico).

---

## Costes de infraestructura — ¿quién paga qué?

### Opción A — Cliente tiene su propio VPS y n8n (ideal)
- Cliente asume: hosting VPS, dominio, SSL, licencia n8n (si cloud)
- PalferIA asume: despliegue, configuración, mantenimiento técnico del sistema

### Opción B — Cliente quiere que PalferIA lo aloje (más común)
| Concepto | Coste mensual cliente | Notas |
|----------|----------------------|-------|
| Espacio en VPS PalferIA | 30–60 €/mes | Según recursos: RAM, CPU, almacenamiento |
| Subdominio en sales.palferia.me | incluido | Para propuestas y herramientas |
| Dominio propio del cliente | 10–15 €/año | El cliente lo contrata o lo gestionamos |
| SSL | incluido | Let's Encrypt automático via Traefik |

### Opción C — Instalación local (on-premise)
- Requiere: servidor local Windows/Linux del cliente, IP fija o VPN
- Coste adicional setup: +500–1.000 € por complejidad
- Limitación: sin acceso remoto sin VPN, backup responsabilidad del cliente
- Solo recomendable si hay restricciones legales de datos

### APIs — Siempre asumidas por el cliente (no incluidas en setup ni cuota)

| API | Coste estimado | Quién lo contrata |
|-----|---------------|-------------------|
| OpenAI / Claude (tokens) | 20–150 €/mes según volumen | Cliente — factura directa |
| WhatsApp Business API (Meta) | 0–80 €/mes según conversaciones | Cliente — cuenta Meta Business |
| Twilio / Vonage (voz) | según llamadas | Cliente — factura directa |
| Google Workspace (Gmail, Calendar) | 6–12 €/usuario/mes | Cliente — si no tiene |
| Dominio web | 10–15 €/año | Cliente o PalferIA lo gestiona |
| Hosting web cliente | 5–30 €/mes | Cliente — si quiere web propia |

**Frase clave para la conversación de venta:**
"Los costes de las APIs son como la factura de la luz de tu sistema IA — van directamente a tu nombre, son variables según el uso, y nosotros te configuramos exactamente cuánto vas a consumir."

---

## Tarifa de trabajo adicional (fuera de mantenimiento)

- Hora de desarrollo: **60 €/h**
- Presupuestado y aceptado por escrito antes de ejecutar

---

## Referencia precios mercado (Marketing Hackers)

| Pack | Setup | Mensual | Incluye |
|------|-------|---------|---------|
| Silver | 1.400 € | 97 € | IA WhatsApp + IA widget/funnel/web |
| Gold | 1.800 € | 97 € | Silver + IA call center |
| Black | 2.500 € | 247 € | Gold + 12 vídeos avatar IA + IA setter |
| Enterprise | 3.500–5.000 € | calc. por horas | hecho a medida |

Nuestros precios están alineados o ligeramente por encima en valor ofrecido.
