-- migrate:up
CREATE TABLE IF NOT EXISTS game (
    -- FIXME: use uuid
    id SERIAL PRIMARY KEY,
    player1 VARCHAR(255),
    player2 VARCHAR(255),
    p1_score INTEGER,
    p2_score INTEGER
);

CREATE INDEX gmae_players_index ON game using btree (player1, player2);

insert into game (player1, player2, p1_score, p2_score) values ('john', 'doh', 1,2);

-- migrate:down