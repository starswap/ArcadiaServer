from flask import Blueprint, Flask, request, Response,session
import json
from arcadia.api.modlocation import getGameType, returnNearCoords, getArcadeCoords

from arcadia.api.modlocation.distdir import bearingToCardinal, dist, direc


TARGET_DISTANCE = 10

api_bp = Blueprint('api_bp', __name__)


@api_bp.route("/game/find", methods=['GET', 'POST'])
def find_games():
    jsonSent = request.get_json(force=True)
    print(jsonSent)
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
    arcade_id = int(arcade_id)
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
    direction = direc(userlat, userlong, arcade_x, arcade_y)
    bearing = bearingToCardinal(direction)

    if distance < TARGET_DISTANCE:
        return Response(
            response=json.dumps({"success": "gamepermitted", "gamecode": getGameType(arcade_id)}),
            status=200,
            mimetype='application/json'
        )

    response_dict = {'distance': str(distance), 'direction': str(direction),"bearing":str(bearing)}

    return Response(
        response=json.dumps(response_dict),
        status=200,
        mimetype='application/json'
    )



