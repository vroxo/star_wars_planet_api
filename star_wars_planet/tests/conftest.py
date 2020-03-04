import pytest
from star_wars_planet.app import create_app, minimal_app
from star_wars_planet.extensions.commands import populate_db, truncate_db
from star_wars_planet.documents import Planet


@pytest.fixture(scope="session")
def min_app():
    app = minimal_app(FORCE_ENV_FOR_DYNACONF="testing")
    return app


@pytest.fixture(scope="session")
def app():
    app = create_app(FORCE_ENV_FOR_DYNACONF="testing")
    with app.app_context():
        populate_db()
        yield app
        truncate_db()


@pytest.fixture(scope="session")
def client(app):
    client = app.test_client()

    yield client
    

@pytest.fixture(scope="session")
def planets(app):
    with app.app_context():
        return Planet.objects()


@pytest.fixture(scope="session")
def planet(app):
    with app.app_context():
        planet = Planet(name='TestePlanet', climate='TesteClimate', terrain='TesteTerrain', count_films=1)
        planet.save()
        return planet
