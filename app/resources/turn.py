from flask.ext.restful import Resource, reqparse, fields, marshal_with
import json

from app.models import Player, Frame

class TurnResource(Resource):
    '''
    endpoint for a turn /frame
    '''
    def put(self, game_id):
        parser = reqparse.RequestParser()
        parser.add_argument('player_id')
        args = parser.parse_args()
        player_id = args['player_id']

        player = Player.query.filter_by(id=player_id).first()
        frame_number = player.frames.count()

        if frame_number < 10:
            turn = Frame(player, frame_number + 1)
            turn.take_turn()
            player.calculate_score()
            return {'Current Score': player.current_score}
        else:
            return {'Final Score': player.current_score}













