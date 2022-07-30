from flask import Blueprint, Flask, request
import json
import haversine as hs
from .arcadeLocation import arcadeLocation
from haversine import Unit
import math


app = Flask(__name__)
app.config["DEBUG"] = True

api_bp = Blueprint('api_bp', __name__)

@app.route("/guess", methods = ['GET', 'POST'])
def recieve_guess():
    if request.method == 'POST':
        user_x = request.values.get('xcoord')
        user_y = request.values.get('ycoord')
        arcade_id = request.values.get('arcade_id')
        arcade_x, arcade_y = arcadeLocation.get_arcade_coords(arcade_id)
        distance = hs.haversine((arcade_x, arcade_y), (user_x, user_y), unit= Unit.METERS)
        direction = 'placeholder'
    return direction, distance

@app.route("/getfirstclue", methods = ['GET', 'POST'])
def get_first_clue():
    #needs to be sent current location of user in request
    return ""



