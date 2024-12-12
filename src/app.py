from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)

# Definice swagger.json
swagger = {
    "openapi": "3.0.0",
    "info": {
        "title": "Kalkulačka API",
        "version": "1.0.0",
        "description": "API pro základní matematické operace"
    },
    "paths": {
        "/add": {
            "get": {
                "summary": "Sčítání dvou čísel",
                "parameters": [
                    {
                        "name": "a",
                        "in": "query",
                        "description": "První číslo",
                        "required": True,
                        "schema": {
                            "type": "integer"
                        }
                    },
                    {
                        "name": "b",
                        "in": "query",
                        "description": "Druhé číslo",
                        "required": True,
                        "schema": {
                            "type": "integer"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Výsledek sčítání",
                        "content": {
                            "application/json": {
                                "example": {
                                    "result": 5
                                }
                            }
                        }
                    }
                }
            }
        },
        "/subtract": {
            "get": {
                "summary": "Odčítání dvou čísel",
                "parameters": [
                    {
                        "name": "a",
                        "in": "query",
                        "description": "První číslo",
                        "required": True,
                        "schema": {
                            "type": "integer"
                        }
                    },
                    {
                        "name": "b",
                        "in": "query",
                        "description": "Druhé číslo",
                        "required": True,
                        "schema": {
                            "type": "integer"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Výsledek odčítání",
                        "content": {
                            "application/json": {
                                "example": {
                                    "result": 2
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}


# Definice API endpointů
@app.route('/add', methods=['GET'])
def add():
    """
    Sčítání dvou čísel.
    """
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return jsonify({'result': a + b})


@app.route('/subtract', methods=['GET'])
def subtract():
    """
    Odčítání dvou čísel.
    """
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return jsonify({'result': a - b})


# Konfigurace Swagger UI
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'  # Cesta k JSON souboru Swagger dokumentace

swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={  # Nastavení Swagger UI
        'app_name': "Kalkulačka API"
    }
)

# Registrování Swagger UI blueprintu
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)


# Uložení swagger.json do statických souborů
@app.route('/static/swagger.json')
def swagger_json():
    return jsonify(swagger)


@app.route('/')
def home():
    return 'Hello, World!'


if __name__ == '__main__':
    app.run(debug=True)
