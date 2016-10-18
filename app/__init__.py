from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)
api = Api(app)

from app import models

from app.resources import NewGameResource, GameResource


api.add_resource(NewGameResource, '/game')
api.add_resource(GameResource, '/game/<string:game_id>')

