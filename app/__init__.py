from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
api = Api(app)

from app import models
db.create_all()

from app.resources import NewGameResource, GameResource, TurnResource

#define our endpoints for game creation, getting current game scores, and simulating a turn/frame for a player
api.add_resource(NewGameResource, '/game')
api.add_resource(GameResource, '/game/<string:game_id>')
api.add_resource(TurnResource, '/game/<string:game_id>/turn')

