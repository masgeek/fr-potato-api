# routes/route.py
from flask import Blueprint, request, jsonify

from app.core import limiter
from app.potato.agwise_potato import AgWisePotato

api_v1 = Blueprint('api_v1', __name__)


# limiter.limit("1/minute")(api_v1)


@api_v1.route('/fr-potato-api-input', methods=['POST'])
@limiter.limit("1/minute")
def get_planting_season():
    data: object = request.get_json()

    if not data:
        return jsonify({'error': 'Missing JSON data in the request body'}), 400

    agwise = AgWisePotato()
    result = agwise.filter_data(data=data)
    return jsonify(result)
