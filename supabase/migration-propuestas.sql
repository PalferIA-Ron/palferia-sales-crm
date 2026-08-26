-- ============================================================
--  PalferIA Sales CRM — Migración: tabla propuestas + campos web
--  Ejecutar en Supabase SQL Editor
-- ============================================================

-- Añadir campos que usa kit-prospeccion pero no estaban en prospectos
alter table prospectos
  add column if not exists web        text,
  add column if not exists instagram  text,
  add column if not exists pain       text,
  add column if not exists semana     integer default 1;

-- ── Tabla propuestas ─────────────────────────────────────────
create table if not exists propuestas (
  id              uuid primary key default gen_random_uuid(),
  created_at      timestamptz default now(),
  prospecto_id    uuid references prospectos(id) on delete cascade,
  slug            text unique not null,         -- token-url: uuid corto
  url             text,                         -- URL pública compartible
  titulo          text,
  estado          text default 'borrador'
                  check (estado in ('borrador','enviada','vista','aceptada','rechazada')),
  proyecto        text check (proyecto in ('COM-studio','ME-sport')),
  skills_usadas   text[],                       -- ['kit-auditoria-seo','kit-auditoria-negocio',...]
  notas_internas  text,                         -- para la vista ?interno
  fecha_envio     date
);

-- RLS
alter table propuestas enable row level security;

create policy "authenticated"
  on propuestas for all
  to authenticated
  using (true)
  with check (true);

-- Política para que kit-prospeccion (anon key) pueda INSERT en prospectos
-- Solo insert, nunca leer ni modificar
create policy "anon_insert_prospectos"
  on prospectos for insert
  to anon
  with check (true);

create policy "anon_insert_pipeline_log"
  on pipeline_log for insert
  to anon
  with check (true);
