from importlib import import_module
from dynaconf import FlaskDynaconf


def load_extensions(app):
    """
    Load all extensions defined in settings.toml for the application
    :param app: Flask object
    """
    for extension in app.config.EXTENSIONS:
        mod = import_module(extension)
        mod.init_app(app)


def init_app(app, **config):
    """
    Factory to add all configurations in the application

    :param app: Flask object
    :param config:
    """
    FlaskDynaconf(app, **config)
