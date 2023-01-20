CREATE TABLE IF NOT EXISTS game (
    -- FIXME: use uuid
    id SERIAL PRIMARY KEY,
    player1 VARCHAR(255),
    player2 VARCHAR(255),
    p1_score INTEGER,
    p2_score INTEGER
);

CREATE INDEX CONCURRENTLY gmae_players_index ON game (player1, player2) using btree;