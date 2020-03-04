from star_wars_planet.documents import Planet


def populate_db():
    """
    Population database
    """
    Planet.objects.insert([
        Planet(name='Endor', climate='temperate', terrain='forests, mountains, lakes', count_films=1),
        Planet(name='Naboo', climate='temperate', terrain='grassy hills, swamps, forests, mountains', count_films=4),
        Planet(name='Alderaan', climate='temperate', terrain='rasslands, mountains', count_films=1)
    ])


def truncate_db():
    """
    Drop database
    """
    Planet.drop_collection()


def init_app(app):
    """
    Factory to add all custom commands in the application

    :param app: Flask object
    """
    for command in [populate_db, truncate_db]:
        app.cli.add_command(app.cli.command()(command))
