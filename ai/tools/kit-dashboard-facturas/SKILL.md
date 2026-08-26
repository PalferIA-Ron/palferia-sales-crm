---
name: dashboard-facturas
description: Lee facturas PDF y genera un dashboard HTML visual con análisis financiero completo: ingresos, gastos, IVA trimestral, balance, evolución mensual y top clientes.
version: 1.0.0
author: PalferIA
---

# Dashboard de Facturas

Lee facturas PDF locales y genera un dashboard HTML con el análisis financiero completo del negocio.

## Estructura de carpetas esperada

```
facturas/
├── ingresos/    ← facturas que emite el usuario (lo que cobra)
└── gastos/      ← facturas que recibe el usuario (lo que paga)
```

Si el usuario solo tiene ingresos, pueden ir todas en `facturas/ingresos/`.

## Flujo

### 1. Verificar que hay facturas
- Comprobar que existen PDFs en `facturas/ingresos/` y/o `facturas/gastos/`
- Listar los archivos encontrados antes de empezar

### 2. Leer cada factura PDF
Para cada PDF, extraer con la herramienta Read:
- Fecha de emisión
- Número de factura
- Emisor (nombre, NIF/CIF)
- Receptor (nombre, NIF/CIF)
- Concepto / descripción
- Base imponible
- % IVA y cuota de IVA
- % IRPF y retención (si aplica)
- Total factura

### 3. Calcular métricas

**Ingresos:**
- Facturación total del período
- IVA repercutido (a declarar)
- IRPF retenido
- Base imponible total
- Evolución mensual
- Top 5 clientes por facturación

**Gastos:**
- Gasto total del período
- IVA soportado (deducible)
- Evolución mensual
- Top 5 proveedores por gasto

**Balance:**
- Resultado bruto (ingresos - gastos)
- IVA a pagar/devolver por trimestre (IVA repercutido - IVA soportado)
- Estimación IRPF anual

### 4. Generar el dashboard HTML

- Nombre: `dashboard-facturas-[año].html`
- Guardar con Write y abrir con `open [archivo]`

### Secciones del dashboard
- KPIs principales: facturación total, gastos, beneficio, IVA a pagar
- Gráfico de barras: evolución mensual de ingresos vs gastos
- Tabla de IVA trimestral (T1, T2, T3, T4)
- Top clientes y top proveedores
- Listado completo de facturas con filtros

### 5. Guardar datos en JSON
Exportar todos los datos extraídos a `facturas_datos.json` para uso en otras herramientas.

## Reglas

- Procesar solo datos reales de las facturas — nunca inventar importes
- Si un PDF no se puede leer o los datos son ambiguos, indicarlo en el informe y pedir confirmación al usuario
- Todos los cálculos se hacen localmente — ningún dato sale del ordenador
- Si falta información en una factura (ej: no tiene IVA desglosado), anotarlo como pendiente de revisión
