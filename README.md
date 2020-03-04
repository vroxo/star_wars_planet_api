# STAR WARS PLANET API
## CLONE

`$ git clone git@github.com:vroxo/star_wars_planet_api.git`

or 

`$ git clone https://github.com/vroxo/star_wars_planet_api.git`

## SETUP

This application uses docker containers, it is mandatory to install Docker CLI and Docker compose.

Enter the docker folder at the root of the project:

`$ cd docker`

Create the containers from the docker-compose.yml file:

`$ docker-compose up -d`

All application dependencies will be installed and the application started using the address http://localhost:5000/ (default for a Flask application)

If we look at the docker files we will see that the main dependencies of the application:

- Python 3.8
- Flask
- Flask Restplus
- Flask MongoEngine
- Pytest
- Dynaconf
- MongoDB

Run the Flask custom command to populate the database:

`$ docker exec star_wars_api flask populate-db`

If you want to clear the existing data in the database, use:

`$ docker exec star_wars_api flask truncate-db`

Run tests:

`$ pytest src/tests`

## API

| HTTP VERB | URL PATH | DESCRIPTION |
|-----------|----------|-------------|
| POST | /api/v1/planets | Creates a new planet | 
| GET | /api/v1/planets | Lists all inserted planets |
| GET | /api/v1/planets/{id} | Returns a specific planet |
| GET | /api/v1/planets/?search_name={name} | List planets containing the given name |
| PUT | /api/v1/planets/{id} | Updates a specific planet. | 
| DELETE | /api/v1/planets/{id} | Removes a specific planet. |

#### POST - /api/v1/planets

###### Input payload:

`{
    name: string (required),
    climate: string (required),
    terrain: string (required)
}`

###### Responses: 

201 CREATED:

`{"message": "Planet [planet_name] created!}`

400 BAD REQUEST

`{
  "errors": {
    "name": "[required_field] is a required property"
  },
  "message": "Input payload validation failed"
}`

`{
  "errors": {
    "name": "[invalid_field] is a invalid field"
  },
  "message": "Input payload validation failed"
}`

#### GET - /api/v1/planets/

###### Responses:

200 OK

`[
  {
    "id": "5e5f0fb48f327012f793b7b2",
    "name": "Endor",
    "climate": "temperate",
    "terrain": "forests, mountains, lakes",
    "count_films": 1
  },
  {
    "id": "5e5f39b1b1452a2f5fafac96",
    "name": "Naboo",
    "climate": "temperate",
    "terrain": "grassy hills, swamps, forests, mountains",
    "count_films": 4
  },
  {
    "id": "5e5f45b48e83f3e3bdda66d0",
    "name": "Alderaan",
    "climate": "temperate",
    "terrain": "grasslands, mountains",
    "count_films": 2
  }
]`

#### GET - /api/v1/planets/?search_name={planet_name}

###### Responses:

200 OK

`[ { "id": "5e5f0fb48f327012f793b7b2", "name": "Endor", "climate": "temperate", "terrain": "forests, mountains, lakes", "count_films": 1 }]`

#### GET - /api/v1/planets/{id}

###### Responses:

200 OK

`{ "id": "5e5f0fb48f327012f793b7b2", "name": "Endor", "climate": "temperate", "terrain": "forests, mountains, lakes", "count_films": 1 }`

400 BAD REQUEST

`{
  "status": "Could not retrieve information!",
  "status_code": "400",
  "message": "[id] is not a valid ObjectId, it must be a 12-byte input or a 24-character hex string"
}`

#### PUT - /api/v1/planets/{id}

###### Input payload:

`{
    name: string (required),
    climate: string (required),
    terrain: string (required)
}`

204 NO CONTENT

400 BAD REQUEST

`{
  "errors": {
    "name": "[required_field] is a required property"
  },
  "message": "Input payload validation failed"
}`

`{
  "errors": {
    "name": "[invalid_field] is a invalid field"
  },
  "message": "Input payload validation failed"
}`

#### DELETE - /api/v1/planets/{id}

###### Responses:

204 NO CONTENT

400 BAD REQUEST

`{
  "status": "Could not retrieve information!",
  "status_code": "400",
  "message": "[id] is not a valid ObjectId, it must be a 12-byte input or a 24-character hex string"
}`
