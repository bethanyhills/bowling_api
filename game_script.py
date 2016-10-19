import requests
import json

url = 'http://127.0.0.1:5000/game'

def new_game():
    '''
    creates a new game
    returns game_id, players and their player IDs.
    ex. {u'game_id': 63, u'players': {u'voldemort': 226, u'ron': 227, u'harry': 225}}

    '''
    headers = {'Content-type': 'application/json'}
    data = {'players': ['harry','voldemort','ron']}
    game = requests.post(url, data=json.dumps(data), headers=headers)
    print game.json()
    return game.json()

def get_current_scores(game_id):
    '''
       returns the current scores for each player
       ex. {u'game_id': 63, u'scores': {u'voldemort': 85, u'ron': 67, u'harry': 94}}
    '''
    game = requests.get(url + '/{}'.format(game_id))
    return game.json()

def take_turn(game_id, player_id):
    '''
    similuates a turn/ complete frame.
    returns a players current score or final score if full 10 frames complete
    '''
    headers = {'Content-type': 'application/json'}
    data = {'player_id': player_id}
    turn = requests.put(url + '/{}/turn'.format(game_id), data=json.dumps(data), headers=headers)
    return turn.json()

#create a new game
game = new_game()
#define frames to play (10 is standard)
for frame in range(1, 11):
    #play a frame
    for player, id in game['players'].items():
        take_turn(str(game['game_id']), id)
    #report on current scores
    print (get_current_scores(str(game['game_id'])))

