#!env/bin/python
import os
import unittest
import requests
import json

from config import basedir
from app import app, db
from app.models import Game, Frame, Player
from app.resources import NewGameResource, GameResource, TurnResource

client = 'http://127.0.0.1:5000/game'

class TestCase(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        self.app = app.test_client()
        # define our endpoints for game creation, getting current game scores, and simulating a turn/frame for a player
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_create_game_db(self):
        game = Game(players=['player1', 'player2', 'player3'])
        db.session.add(game)
        db.session.commit()
        assert game.id
        assert game.players.count() == 3

    def test_create_player_db(self):
        game = Game(players=['player1', 'player2', 'player3'])
        db.session.add(game)
        db.session.commit()
        for player in game.players:
            #confirm player created and associated to game
            assert player.id
            assert player.game_id

    def test_create_frame_db(self):
        game = Game(players=['player1', 'player2', 'player3'])
        db.session.add(game)
        frame = Frame(game.players[0], 1)
        db.session.commit()
        assert frame.id
        assert frame.frame_number


    #Test API Endpoints
    def test_create_game_endpoint(self):
        headers = {'Content-type': 'application/json'}
        data = {'players': ['test1', 'test2', 'test3', 'test4']}
        response = requests.post(client, data=json.dumps(data), headers=headers)
        assert response.status_code == 200
        assert response.json()['game_id']
        assert len(response.json()['players']) == len(data['players'])
        return response.json()

    def test_get_game_current_score(self):
        game = self.test_create_game_endpoint()
        response = requests.get(client + '/{}'.format(game['game_id']))
        assert response.status_code == 200
        #no turns yet so scores should be 0
        assert sum(response.json()['scores'].values()) == 0

    def test_take_turn(self):
        new_game = self.test_create_game_endpoint()
        for name, id in new_game['players'].items():
            headers = {'Content-type': 'application/json'}
            data = {'player_id': id}
            turn = requests.put(client + '/{}/turn'.format(new_game['game_id']), data=json.dumps(data), headers=headers)
            assert turn.status_code == 200
            assert turn.json()['Current Score']

    def test_full_frames(self):
        new_game = self.test_create_game_endpoint()
        previous_score_sum = 0
        for num in range(1, 11):
            for name, id in new_game['players'].items():
                headers = {'Content-type': 'application/json'}
                data = {'player_id': id}
                turn = requests.put(client + '/{}/turn'.format(new_game['game_id']), data=json.dumps(data),
                                    headers=headers)
            current_scores = requests.get(client + '/{}'.format(new_game['game_id']))
            current_score_sum = sum(current_scores.json()['scores'].values())
            assert current_score_sum > previous_score_sum
            previous_scores = current_score_sum

    def test_no_players(self):
        headers = {'Content-type': 'application/json'}
        response = requests.post(client, headers=headers)
        assert response.status_code == 400

    def test_invalid_player_id(self):
        new_game = self.test_create_game_endpoint()
        headers = {'Content-type': 'application/json'}
        data = {'player_id': '0823940328'}
        turn = requests.put(client + '/{}/turn'.format(new_game['game_id']), data=json.dumps(data), headers=headers)
        assert turn.status_code == 400

    def test_invalid_game_id(self):
        response = requests.get(client + '/{}'.format('084328'))
        assert response.status_code == 400

if __name__ == '__main__':
    unittest.main()