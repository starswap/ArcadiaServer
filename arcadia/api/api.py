from flask import Blueprint, Flask, request, Response
import json
from arcadia.api.modlocation import returnNearCoords, getArcadeCoords

from arcadia.api.modlocation.distdir import dist, direc



api_bp = Blueprint('api_bp', __name__)


@api_bp.route("/game/find", methods=['GET', 'POST'])
def find_games():
    jsonSent = request.get_json(force=True)

    # needs to be sent current location of user in request
    user_x = float(jsonSent['userlat'])
    user_y = float(jsonSent['userlong'])

    return Response(
        response=json.dumps(
            {
                "locations": returnNearCoords(user_x, user_y)
            }
        ),
        status=200,
        mimetype='application/json'
    )


@api_bp.route("/game/<arcade_id>/guess", methods=['POST'])
def receive_guess(arcade_id):

    jsonSent = request.get_json(force=True)

    userlat = float(jsonSent['userlat'])
    userlong = float(jsonSent['userlong'])
    poilat = float(jsonSent['poilat'])
    poilong = float(jsonSent['poilong'])
    
    if not userlat or not userlong or not poilat or not poilong:
        return "insufficient parameters"

    arcade_x, arcade_y = getArcadeCoords( poilat, poilong)

    # distance = hs.haversine((arcade_x, arcade_y), (user_x, user_y), unit=Unit.METERS)
    distance = dist(arcade_x, arcade_y, userlat, userlong)
    direction = direc(arcade_x, arcade_y, userlat, userlong)

    if distance < 15:
        return Response(
            response=json.dumps({"success": "gamepermitted"}),
            status=200,
            mimetype='application/json'
        )

    response_dict = {'distance': str(distance), 'direction': str(direction)}

    return Response(
        response=json.dumps(response_dict),
        status=200,
        mimetype='application/json'
    )



