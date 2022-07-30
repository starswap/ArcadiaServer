from flask import Blueprint, Flask, request, Response
import json
from arcadia.api.modlocation import returnNearCoords, getArcadeCoords

from arcadia.api.modlocation.distdir import dist, direc

api_bp = Blueprint('api_bp', __name__)


@api_bp.route("/game/find", methods=['GET', 'POST'])
def find_games():
    # needs to be sent current location of user in request
    user_x = request.values.get('xcoord')
    user_y = request.values.get('ycoord')

    user_x = 51.364991
    user_y = -0.361726

    return Response(
        response=json.dumps(
            {
                "radius": 50,
                "locations": returnNearCoords(user_x, user_y)
            }
        ),
        status=200,
        mimetype='application/json'
    )


@api_bp.route("/game/<arcade_id>/guess", methods=['POST'])
def recieve_guess(arcade_id):
    user_x = request.values.get('xcoord')
    user_y = request.values.get('ycoord')
    poilat = request.values.get('poilat')
    poilong = request.values.get('poilong')
    # arcade_id = request.values.get('arcade_id')
    
    
    #! also pull the poi coords out of the database for the arcade ID
    arcade_x, arcade_y = getArcadeCoords( xloc, xlat)
    
    
    # distance = hs.haversine((arcade_x, arcade_y), (user_x, user_y), unit=Unit.METERS)
    distance = dist(arcade_x, arcade_y, user_x, user_y)
    
    direction = direc(arcade_x, arcade_y, user_x, user_y)
    
    
    response_dict = {'direction': str(distance), 'distance': str(direction)}

    return Response(
        response=json.dumps(response_dict),
        status=200,
        mimetype='application/json'
    )


# #! I am not sure this is necessary?
# @api_bp.route("/game/<arcade_id>/clue", methods=['GET', 'POST'])
# def get_clue(arcade_id):
#     # needs to be sent current location of user in request
#     return Response(
#         response=json.dumps({"key": "str"}),
#         status=200,
#         mimetype='application/json'
#     )
