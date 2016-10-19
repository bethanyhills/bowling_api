from app import db
#from app.models.game import Game
from app.models.frame import Frame

'''
defines our Player model
'''

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

    # define the 1 side of the 1 to many relationship of game to players
    game_id = db.Column(db.Integer, db.ForeignKey('game.id'))

    #defines one to many relationship of player to frames. join loads the relationship in the same query as the parent.
    #dynamic is used for many items - it returns a query object
    frames = db.relationship('Frame', backref='player', lazy='dynamic')
    current_score = db.Column(db.Integer)

    def __init__(self, name, game):
        self.name = name
        self.game_id = game.id
        db.session.add(self)

    def __repr__(self):
        return '%r' % (self.id)

    def calculate_score(self):
        #calculate score - taking into consideration strikes and spares
        frames = self.frames.all()
        score = 0
        for i, frame in enumerate(frames):
            #add frame score
            score += frame.frame_score
            #if frame was strike or spare, calculate extra points
            if frame.strike() or frame.spare():
                extra_points = self.calculate_bonus(i, frame, frames)
                score += extra_points
        self.current_score = score
        db.session.add(self)
        db.session.commit()

    def calculate_bonus(self, i, frame, frames):
        #if this is the most recent frame played, return. No frames exist yet to score the bonus points
        if frame == frames[-1]:
            return 0
        #add the following 2 rolls
        if frame.strike():
            return frames[i+1].frame_score
        #add the next roll
        if frame.spare():
            return frames[i+1].roll1





