from enum import Enum
from dataclasses import dataclass
from schema.game import GameSchema, GameMoveSchema, GameScoreSchema
from repository.game import GameRepo


class Choices(Enum):
    ROCK = 'ROCK'
    PAPER = 'PAPER'
    SCISSORS = 'SCISSORS'


@dataclass(frozen=True)
class User:
    name: str
    scrore: int


@dataclass(frozen=True)
class Game:
    player1: User
    player2: User


@dataclass(frozen=True)
class GameMove:
    player1: Choices
    player2: Choices
    game_id: int


@dataclass(frozen=True)
class GameScore:
    player1: int
    player2: int
    game_id: int


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
        return GameSchema().dump(game)

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
