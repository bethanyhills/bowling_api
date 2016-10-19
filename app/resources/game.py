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
        parser.add_argument('players', action='append', help="{'players': ['player1','player2','players3']}")
        args = parser.parse_args()
        if args['players']:
            if type(args['players']) is list:
                game = Game(args['players'])
                players = game.get_players()
                response = {}
                response['game_id'] = game.id
                response['players'] = players
                return response, 200
            else:
                return {'message': 'you must format your players as a list'}, 400
        else:
            return {'message': 'you must add a list of players to create a new game'}, 400


class GameResource(Resource):
    '''
    endpoint to get game information, including current scores
    '''

    def get(self, game_id):
        game = Game.query.filter_by(id=game_id).first()
        if not game:
            return {"message": "Game does not exist. Please use a valid game_id or create a new game."}, 400
        scores = game.get_scores()
        response = {}
        response['game_id'] = game.id
        response['scores'] = scores
        return response, 200
