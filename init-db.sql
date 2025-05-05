-- Habilitar a extensão pgvector
CREATE EXTENSION IF NOT EXISTS vector;

-- Configurar busca textual em português
CREATE TEXT SEARCH CONFIGURATION pt_br (COPY = portuguese);
ALTER TEXT SEARCH CONFIGURATION pt_br
    ALTER MAPPING FOR hword, hword_part, word
    WITH portuguese_stem;

-- Habilitar a extensão unaccent para busca sem acentos
CREATE EXTENSION IF NOT EXISTS unaccent;