from flask_mongoengine import MongoEngine

db = MongoEngine()


def init_app(app):
    """
    Factory add the database to the application.
    :param app:
    """
    db.init_app(app)
