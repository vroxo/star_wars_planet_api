from flask import Flask
from flask_mongoengine import MongoEngine

app = Flask(__name__)

app.config["SECRET_KEY"] = "flask+mongoengine=<3"
app.config['MONGODB_SETTINGS'] = {
    'db': 'star_wars_planets',
    'username': 'skywalker',
    'password': 'skywalker',
    'authentication_source': 'admin'
}

db = MongoEngine(app)

from .routes import blueprint
app.register_blueprint(blueprint, url_prefix='/api/v1')


