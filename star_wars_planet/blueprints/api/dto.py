from flask_restplus import Namespace, fields


class PlanetDto:
    ns = Namespace('planets', description='Planetas Star Wars')
    planet = ns.model('Planet', {
        'id': fields.String,
        'name': fields.String(description='Name of planet'),
        'climate': fields.String(description='Climate of planet'),
        'terrain': fields.String(description='Terrain of planet'),
        'count_films': fields.Integer
    })

    planet_payload = ns.model('Planet', {
        'name': fields.String(required=True, description='Name of planet'),
        'climate': fields.String(required=True, description='Climate of planet'),
        'terrain': fields.String(required=True, description='Terrain of planet'),
    })

    @staticmethod
    def validate_json_payload(**json) -> dict:
        """
        Validates that the id (defined by mongoDB) and cont_films (defined by SWAPI Service)
        fields are not in the payload

        :param json: Request json
        :return: dict
        """
        result = {'error': False, 'message': 'Payload is valid'}
        if 'id' in list(json.keys()):
            result['error'] = True
            result['message'] = "'id' is a invalid field"

        if 'count_films' in list(json.keys()):
            result['error'] = True
            result['message'] = "'count_films' is a invalid field"

        return result
