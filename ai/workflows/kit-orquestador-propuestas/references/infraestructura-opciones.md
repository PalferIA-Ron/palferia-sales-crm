# Opciones de Infraestructura — Decisor para Propuestas

## Árbol de decisión

```
¿El cliente ya tiene VPS con n8n instalado?
├── SÍ → Opción A: instalamos en su infraestructura
│         Setup normal. Sin coste adicional de hosting.
│
└── NO → ¿Quiere contratar su propio servidor?
         ├── SÍ (DIY) → Opción A asistida
         │   Le recomendamos: Hostinger VPS Basic 4GB (5-8€/mes)
         │   Le configuramos nosotros. Coste adicional setup: +200€
         │
         └── NO (prefiere que lo gestionemos todo)
             ├── Opción B: en VPS PalferIA → +30-60€/mes en cuota
             └── ¿Tiene restricciones de datos/legal?
                 └── SÍ → Opción C: instalación local → +500-1000€ setup
```

## Descripción de cada opción

### Opción A — Infraestructura propia del cliente
**Requiere:** VPS Linux con acceso SSH, n8n instalado (o lo instalamos)
**Responsabilidad hosting:** 100% cliente
**Ideal para:** clientes con equipo técnico o que ya tienen servidor
**Coste adicional:** 0€ (ya lo tienen)
**En propuesta:** no mencionar hosting — el cliente ya lo asume

### Opción B — Alojado en VPS PalferIA (más común)
**Requiere:** nada del cliente — lo gestionamos todo
**Responsabilidad hosting:** PalferIA
**Ideal para:** negocios locales sin equipo técnico (mayoría COM-studio y ME-sport)
**Coste adicional:** 30–60€/mes incluido en cuota mensual o cobrado aparte
**En propuesta:** mencionar como "servicio gestionado — sin preocupaciones técnicas"
**Incluye:** subdominio, SSL, backups semanales, monitorización básica

### Opción C — Instalación local (on-premise)
**Requiere:** PC/servidor Windows o Linux siempre encendido, IP fija o túnel ngrok
**Responsabilidad hosting:** cliente (su local/oficina)
**Ideal para:** clientes con datos sensibles (clínicas, asesorías)
**Coste adicional:** +500–1.000€ en setup por complejidad extra
**Limitaciones:** sin acceso remoto sin VPN, cliente responsable de backups y energía
**En propuesta:** solo si el cliente lo pide — no es la opción por defecto

## Preguntas clave para el setter tool

1. ¿Tienes algún servidor o VPS contratado actualmente?
2. ¿Tienes n8n instalado? ¿En qué URL?
3. ¿Tienes dominio propio? ¿Con qué proveedor?
4. ¿Hay alguna restricción legal sobre dónde deben vivir tus datos?
5. ¿Tienes alguien técnico en tu equipo que gestione servidores?

## Frases para la conversación de venta

- "Nosotros nos encargamos de todo el tema técnico — tú no tocas ningún servidor."
- "El sistema vive en la nube, 24/7, sin que tengas que hacer nada."
- "Si prefieres que todo quede en tu propio servidor, lo instalamos allí también."
