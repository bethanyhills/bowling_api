from app import db
#from app.models.player import Player

'''
Defines our Frame model.
There are two turns per Frame.
A maximum of 13 frame are possible.

'''

class Frame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #define the 1 side of the 1 to many relationship of player to frames
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    frame_number = db.Column(db.Integer)
    frame_score = db.Column(db.Integer)
    turn_1 = db.Column(db.Integer)
    turn_2 = db.Column(db.Integer)

    def __init__(self, player, frame_number):
        self.player_id = player.id
        self.frame_score = 0
        self.frame_number = frame_number
        db.session.add(self)

    def __repr__(self):
        return '<Current Score %r>' % (self.frame_score)
