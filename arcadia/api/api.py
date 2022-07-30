from flask import Flask, request
import json
import haversine as hs
from .arcadeLocation import arcadeLocation


app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/guess", methods = ['GET', 'POST'])
def recieve_guess():
    if request.method == 'POST':
        user_x = request.values.get('xcoord')
        user_y = request.values.get('ycoord')
        arcade_id = request.values.get('arcade_id')
        arcade_x, arcade_y = arcadeLocation.get_arcade_coords(arcade_id)
        hs.haversine
    return direction, distance

@app.route("/getfirstclue", methods = ['GET', 'POST'])
def get_first_clue():
    #needs to be sent current location of user in request
    return ""


def generate_game_location():
    return ""

def asd():
    pass


if __name__ == "__main__":
 app.run(host='0.0.0.0', debug=True)