from flask import Flask, request
import json
import haversine as hs

app = Flask(__name__)
app.config["DEBUG"] = True

@app.route("/guess", methods = ['GET', 'POST'])
def recieve_guess():
    content = request.json
    user_position = content['user_coordinates']
    
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