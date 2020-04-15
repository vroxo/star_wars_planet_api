import pytest


@pytest.fixture
def json_valid():
    return {
        'name': 'ValidPlanet',
        'climate': 'ValidPlanet',
        'terrain': 'ValidPlanet'
    }


@pytest.fixture
def json_not_valid():
    return {
        'id': 1,
        'name': 'ValidPlanet',
        'climate': 'ValidPlanet',
        'terrain': 'ValidPlanet'
    }


def test_planets_get_all(client, planets, mocker):
    response = client.get('/api/v1/planets/')
    data = response.json
    assert len(data) == 3
    for planet in planets:
        assert str(planet.id) in [str(item["id"]) for item in data]
        assert planet.name in [item["name"] for item in data]
        assert planet.climate in [item["climate"] for item in data]
        assert planet.terrain in [item["terrain"] for item in data]
        assert planet.count_films in [item["count_films"] for item in data]


def test_planets_get_by_id(client, planet, mocker):
    response = client.get(f'/api/v1/planets/{planet.id}')
    data = response.json
    print(data)
    assert str(planet.id) == data["id"]
    assert planet.name == data["name"]
    assert planet.climate == data["climate"]
    assert planet.terrain == data["terrain"]
    assert planet.count_films == data["count_films"]


def test_planets_get_by_id_not_valid(client):
    response = client.get(f'/api/v1/planets/id_not_valid')
    print(response.json)
    assert response.status_code == 400
    assert response.json['status'] == 'Could not retrieve information!'


def test_planets_get_by_name(client, planet, mocker):
    response = client.get(f'/api/v1/planets/?search_name={planet.name}')

    assert len(response.json) == 1
    assert str(planet.id) in [str(item["id"]) for item in response.json]


def test_post_planet(client, json_valid, mocker):
    mocker.patch("star_wars_planet.services.SWAPIService.count_films_by_planet_name",
                 return_value=dict(status_code=200, result=dict(planet_name='ValidPlanet', count_films=2)))

    response = client.post('/api/v1/planets/', json=json_valid)
    assert response.status_code == 201
    assert response.json == {'message': f"Planet {json_valid['name']} created!"}


def test_post_planet_with_json_invalid(client, json_not_valid):
    response = client.post('/api/v1/planets/', json=json_not_valid)
    assert response.status_code == 400
    assert response.json['message'] == "Input payload validation failed"


def test_put_planet(client, planet, json_valid, mocker):
    response = client.put(f'/api/v1/planets/{planet.id}', json=json_valid)
    assert response.status_code == 204


def test_put_planet_with_invalid_json(client, planet, json_not_valid):
    response = client.put(f'/api/v1/planets/{planet.id}', json=json_not_valid)
    assert response.status_code == 400
    assert response.json['message'] == "Input payload validation failed"


def test_delete_planet(client, planet, mocker):
    response = client.delete(f'/api/v1'
                             f'/planets/{planet.id}')
    assert response.status_code == 204


def test_delete_planet_with_invalid_id(client):
    response = client.delete('/api/v1/planets/invalid_id')
    assert response.status_code == 400


def test_invalid_url(client):
    response = client.delete('/invalid//api/v1/planets/')
    assert response.status_code == 404


def test_fail():
    assert False
