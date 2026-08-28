# PROMPT MAESTRO — DISEÑO DE APP WEB DE GESTIÓN DE PROYECTOS CON CLAUDE

## ROL

Actúa como **Product Manager Senior + UX/UI Designer + Software Architect + AI Agent Architect + Full-Stack Engineer**, especializado en construir aplicaciones web basadas en LLM para gestionar proyectos profesionales.

Quiero diseñar y desarrollar una **aplicación web para trabajar con Claude**, donde cada proyecto corresponda a un cliente y diferentes conversaciones/chat tengan funciones especializadas.

NO quiero una plataforma de automatización empresarial genérica.

NO quiero un sistema multiagente complejo.

NO quiero que todos los chats hagan de todo.

Quiero una aplicación sencilla, visual y organizada donde:

**cada chat tenga una responsabilidad concreta y entregue un resultado concreto para el proyecto.**

---

# 1. CONCEPTO GENERAL

La aplicación debe permitir crear un:

# PROYECTO / CLIENTE

Cada proyecto contiene toda la información disponible del cliente.

La información puede proceder de:

- Archivos `.md`
- Archivos `.html`
- Documentos `.doc`
- `.docx`
- PDFs si se decide incorporarlos
- URLs
- Websites completos
- Textos pegados manualmente
- Información introducida por el usuario

El sistema debe convertir toda esta información en un:

# CLIENT CONTEXT

Este contexto será la base común que utilizarán los diferentes chats.

---

# 2. FLUJO PRINCIPAL

La aplicación debe seguir este flujo:

```text
CREAR CLIENTE
      ↓
CARGAR INFORMACIÓN
      ↓
ANALIZAR INFORMACIÓN
      ↓
CREAR CONTEXTO DEL CLIENTE
      ↓
CREAR PROYECTO
      ↓
SELECCIONAR ÁREA DE TRABAJO
      ↓
ABRIR CHAT ESPECIALIZADO
      ↓
CLAUDE ANALIZA EL CONTEXTO
      ↓
GENERA ENTREGABLE
      ↓
GUARDAR ENTREGABLE
      ↓
REVISAR
      ↓
APROBAR
      ↓
INCORPORAR AL PROYECTO
```

---

# 3. PRINCIPIO FUNDAMENTAL

Cada chat debe responder a una pregunta:

> **¿Qué entregable concreto debe producir este chat para que el proyecto avance?**

No crear chats que simplemente "analicen".

Cada chat debe producir un resultado utilizable.

Ejemplo:

❌ Chat:

"Analiza el negocio."

✅ Chat:

"Genera el documento de Buyer Personas del cliente."

---

# 4. ESTRUCTURA DEL PROYECTO

Cada cliente tendrá:

```text
CLIENTE
│
├── Información original
│
├── Contexto del cliente
│
├── Investigación
│
├── Producto
│
├── Procesos
│
├── Automatizaciones
│
├── Agentes
│
├── Desarrollo
│
├── Soporte
│
├── Comercial
│
├── Marketing
│
└── Entregables
```

---

# 5. DASHBOARD DEL PROYECTO

La pantalla principal del cliente debe mostrar:

## Información del cliente

- Nombre.
- Empresa.
- Sector.
- País.
- Website.
- Descripción.
- Estado del proyecto.

## Fuentes disponibles

Mostrar:

```text
📄 12 archivos
🌐 3 websites
📝 4 documentos
🔗 8 URLs
```

## Progreso

Mostrar áreas:

```text
Discovery        ██████████ 100%

Producto         ███████░░░ 70%

Procesos         █████░░░░░ 50%

Automatización   ███░░░░░░░ 30%

Agentes          ██░░░░░░░░ 20%

Desarrollo       ░░░░░░░░░░ 0%

Marketing        ██████░░░░ 60%

Comercial        ████░░░░░░ 40%
```

---

# 6. ÁREAS DE TRABAJO

La aplicación debe organizar los chats por áreas.

## DISCOVERY

Chats:

### 01 — Analista del cliente

Entrega:

`client-analysis.md`

Debe analizar toda la información disponible.

---

### 02 — Investigador del mercado

Entrega:

`market-research.md`

---

### 03 — Investigador de competencia

Entrega:

`competitor-analysis.md`

---

### 04 — Buyer Persona

Entrega:

`buyer-personas.md`

---

# PRODUCTO

### 05 — Product Manager

Entrega:

`product-strategy.md`

---

### 06 — User Journey

Entrega:

`customer-journey.md`

---

### 07 — Requisitos

Entrega:

`product-requirements.md`

---

### 08 — Funcionalidades

Entrega:

`feature-specification.md`

---

# PROCESOS

### 09 — Business Process Analyst

Entrega:

`process-map.md`

---

### 10 — Process Optimization

Entrega:

`process-optimization.md`

---

### 11 — Automation Analyst

Entrega:

`automation-opportunities.md`

---

# AGENTES

### 12 — AI Agent Architect

Entrega:

`agent-strategy.md`

---

### 13 — Agent Designer

Entrega:

`agent-specifications.md`

---

### 14 — Multi-Agent Analyst

Entrega:

`multi-agent-analysis.md`

Solo debe recomendar multiagente cuando esté justificado.

---

# AUTOMATIZACIÓN

### 15 — Automation Architect

Entrega:

`automation-architecture.md`

Debe decidir entre:

- LCNC.
- RPA.
- DPA.
- BPA.
- IA.
- Agentes.
- Scripting.

---

# DESARROLLO

### 16 — Software Architect

Entrega:

`technical-architecture.md`

---

### 17 — Developer

Entrega:

`development-specification.md`

---

### 18 — QA Engineer

Entrega:

`testing-strategy.md`

---

# SOPORTE

### 19 — Technical Support

Entrega:

`support-strategy.md`

---

### 20 — Troubleshooting

Entrega:

`troubleshooting.md`

---

# COMERCIAL

### 21 — Sales Strategist

Entrega:

`sales-strategy.md`

---

### 22 — Sales Enablement

Entrega:

`sales-playbook.md`

---

### 23 — Pricing

Entrega:

`pricing-strategy.md`

---

# MARKETING

### 24 — Marketing Strategist

Entrega:

`marketing-strategy.md`

---

### 25 — Content Strategist

Entrega:

`content-strategy.md`

---

### 26 — SEO

Entrega:

`seo-strategy.md`

---

### 27 — Conversion / CRO

Entrega:

`conversion-strategy.md`

---

# DIRECCIÓN

### 28 — Project Manager

Entrega:

`project-plan.md`

---

### 29 — Strategic Advisor

Entrega:

`strategic-recommendations.md`

---

### 30 — Project Auditor

Entrega:

`project-audit.md`

Este chat debe analizar todos los documentos existentes y detectar:

- Contradicciones.
- Información faltante.
- Decisiones sin justificar.
- Riesgos.
- Duplicidades.
- Problemas de arquitectura.
- Problemas de producto.
- Problemas comerciales.

---

# 7. CONTEXTO COMPARTIDO

Todos los chats deben poder consultar el contexto del proyecto.

El contexto debe estar organizado en:

```text
CLIENT CONTEXT
│
├── identity
├── business
├── products
├── services
├── customers
├── market
├── competitors
├── processes
├── technology
├── automation
├── agents
├── marketing
├── sales
└── decisions
```

Pero el chat NO debe cargar indiscriminadamente toda la información.

Debe utilizar únicamente la información relevante para su tarea.

---

# 8. FUENTES DEL CLIENTE

El usuario debe poder subir:

## Archivos

- `.md`
- `.txt`
- `.html`
- `.doc`
- `.docx`
- `.pdf`

## URLs

Ejemplo:

```text
https://cliente.com
```

El sistema debe permitir analizar:

- Página principal.
- Servicios.
- Productos.
- About.
- Contacto.
- Blog.
- FAQs.
- Landing pages.

Cuando sea posible.

---

# 9. SOURCE REGISTRY

Cada fuente debe registrarse.

Ejemplo:

```json
{
  "id": "source_001",
  "type": "website",
  "url": "https://example.com",
  "title": "Website principal",
  "date_added": "2026-08-28",
  "status": "processed"
}
```

Para archivos:

```json
{
  "id": "source_002",
  "type": "markdown",
  "filename": "brief_cliente.md",
  "status": "processed"
}
```

---

# 10. TRAZABILIDAD

Claude debe poder indicar de dónde procede cada información importante.

Ejemplo:

```text
Información:
El cliente ofrece entrenamiento personal.

Fuente:
brief_cliente.md
```

O:

```text
Fuente:
https://cliente.com/servicios
```

Nunca presentar una inferencia como información proporcionada directamente por el cliente.

Diferenciar:

### CONFIRMADO

Información encontrada directamente.

### INFERIDO

Conclusión derivada de varias fuentes.

### PROPUESTO

Recomendación de Claude.

### PENDIENTE

Información que debe confirmar el cliente.

---

# 11. CHAT ESPECIALIZADO

Cada chat debe tener:

## SYSTEM ROLE

Define el rol.

## OBJECTIVE

Qué debe conseguir.

## INPUTS

Qué información necesita.

## CONTEXT

Qué documentos puede consultar.

## PROCESS

Cómo debe analizar.

## OUTPUT

Qué archivo debe producir.

## VALIDATION

Cómo comprobar que el resultado es correcto.

---

# 12. PLANTILLA DE CHAT

Todos los chats deben seguir esta estructura conceptual:

```text
ROL
↓
OBJETIVO
↓
CONTEXTO
↓
FUENTES
↓
ANÁLISIS
↓
DECISIONES
↓
ENTREGABLE
↓
VALIDACIÓN
```

---

# 13. ENTREGABLES

Cada conversación debe poder producir un documento.

Ejemplo:

```text
Chat:
Product Manager

Output:
docs/product/product-strategy.md
```

El usuario debe poder:

- Ver.
- Editar.
- Aprobar.
- Regenerar.
- Comparar versiones.
- Descargar/exportar.
- Enviar al siguiente chat.

---

# 14. ESTADOS DEL DOCUMENTO

Cada entregable tendrá:

```text
DRAFT
↓
REVIEW
↓
CHANGES REQUESTED
↓
APPROVED
↓
FINAL
```

---

# 15. DEPENDENCIAS ENTRE CHATS

Los chats pueden depender de entregables anteriores.

Ejemplo:

```text
Analista cliente
       ↓
Market Research
       ↓
Product Manager
       ↓
Process Analyst
       ↓
Automation Architect
       ↓
Agent Architect
       ↓
Software Architect
       ↓
Developer
```

Pero el usuario debe poder abrir cualquier chat.

Si faltan documentos necesarios:

**el chat debe indicarlo y trabajar con la información disponible.**

No bloquear innecesariamente al usuario.

---

# 16. INTERFAZ DEL CHAT

Cada conversación debe mostrar:

### Contexto utilizado

```text
✓ client-analysis.md
✓ market-research.md
✓ website-home.html
✓ services.md
```

### Entregable esperado

```text
product-strategy.md
```

### Estado

```text
DRAFT
```

### Acciones

- Generar.
- Regenerar.
- Revisar.
- Aprobar.
- Guardar.
- Exportar.

---

# 17. SIDEBAR

Diseña una interfaz tipo workspace.

```text
┌─────────────────────────────────────────────┐
│ LOGO                     CLIENTE             │
├───────────────┬─────────────────────────────┤
│               │                             │
│ PROYECTO      │      CHAT                   │
│               │                             │
│ Discovery     │      conversación           │
│ Producto      │                             │
│ Procesos      │                             │
│ Automatización│                             │
│ Agentes       │                             │
│ Desarrollo    │                             │
│ Soporte       │                             │
│ Comercial     │                             │
│ Marketing     │                             │
│               │                             │
│ Documentos    │                             │
│ Fuentes       │                             │
│               │                             │
│ Configuración │                             │
└───────────────┴─────────────────────────────┘
```

---

# 18. DOCUMENTOS

Crear un explorador:

```text
DOCUMENTOS

📁 Discovery
   ├── client-analysis.md
   ├── market-research.md
   └── competitor-analysis.md

📁 Product
   ├── product-strategy.md
   └── product-requirements.md

📁 Automation
   ├── automation-opportunities.md
   └── automation-architecture.md

📁 Agents
   ├── agent-strategy.md
   └── agent-specifications.md
```

---

# 19. VERSIONADO

Cada documento debe mantener versiones.

Ejemplo:

```text
product-strategy.md

v1
v2
v3
FINAL
```

Registrar:

- Autor.
- Fecha.
- Motivo del cambio.
- Chat que produjo el cambio.

---

# 20. BASE DE CONOCIMIENTO

El sistema debe poder crear una base de conocimiento del cliente.

No es necesario convertir inicialmente todo en un sistema RAG complejo.

Diseña una arquitectura que permita evolucionar posteriormente hacia:

- Embeddings.
- Vector database.
- Semantic search.
- Hybrid search.
- Retrieval.
- Document chunks.

Pero para el MVP prioriza simplicidad.

---

# 21. ARQUITECTURA DE LA APLICACIÓN

Propón una arquitectura moderna.

Por defecto evalúa:

### Frontend

- Next.js
- React
- TypeScript
- Tailwind CSS

### Backend

Puede utilizar:

- Next.js API routes.
- Node.js.
- Python cuando sea necesario.

### Database

Evalúa:

- PostgreSQL.
- SQLite para desarrollo local.

### Storage

- Local storage para MVP.
- S3 compatible posteriormente.

### LLM

Diseña una capa abstracta:

```text
LLM Provider
      ↓
LLM Service
      ↓
Chat
      ↓
Specialized Prompt
```

No acoples toda la aplicación directamente a un único proveedor.

---

# 22. CLAUDE

La aplicación debe estar especialmente preparada para trabajar con Claude.

Diseña:

```text
Claude Service
│
├── Context Builder
├── Prompt Manager
├── Chat Manager
├── Document Manager
├── Output Manager
└── Validation Manager
```

---

# 23. PROMPT MANAGER

Los prompts de los chats deben estar separados del código.

Ejemplo:

```text
prompts/
├── discovery/
├── product/
├── processes/
├── automation/
├── agents/
├── development/
├── support/
├── commercial/
└── marketing/
```

Cada prompt debe poder versionarse.

---

# 24. ESTRUCTURA DEL PROYECTO LOCAL

Genera una estructura preparada para:

**VS Code + Claude Code + Git**

Propuesta:

```text
claude-project-manager/
│
├── CLAUDE.md
├── README.md
├── package.json
├── .env.example
├── .gitignore
│
├── app/
│   ├── dashboard/
│   ├── projects/
│   ├── clients/
│   ├── chats/
│   ├── documents/
│   ├── sources/
│   └── settings/
│
├── components/
│   ├── ui/
│   ├── chat/
│   ├── project/
│   ├── documents/
│   ├── sources/
│   └── dashboard/
│
├── lib/
│   ├── claude/
│   ├── documents/
│   ├── sources/
│   ├── projects/
│   ├── prompts/
│   └── database/
│
├── prompts/
│   ├── discovery/
│   ├── product/
│   ├── processes/
│   ├── automation/
│   ├── agents/
│   ├── development/
│   ├── support/
│   ├── commercial/
│   ├── marketing/
│   └── management/
│
├── docs/
│
├── data/
│   ├── projects/
│   ├── uploads/
│   └── outputs/
│
├── tests/
│
└── scripts/
```

Adapta esta estructura al stack elegido.

---

# 25. MODELO DE DATOS

Diseña como mínimo las entidades:

```text
User
Project
Client
Source
Document
Chat
ChatMessage
Prompt
Deliverable
Version
Decision
Task
```

Relaciones:

```text
Client
  ↓
Project
  ↓
Sources
Documents
Chats
Deliverables
Decisions
Tasks
```

---

# 26. CREACIÓN DE PROYECTO

El usuario debe poder:

1. Crear cliente.
2. Introducir información básica.
3. Subir archivos.
4. Añadir URLs.
5. Procesar información.
6. Crear contexto.
7. Revisar contexto.
8. Comenzar proyecto.

---

# 27. IMPORTACIÓN DE WEBSITE

Diseña un módulo que permita:

```text
URL
 ↓
Crawler
 ↓
Pages
 ↓
Content extraction
 ↓
Clean text
 ↓
Source registry
 ↓
Client context
```

Debe controlar:

- URLs duplicadas.
- Páginas irrelevantes.
- Límites de profundidad.
- Errores.
- Tiempo de espera.
- Robots.txt cuando corresponda.
- Rate limits.

---

# 28. PROCESAMIENTO DE DOCUMENTOS

Pipeline:

```text
UPLOAD
 ↓
FILE VALIDATION
 ↓
TEXT EXTRACTION
 ↓
NORMALIZATION
 ↓
METADATA
 ↓
CHUNKING
 ↓
INDEX
 ↓
AVAILABLE TO CHAT
```

---

# 29. CONTEXTO DEL CHAT

Cada chat debe construir dinámicamente el contexto.

Ejemplo:

```text
SYSTEM PROMPT
+
CLIENT PROFILE
+
RELEVANT SOURCES
+
PREVIOUS APPROVED DELIVERABLES
+
USER REQUEST
```

No enviar siempre todos los documentos.

---

# 30. REGLAS DE CONTEXTO

Prioridad:

### Nivel 1

Información explícita proporcionada por el cliente.

### Nivel 2

Documentos aprobados del proyecto.

### Nivel 3

Investigación externa.

### Nivel 4

Inferencias de Claude.

### Nivel 5

Recomendaciones.

Nunca mezclar estos niveles sin identificarlos.

---

# 31. OUTPUT STRUCTURED

Cada chat debe devolver:

```json
{
  "status": "draft",
  "summary": "...",
  "deliverable": {
    "filename": "product-strategy.md",
    "content": "..."
  },
  "sources_used": [],
  "assumptions": [],
  "open_questions": [],
  "recommendations": []
}
```

---

# 32. CONTROL DE CALIDAD

Antes de guardar un entregable Claude debe comprobar:

- ¿Utilizó las fuentes disponibles?
- ¿Existen contradicciones?
- ¿Hay información inventada?
- ¿Hay supuestos?
- ¿Hay información pendiente?
- ¿El documento cumple su objetivo?
- ¿Es coherente con documentos aprobados?

---

# 33. PROJECT MEMORY

Cada proyecto debe tener una memoria estructurada.

Ejemplo:

```text
project-memory/
├── client-profile.md
├── business-model.md
├── products.md
├── customers.md
├── market.md
├── technology.md
├── decisions.md
├── assumptions.md
└── open-questions.md
```

Solo la información validada debe convertirse en memoria oficial.

---

# 34. DECISION LOG

Crear:

`decisions.md`

Registrar:

```text
Decision
Date
Area
Context
Options
Decision
Reason
Impact
Approved by
```

---

# 35. OPEN QUESTIONS

Crear:

`open-questions.md`

Clasificar:

- Cliente.
- Producto.
- Tecnología.
- Legal.
- Comercial.
- Marketing.
- Desarrollo.

---

# 36. MVP

No intentes desarrollar todas las funcionalidades inicialmente.

Define un MVP con:

### 1.

Crear proyecto.

### 2.

Crear cliente.

### 3.

Subir documentos.

### 4.

Añadir URL.

### 5.

Procesar fuentes.

### 6.

Crear contexto.

### 7.

Seleccionar chat.

### 8.

Conversar con Claude.

### 9.

Generar Markdown.

### 10.

Guardar entregable.

### 11.

Versionar documento.

### 12.

Aprobar documento.

---

# 37. FASES POSTERIORES

Después del MVP:

## V2

- Búsqueda semántica.
- RAG.
- Vector DB.
- Comparación de versiones.
- Mejor gestión de fuentes.

## V3

- Automatización de workflows.
- Integraciones.
- Exportación avanzada.
- Colaboración.

## V4

- Agentes.
- Ejecución automática.
- Workflows autónomos.

No implementar estas funcionalidades antes de validar que son necesarias.

---

# 38. REGLAS PARA CLAUDE CODE

El proyecto debe incluir un `CLAUDE.md`.

Claude Code debe:

1. Leer `CLAUDE.md`.
2. Comprender la arquitectura.
3. Revisar documentación existente.
4. No modificar arquitectura sin justificarlo.
5. No eliminar funcionalidades existentes sin autorización.
6. Mantener TypeScript tipado.
7. Crear tests.
8. Actualizar documentación cuando cambie arquitectura.
9. Mantener separación entre UI, lógica y servicios.
10. No introducir dependencias innecesarias.
11. Mantener seguridad de las API keys.
12. No guardar secretos en Git.

---

# 39. EXPERIENCIA DE USUARIO

La aplicación debe sentirse como:

**Workspace profesional de proyectos + AI workspace + gestor documental.**

Debe evitar sentirse como:

- ChatGPT genérico.
- Un CRM.
- Un gestor de tareas.
- Una plataforma de RPA.

El chat es importante, pero el verdadero producto es:

**EL PROYECTO + SU CONTEXTO + SUS DOCUMENTOS + SUS ENTREGABLES.**

---

# 40. RESULTADO QUE QUIERO DE TI

A partir de este prompt debes actuar como Product Manager y Arquitecto del proyecto.

Antes de escribir código:

## FASE 1

Define:

- Product Vision.
- Problema.
- Usuarios.
- Casos de uso.
- User Stories.
- MVP.

## FASE 2

Define:

- UX.
- Pantallas.
- Navegación.
- Componentes.
- Flujos.

## FASE 3

Define:

- Arquitectura.
- Stack.
- Base de datos.
- Gestión documental.
- Integración Claude.
- Gestión de prompts.

## FASE 4

Define:

- Estructura de carpetas.
- Modelos.
- APIs.
- Servicios.
- Componentes.

## FASE 5

Crea:

- `README.md`
- `CLAUDE.md`
- documentación técnica
- prompts iniciales
- esquema de base de datos
- roadmap

## FASE 6

Divide el desarrollo en tareas pequeñas y ejecutables por Claude Code.

Cada tarea debe indicar:

```text
TASK ID
OBJECTIVE
FILES
DEPENDENCIES
IMPLEMENTATION
ACCEPTANCE CRITERIA
TESTS
```

---

# PRINCIPIO FINAL

No construyas una aplicación donde Claude simplemente responda preguntas.

Construye una aplicación donde:

```text
CLIENTE
   ↓
FUENTES
   ↓
CONTEXTO
   ↓
CHAT ESPECIALIZADO
   ↓
ENTREGABLE
   ↓
VALIDACIÓN
   ↓
MEMORIA DEL PROYECTO
   ↓
SIGUIENTE CHAT
```

Cada conversación debe hacer avanzar el proyecto.

Cada chat debe tener una responsabilidad.

Cada responsabilidad debe producir un entregable.

Cada entregable aprobado debe alimentar el contexto del proyecto.

El resultado final debe ser un **workspace de inteligencia de proyectos basado en Claude**, preparado para funcionar inicialmente en local mediante VS Code + Claude Code y poder evolucionar posteriormente a una aplicación web multiusuario.