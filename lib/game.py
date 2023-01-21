
from models.game import Game, GameScore, User
from repository.game import GameRepo
from schema.game import GameMoveSchema, GameSchema, GameScoreSchema


class GameLib:
    def __init__(self, repo: GameRepo) -> int:
        self.repo = repo

    def start(self, game: GameSchema) -> int:
        game = Game(
            player1=User(
                name=game.player1.name,
                scrore=game.player1.score
            ),
            player2=User(
                name=game.player2.name,
                scrore=game.player2.score
            ),
        )
        return self.repo.save_game(game)

    def retrieve(self, id: int) -> GameSchema:
        game = self.repo.retrieve_game(id)
        return GameSchema().dumps(game)

    def score(self, score: GameScoreSchema) -> None:
        self.repo.update_game(GameScore(
            player1=score.player1,
            player2=score.player2,
            game_id=score.id
        ))

    def play(self, game_move: GameMoveSchema) -> str:
        if game_move.player1 == "ROCK" and game_move.player2 == "PAPER":
            return "Player 2"
        elif game_move.player1 == "PAPER" and game_move.player2 == "SCISSOR":
            return "Player 2"
        elif game_move.player1 == "SCISSOR" and game_move.player2 == "ROCK":
            return "Player 2"
        elif game_move.player1 == game_move.player2:
            return "Tie"
        else:
            return "Player 1"
