from flask import Flask
from star_wars_planet.extensions import configuration


def minimal_app(**config) -> object:
    """
    Creates a basic Flask application

    :param config:
    :return: Flask object
    """
    app = Flask(__name__)
    configuration.init_app(app, **config)
    return app


def create_app(**config) -> object:
    """
    Create a Flask application with all settings specified in settings.toml

    :param config:
    :return: Flask object
    """
    app = minimal_app(**config)
    configuration.load_extensions(app)
    return app

