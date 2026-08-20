-- ============================================================
--  PalferIA Sales CRM — Seed Data (17 prospects)
--  Run AFTER schema.sql
-- ============================================================

insert into prospectos
  (nombre, municipio, sector, score, estado, proyecto, socios_est, ultimo_contacto)
values

  -- ── COM-studio ───────────────────────────────────────────

  (
    'Cortinajes Valls & París',
    'Godella',
    'Decoración',
    33,
    'waiting',
    'COM-studio',
    null,
    '2026-08-20'
  ),

  (
    'Romaib Fontaneros',
    'Paterna',
    'Fontanería',
    28,
    'waiting',
    'COM-studio',
    null,
    '2026-08-20'
  ),

  (
    'Fisioterapia Bienestar',
    'Paterna',
    'Fisioterapia',
    35,
    'waiting',
    'COM-studio',
    null,
    '2026-08-20'
  ),

  (
    'Masía Rocafort',
    'Rocafort',
    'Restaurante',
    35,
    'waiting',
    'COM-studio',
    null,
    '2026-08-20'
  ),

  (
    'In English',
    'Burjassot',
    'Academia Idiomas',
    62,
    'identified',
    'COM-studio',
    null,
    null
  ),

  (
    'Orquisato Floristería',
    'Burjassot',
    'Floristería',
    42,
    'identified',
    'COM-studio',
    null,
    null
  ),

  (
    'Talleres Godella',
    'Godella',
    'Automoción',
    28,
    'identified',
    'COM-studio',
    null,
    null
  ),

  (
    'Academia Oposiciones Valencia',
    'Paterna',
    'Formación',
    45,
    'identified',
    'COM-studio',
    null,
    null
  ),

  (
    'Inmobiliaria Moncada',
    'Moncada',
    'Inmobiliaria',
    42,
    'identified',
    'COM-studio',
    null,
    null
  ),

  (
    'Baker Street Panadería',
    'Burjassot',
    'Alimentación',
    28,
    'identified',
    'COM-studio',
    null,
    null
  ),

  (
    'Clínica Dental Moncada',
    'Moncada',
    'Odontología',
    42,
    'identified',
    'COM-studio',
    null,
    null
  ),

  -- ── ME-sport ─────────────────────────────────────────────

  (
    'Estudio Vitale',
    'Burjassot',
    'Pilates / Yoga',
    28,
    'waiting',
    'ME-sport',
    '50-80 socios',
    '2026-08-20'
  ),

  (
    'Dojo Hikari Valencia',
    'Campanar',
    'Artes Marciales',
    35,
    'waiting',
    'ME-sport',
    '100-200 socios',
    '2026-08-20'
  ),

  (
    'DF Swimming Team',
    'Valencia',
    'Natación',
    35,
    'waiting',
    'ME-sport',
    '200+ socios',
    '2026-08-20'
  ),

  (
    'CrossFit Taronja Moncada',
    'Moncada',
    'CrossFit',
    35,
    'alternative',
    'ME-sport',
    '50-100 socios',
    null
  ),

  (
    'B-Phulness',
    'Paterna',
    'Yoga / Pilates',
    35,
    'waiting',
    'ME-sport',
    '30-60 socios',
    '2026-08-20'
  ),

  (
    'Pádel Valencia Horta Nord',
    'Albalat dels Sorells',
    'Pádel',
    42,
    'identified',
    'ME-sport',
    '200+',
    null
  );
