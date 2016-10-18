from flask.ext.restful import Resource, reqparse, fields, marshal_with
import json

from app.models import Game


class NewGameResource(Resource):
    '''
    create new game by passing in a list of players. returns a game ID.
    '''
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('players')
        args = parser.parse_args()
        if args['players']:
            game = Game(args['players'])
            return {'Game': game.id}


class GameResource(Resource):
    '''
    endpoint to get game information, including current scores
    '''

    def get(self, game_id):
        game = Game.query.filter_by(id=game_id).first()
        scores = game.get_scores()
        return {'Game': game.id, 'Scores': scores}