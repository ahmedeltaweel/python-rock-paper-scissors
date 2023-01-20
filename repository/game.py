import psycopg2
from lib.game import User, Game, GameScore


class GameRepo:
    def __init__(self, conn: psycopg2.connection) -> None:
        self.conn = conn

    def save_game(self, game: Game) -> int:
        _cursor = self.conn.cursor()
        saved_id = _cursor.execute(
            "INSERT INTO game (player1, player2, p1_score, p2_score) VALUES (%s, %s, %s, %s) returning id",
            (game.player1.name, game.player2.name, game.player1.scrore, game.player2.scrore))
        _cursor.close()

        return saved_id

    def retrieve_game(self, id: int) -> Game:
        _cursor = self.conn.cursor()
        _cursor.execute("SELECT * FROM game where id = %s", id)
        game = _cursor.fetchone()
        _cursor.close()
        return Game(
            player1=User(name=game['player1'], scrore=game['p1_score']),
            player2=User(name=game['player2'], scrore=game['p2_score'])
        )

    def update_game(self, move: GameScore) -> None:
        _cursor = self.conn.cursor()
        _cursor.execute(
            "Update game SET(p1_score, p2_score) VALUES (%s, %s) where id = %s",
            (move.player1, move.player2, move.game_id))
        _cursor.close()
