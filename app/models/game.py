from app import db
from app.models.player import Player
'''
defines our Game model.
Many players to a game.

'''

class Game(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    is_complete = db.Column(db.Boolean, default=False)
    #defines the 1 to many relationship of game to players
    players = db.relationship('Player', backref='game', lazy='dynamic')

    def __init__(self, players= []):
        #TODO: take a list of players, create player, associate to game
        if players:
            print (players)
            for player in players:
                print (player)
                p = Player(player, self)
                self.players.append(p)
                db.session.add(p)
        db.session.add(self)
        db.session.commit()



    def __repr__(self):
        return '<Players %r>' % (self.players)
