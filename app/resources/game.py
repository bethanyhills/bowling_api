from flask.ext.restful import Resource, reqparse, fields, marshal_with
from flask import jsonify
import json
import pdb

from app.models import Game


class NewGameResource(Resource):
    '''
    create new game by passing in a list of players. returns a game ID.
    '''
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('players', action='append')
        args = parser.parse_args()
        if args['players']:
            game = Game(args['players'])
            players = game.get_players()
            response = {}
            response['game_id'] = game.id
            response['players'] = players
        return response


class GameResource(Resource):
    '''
    endpoint to get game information, including current scores
    '''

    def get(self, game_id):
        game = Game.query.filter_by(id=game_id).first()
        scores = game.get_scores()
        response = {}
        response['game_id'] = game.id
        response['scores'] = scores
        return response
