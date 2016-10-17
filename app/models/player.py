from app import db

'''
defines our Player model
'''

class Player(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Player %r>' % (self.name)

