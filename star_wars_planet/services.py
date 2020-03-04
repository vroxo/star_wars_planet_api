import requests
from dynaconf import settings


class SWAPIService:
    def __init__(self):
        self.uri = settings.URI_SWAPI

    def get_planet_by_name(self, planet_name) -> dict:
        """
        Returns the planets that contain the name specified via SWAPI.

        :param planet_name: str
        :return: dict
        """
        url = f'{self.uri}/planets/?search={planet_name}'
        response = requests.get(url)

        result_dict = dict(status_code=response.status_code, message='', result={})
        if response.status_code != 200:
            result_dict['message'] = 'Resource Not Found!'
        else:
            json_response = response.json()

            if int(json_response.get('count')) == 0:
                result_dict['message'] = 'Success! But no planet with that name was found.'
            else:
                result_dict['message'] = 'Success!'
                result_dict['result'] = json_response.get('results')[0]

        return result_dict

    def count_films_by_planet_name(self, planet_name: str) -> dict:
        """
        Returns the name of the planet and the number of films that the planet appears in a dictionary.

        :param planet_name: str
        :return: dict
        """
        json_response = self.get_planet_by_name(planet_name)
        json_result = dict(status_code=json_response.get('status_code'), result=dict())

        if json_response.get('result'):
            planet = json_response.get('result')
            json_result['result'] = dict(planet_name=planet.get('name'), count_films=len(planet.get('films')))

        return json_result
