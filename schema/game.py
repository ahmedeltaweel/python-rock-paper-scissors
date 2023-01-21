from marshmallow import Schema, ValidationError, fields
from models.game import Choices


class UserSchema(Schema):
    name = fields.String(required=True)
    score = fields.Integer(required=False)


class GameSchema(Schema):
    player1 = UserSchema()
    player2 = UserSchema()


def validate_move(move: str):
    if hasattr(Choices, move.upper()):
        raise ValidationError("A move must be either ROCK, PAPER or SCISSORS.")


class GameMoveSchema(Schema):
    player1 = fields.Str(validate=validate_move)
    player2 = fields.Str(validate=validate_move)


class GameScoreSchema(Schema):
    player1 = fields.Integer(required=True)
    player2 = fields.Integer(required=True)
    id = fields.Integer(required=True)
