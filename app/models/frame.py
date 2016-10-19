from random import randint

from app import db

'''
Defines our Frame model.
There are two turns/rolls per Frame
(with the exception of the final frame where a strike earns 2 extra rolls and a spare earns 1 extra roll)
A maximum of 10 frames are possible.

'''

class Frame(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    #define the 1 side of the 1 to many relationship of player to frames
    player_id = db.Column(db.Integer, db.ForeignKey('player.id'))
    roll1 = db.Column(db.Integer)
    roll2 = db.Column(db.Integer)
    roll3 = db.Column(db.Integer)
    frame_number = db.Column(db.Integer)
    frame_score = db.Column(db.Integer)
    roll_count = db.Column(db.Integer)

    def __init__(self, player, frame_number):
        self.player_id = player.id
        self.frame_score = 0
        self.roll_count = 0
        self.frame_number = frame_number
        db.session.add(self)
        db.session.commit()

    def __repr__(self):
        return '<Frame Score %r>' % (self.frame_score)

    #defines a turn - 2 rolls to make up a frame. 3 potentially if its the 10th frame.
    def take_turn(self):
        rolls_allowed = 2
        pins_left = 10
        while self.roll_count < rolls_allowed :
            #handle extra rolls in 10th frame
            pins_hit = randint(0, pins_left)
            self.frame_score += pins_hit
            self.roll_count += 1

            #record individual roll scores
            self.parse_rolls(pins_hit)

            #if strike, break
            if self.strike():
                rolls_allowed = 0
            else:
                #continue to the next role
                pins_left = 10 - pins_hit

            if self.frame_number == 10:
                # add extra rolls if needed
                rolls_allowed += self.extra_rolls()

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

    #record individual roll scores
    def parse_rolls(self, pins_hit):
        if self.roll_count == 1:
            self.roll1 = pins_hit
        elif self.roll_count == 2:
            self.roll2 = pins_hit
        else:
            self.roll3 = pins_hit


    def extra_rolls(self):
        #only get a spare on 2nd roll. add 1 more roll to allow a final roll for a total of 3
        if self.spare():
            return 1
        #increment total allowed rolls to 3
        if self.strike():
            return 3
        return 0





