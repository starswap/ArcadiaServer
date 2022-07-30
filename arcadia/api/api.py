from flask import Blueprint, Flask, request, Response
import json
import haversine as hs
from .arcadeLocation import arcadeLocation
from haversine import Unit
import math


api_bp = Blueprint('api_bp', __name__)


@api_bp.route("/game/find", methods=['GET', 'POST'])
def find_games():
    # needs to be sent current location of user in request
    user_x = request.values.get('xcoord')
    user_y = request.values.get('ycoord')

    # do logic here

    return Response(
        response=json.dumps(
            {
                "radius": "50m",
                "locations": [{"x": 1.11111, "y": 2.22222}, {"x": 4.444444, "y": 5.55555}, {"x": 6.666666, "y": 7.7777}]
            }
        ),
        status=200,
        mimetype='application/json'
    )


@api_bp.route("/game/<arcade_id>/guess", methods=['POST'])
def recieve_guess(arcade_id):
    user_x = request.values.get('xcoord')
    user_y = request.values.get('ycoord')
    # arcade_id = request.values.get('arcade_id')
    arcade_x, arcade_y = arcadeLocation.get_arcade_coords(arcade_id)
    distance = hs.haversine((arcade_x, arcade_y),
                            (user_x, user_y), unit=Unit.METERS)
    direction = 'placeholder'
    response_dict = {'direction': direction, 'distance': distance}

    return Response(
        response=json.dumps(response_dict),
        status=200,
        mimetype='application/json'
    )


#! I am not sure this is necessary?
@api_bp.route("/game/<arcade_id>/clue", methods=['GET', 'POST'])
def get_clue(arcade_id):
    # needs to be sent current location of user in request
    return Response(
        response=json.dumps({"key": "str"}),
        status=200,
        mimetype='application/json'
    )
