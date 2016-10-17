from random import randint

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
    roll_count = db.Column(db.Integer)

    def __init__(self, player, frame_number):
        self.player_id = player.id
        self.frame_score = 0
        self.roll_count = 0
        self.frame_number = frame_number
        db.session.add(self)

    def __repr__(self):
        return '<Current Score %r>' % (self.frame_score)

    #2 rolls allowed per turn. Those 2 rolls make up a frame.
    def take_turn(self):
        rolls_left = 2
        pins_left = 10
        while rolls_left > 0:
            #handle extra rolls in 10th frame
            if self.frame_number == 10:
                #add extra rolls if needed
                rolls_left += self.extra_rolls()
            pins_hit = randint(0, pins_left)
            self.frame_score += pins_hit
            self.roll_count += 1
            #if strike, break
            if self.strike():
                rolls_left = 0
            else:
                #continue to 2nd role
                pins_left = 10 - pins_hit
                rolls_left -= 1

        db.session.add(self)
        db.session.commit()

    # determine if strike
    def strike(self):
        if self.roll_count == 1 and self.frame_score == 10:
            return True
        else:
            return False

    # determine if spare
    def spare(self):
        if self.roll_count == 2 and self.frame_score == 10:
            return True
        else:
            return False

    def extra_rolls(self):
        if self.spare():
            return 1
        if self.strike():
            return 2
        return 0





