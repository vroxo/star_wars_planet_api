from flask import Blueprint
from flask_restplus import Api
from .resources import ns

bp = Blueprint("Star Wars Planets API", __name__)
api = Api(bp,
          version="1.00.00",
          title="Star Wars Planets API",
          description="API for managing planets from Star Wars movies.",
          doc='/doc/')


def init_app(app):
    """
    Factory creates the api via blueprint and a namespace for the api in the application

    :param app: Flask object
    """
    api.add_namespace(ns)
    app.register_blueprint(bp, url_prefix='/api/v1')
