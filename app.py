from flask import Flask

app = Flask(__name__)

@app.route("/guess")
def recieve_guess():
    return ""