from flask import Flask, request, jsonify, Response
from flask.views import MethodView
from marshmallow import ValidationError
from schema.game import GameSchema, GameMoveSchema, GameScoreSchema
from lib.game import GameLib
from repository.game import GameRepo
from db import PostgresSQLConnection
import os

app = Flask(__name__)


class GameAPI(MethodView):

    def __init__(self) -> None:
        super().__init__()
        db_conn = PostgresSQLConnection(
            host=os.environ['DB_HOST'],
            port=os.environ['DB_PORT'],
            database=os.environ['DB_DATABASE'],
            username=os.environ['DB_USERNAME'],
            password=os.environ['DB_PASSWORD']
        )

        repo = GameRepo(conn=db_conn)
        self.lib = GameLib(repo=repo)

    def get(self):
        game = self.lib.retrieve(self.get('id'))
        if not game:
            return Response(status=404)
        return Response(response=game, status=200)

    def post(self):
        data = request.get_json()
        schema = GameSchema()
        try:
            # Validate request body against schema data types
            result = schema.load(data)
        except ValidationError as err:
            return Response(jsonify(err.messages), status=404)

        id = self.lib.start(result)
        return Response({
            "message": "Game started",
            "id": id
        }, 201)

    def put(self):
        data = request.get_json()
        schema = GameScoreSchema()
        try:
            # Validate request body against schema data types
            result = schema.load(data)
        except ValidationError as err:
            return Response(jsonify(err.messages), status=400)
        response = self.lib.Score(game_move=result)
        return Response({
            "message": response,
            "id": self.get('id')
        }, 204)

    def patch(self):
        data = request.get_json()
        schema = GameMoveSchema()
        try:
            # Validate request body against schema data types
            result = schema.load(data)
        except ValidationError as err:
            return Response(jsonify(err.messages), status=400)
        response = self.lib.play(game_move=result)
        return Response({
            "winner": response,
            "id": self.get('id')
        }, 200)


app.add_url_rule('/game', view_func=GameAPI.as_view('counter'))


if __name__ == '__main__':
    app.run(debug=True)
