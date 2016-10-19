from flask.ext.restful import Resource, reqparse, fields, marshal_with
import json
import pdb

from app.models import Player, Frame

class TurnResource(Resource):
    '''
    endpoint for a turn /frame
    '''
    def put(self, game_id):
        parser = reqparse.RequestParser()
        parser.add_argument('player_id')
        args = parser.parse_args()

        player = Player.query.filter_by(id=int(args['player_id'])).first()
        frame_number = player.frames.count()
        if frame_number < 10:
            #create Frame
            turn = Frame(player, frame_number + 1)
            #simulate 2 rolls
            turn.take_turn()
            #calculate current score
            player.calculate_score()
            return {'Current Score': str(player.current_score)}
        else:
            return {'Final Score': str(player.current_score)}













