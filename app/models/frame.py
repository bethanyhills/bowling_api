from app import db

'''
Defines our Frame model.
There are two turns per Frame.
A maximum of 13 frame are possible.

'''

class Frame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #define the 1 side of the 1 to many relationship of player to frames
    player_id = db.Columnn(db.Integer, db.ForeignKey('player.id'))
    frame_number = db.Column(db.Integer)
    frame_score = db.Column(db.Integer)
    turn_1 = db.Column(db.Integer)
    turn_2 = db.Colum(db.Integer)

    def __init__(self, player_id):
        self.player_id = player_id
        self.frame_score = 0

    def __repr__(self):
        return '<Current Score %r>' % (self.frame_score)