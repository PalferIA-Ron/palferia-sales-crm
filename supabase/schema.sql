-- ============================================================
--  PalferIA Sales CRM — Database Schema
--  Run this in the Supabase SQL Editor (once, on a fresh project)
-- ============================================================

-- prospectos
create table if not exists prospectos (
  id              uuid primary key default gen_random_uuid(),
  created_at      timestamptz default now(),
  nombre          text not null,
  municipio       text,
  sector          text,
  score           integer check (score >= 0 and score <= 100),
  estado          text default 'identified'
                  check (estado in (
                    'identified','contacted','waiting','call',
                    'proposal','negotiating','closed','discarded','alternative'
                  )),
  proyecto        text check (proyecto in ('COM-studio','ME-sport')),
  email           text,
  telefono        text,
  socios_est      text,
  ultimo_contacto date,
  proxima_accion  text,
  notas           text
);

-- pipeline_log
create table if not exists pipeline_log (
  id                uuid primary key default gen_random_uuid(),
  created_at        timestamptz default now(),
  fecha             date default current_date,
  proyecto          text,
  prospecto_id      uuid references prospectos(id) on delete set null,
  prospecto_nombre  text,
  accion            text,
  resultado         text
);

-- mensajes_whatsapp
create table if not exists mensajes_whatsapp (
  id           uuid primary key default gen_random_uuid(),
  created_at   timestamptz default now(),
  prospecto_id uuid references prospectos(id) on delete cascade,
  session_id   text,
  telefono     text,
  direccion    text check (direccion in ('outbound','inbound')),
  contenido    text,
  timestamp_wa timestamptz default now()
);

-- ── Row Level Security ────────────────────────────────────────
alter table prospectos        enable row level security;
alter table pipeline_log      enable row level security;
alter table mensajes_whatsapp enable row level security;

create policy "authenticated"
  on prospectos for all
  to authenticated
  using (true)
  with check (true);

create policy "authenticated"
  on pipeline_log for all
  to authenticated
  using (true)
  with check (true);

create policy "authenticated"
  on mensajes_whatsapp for all
  to authenticated
  using (true)
  with check (true);
