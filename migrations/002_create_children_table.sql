CREATE TABLE IF NOT EXISTS children (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
    nickname VARCHAR(255) NOT NULL,
    birth_month INTEGER NOT NULL CHECK (birth_month BETWEEN 1 AND 12),
    birth_year INTEGER NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()
);

CREATE INDEX IF NOT EXISTS idx_children_user_id ON children(user_id);
