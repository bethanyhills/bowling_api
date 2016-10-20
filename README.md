# bowling_api
Bowling Score API for game creation, turn simulation, and scoring

#Steps:
1. Clone this repo
2. Pip install requirements
3. run the server: python /.run.py
4. use game_script.py to play a game against the Bowling Score API

#API Documentation:

###Create a New Game
  Endpoint: '/game'
  
  Action: POST
  
  Example: 
               
               post(url, 
                    data = {'players': ['Harry','Voldemort','Dumbledore']}), 
                    headers={'Content-type': 'application/json'}
                    )

  Returns: Game ID, Player Names, Player IDs
  
  Example Response: 
  
              {
                'game_id': 63, 
                'players': {
                             'Harry': 226,
                             'Voldemort': 227,
                             'Dumbledore': 225
                            }
                }
  
                
###Get Game Information
  Description: Returns the players and their current scores 
  
  Endpoint: '/game/:game_id'
  
  Action: GET
  
  Example: 
                
                
                get(url + '/{}'.format(game_id), 
                    headers={'Content-type': 'application/json'}
                    )

  Returns: Game ID, Player Names, Player Current Scores
  
  Example Response: 
  
                {
                  'game_id': 63, 
                  'scores': {
                              'Harry': 85,
                              'Voldemort': 67,
                              'Dumbledore': 94
                            }
                 }


###Take a Turn
  Description: Simulates a turn (2 rolls to make a full frame. If 10th frame, includes any bonus rolls)
  
  Endpoint: '/game/:game_id/turn'
  
  Action: PUT
  
  Example:
              
              
              put(url + '/{}/turn'.format(game_id), 
                  data = {'player_id': player_id}, 
                  headers={'Content-type': 'application/json'}
                  )
  
      
  Returns: Player Name, Player Current Score
  
  Example Response: 
          
          If game is in progress:
                
                
                {
                  'ID': 226, 
                  'Current Score': 85
                }
                
                
          
          If 10 Frames have been played:
          
                
                {
                  'ID': 226, 
                  'Final Score': 120
                }
            


