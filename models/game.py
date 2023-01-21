from enum import Enum
from dataclasses import dataclass


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
