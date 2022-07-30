from flask import Blueprint, Flask, request
import json
import haversine as hs
from .arcadeLocation import arcadeLocation
from haversine import Unit
import math



api_bp = Blueprint('api_bp', __name__)


@api_bp.route("/game/find", methods = ['GET', 'POST'])
def get_first_clue():
    #needs to be sent current location of user in request
    return ""


@api_bp.route("/game/<arcade_id>/guess", methods = ['GET', 'POST'])
def recieve_guess(arcade_id):
    if request.method == 'POST':
        user_x = request.values.get('xcoord')
        user_y = request.values.get('ycoord')
        # arcade_id = request.values.get('arcade_id')
        arcade_x, arcade_y = arcadeLocation.get_arcade_coords(arcade_id)
        distance = hs.haversine((arcade_x, arcade_y), (user_x, user_y), unit= Unit.METERS)
        direction = 'placeholder'
        response_dict = {'direction': direction, 'distance': distance}
        
        return api_bp.response_class(
            response=json.dumps(response_dict),
            status=200,
            mimetype='application/json'
        )

@api_bp.route("/game/<id>/clue", methods = ['GET', 'POST'])
def get_clue():
    #needs to be sent current location of user in request
    return ""



