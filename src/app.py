from flask import Flask, request, jsonify
from flask_swagger_ui import get_swaggerui_blueprint

app = Flask(__name__)


@app.route('/add', methods=['GET'])
def add():
    """
    Sčítání dvou čísel.

    Příklad použití:
    >>> add()
    {'result': 3}
    >>> add(2, 3)
    {'result': 5}
    """
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return jsonify({'result': a + b})


@app.route('/subtract', methods=['GET'])
def subtract():
    """
    Odčítání dvou čísel.

    Příklad použití:
    >>> subtract()
    {'result': 2}
    >>> subtract(5, 3)
    {'result': 2}
    """
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return jsonify({'result': a - b})


@app.route('/multiply', methods=['GET'])
def multiply():
    """
    Násobení dvou čísel.

    Příklad použití:
    >>> multiply()
    {'result': 12}
    >>> multiply(3, 4)
    {'result': 12}
    """
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)
    return jsonify({'result': a * b})


@app.route('/divide', methods=['GET'])
def divide():
    """
    Dělení dvou čísel s ošetřením dělení nulou.

    Příklad použití:
    >>> divide()
    {'result': 4}
    >>> divide(8, 2)
    {'result': 4}
    >>> divide(8, 0)
    {'error': 'Cannot divide by zero'}
    """
    a = request.args.get('a', type=int)
    b = request.args.get('b', type=int)

    if b == 0:
        return jsonify({'error': 'Cannot divide by zero'}), 400

    return jsonify({'result': a / b})


# Definování cesty k Swagger JSON dokumentaci
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'

# Vytvoření Swagger UI blueprintu
swagger_ui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL, config={
    'app_name': "Kalkulačka API"
})

# Registrace blueprintu
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

if __name__ == '__main__':
    app.run(debug=True)
