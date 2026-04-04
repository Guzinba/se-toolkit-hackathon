-- Migration: Create notes table
-- Run this once on fresh DB or add to your init script

CREATE TABLE IF NOT EXISTS notes (
    id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    tags JSONB DEFAULT '[]'::jsonb,
    created_at TIMESTAMP DEFAULT NOW()
);

-- Индекс для быстрого поиска по тегам
CREATE INDEX IF NOT EXISTS idx_notes_tags ON notes USING GIN (tags);
-- Индекс по дате для сортировки
CREATE INDEX IF NOT EXISTS idx_notes_created ON notes (created_at DESC);
