from app import db

'''
defines our Game model.
Many players to a game.

'''

class Game(db.model):
    id = db.Column(db.Integer, primary_key=True)
    is_complete = db.Column(db.Boolean, default=False)
    #defines the 1 to many relationship of game to players
    players = db.relationship(
        'Player', backref=db.backref('game', lazy='joined'), lazy='dynamic')

    def __init__(self, players):
        #TODO: THERE MUST BE PLAYERS TO INITIALIZE A GAME
        self.players = players

    def __repr__(self):
        return '<Players %r>' % (self.players)
