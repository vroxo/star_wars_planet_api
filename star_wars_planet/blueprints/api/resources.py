from flask import request
from mongoengine import errors
from flask_restplus import Resource

from .dto import PlanetDto
from star_wars_planet.documents import Planet
from star_wars_planet.services import SWAPIService

ns = PlanetDto.ns
_planet = PlanetDto.planet
_payload = PlanetDto.planet_payload


@ns.route('/')
@ns.doc(responses={200: 'Success', 201: 'Object Created', 500: 'Internal Error'},
        params={'planet_id': 'Specify the Id associated with the planet.'})
class PlanetsResource(Resource):
    @ns.marshal_list_with(_planet)
    def get(self):
        """
        HTTP verb GET - Returns all planets inserted or containing the specified name.
        :return: json
        """
        search_name = request.args.get('search_name')
        if search_name:
            planets = Planet.objects(name__icontains=search_name)
        else:
            planets = Planet.objects()

        return [{'id': str(planet.id), 'name': planet.name, 'climate': planet.climate, 'terrain': planet.terrain,
                 'count_films': planet.count_films} for
                planet in
                planets]

    @ns.expect(_payload, validate=True)
    def post(self):
        """
        HTTP verb POST - Creates a new planet.
        :return: json, status_code
        """
        try:
            payload_validated = PlanetDto.validate_json_payload(**request.json)

            if payload_validated.get('error'):
                return {"errors": {"name": f"{payload_validated.get('message')}"},
                        "message": "Input payload validation failed"}, 400

            planet_name = request.json['name']
            service = SWAPIService()
            response = service.count_films_by_planet_name(planet_name)

            if response.get('status_code') == 200:
                json_planet = response.get('result')
                Planet(
                    name=request.json['name'],
                    climate=request.json['climate'],
                    terrain=request.json['terrain'],
                    count_films=json_planet.get('count_films')
                ).save()
                result = {'message': f"Planet {planet_name} created!"}, 201
            else:
                result = {'message': "Impossible to consult the SWAPI service to register the number of films.!"}, 500

            return result
        except errors.InvalidDocumentError as ie:
            ns.abort(400, ie.__str__(), status='Body invalid', statusCode='400')
        except Exception as e:
            ns.abort(500, e.__str__(), status='Body invalid', statusCode='500')


@ns.route('/<string:planet_id>')
@ns.doc(responses={200: 'Success', 204: 'Object Deleted.', 400: 'Invalid Argument', 500: 'Internal Error',
                   404: 'Not Found'},
        params={'planet_id': 'Specify the Id associated with the planet.'})
class PlanetItemResource(Resource):
    @ns.marshal_with(_planet)
    def get(self, planet_id):
        """
        HTTP verb GET - Returns a specific planet
        :param planet_id: string
        :return: json, status_code
        """
        try:
            planet = Planet.objects(id=planet_id).get()
            return planet
        except errors.ValidationError as ve:
            ns.abort(400, ve.__str__(), status='Could not retrieve information!', status_code='400')
        except errors.DoesNotExist as dne:
            ns.abort(404, dne.__str__(), status='Planet not found!', status_code='404')
        except Exception as e:
            ns.abort(500, e.__str__(), status='Internal Error!', status_code='500')

    def delete(self, planet_id):
        """
        HTTP verb DELETE - Remove a specific planet

        :param planet_id:
        :return: json, status_code
        """
        try:
            planet = Planet.objects(id=planet_id).get()
            planet.delete()
            return f'Planet {planet.name} deleted!', 204
        except errors.ValidationError as ve:
            ns.abort(400, ve.__str__(), status='Could not retrieve information!', statusCode='400')
        except errors.DoesNotExist as dne:
            ns.abort(404, dne.__str__(), status='Planet not found!', statusCode='404')
        except Exception as e:
            ns.abort(500, e.__str__(), status='Internal Error!', statusCode='500')

    @ns.expect(_payload, validate=True)
    def put(self, planet_id):
        """
        HTTP verb PUT - Update Planet
        :param planet_id:
        :return:
        """
        try:
            payload_validated = PlanetDto.validate_json_payload(**request.json)

            if payload_validated.get('error'):
                return {"errors": {"name": f"{payload_validated.get('message')}"},
                        "message": "Input payload validation failed"}, 400

            planet = Planet.objects(id=planet_id).get()
            planet.update(**request.json)
            return '', 204
        except errors.ValidationError as ve:
            ns.abort(400, ve.__str__(), status='Bad request!', statusCode='400')
        except errors.DoesNotExist as dne:
            ns.abort(404, dne.__str__(), status='Planet not found!', statusCode='404')
        except Exception as e:
            ns.abort(500, e.__str__(), status='Internal Error!', statusCode='500')
