from flask import Blueprint, render_template, session
from arcadia.arcadiaApp.requiremobile import requiremobile
from flask import Blueprint, request
from passlib.hash import argon2
from requests import Response
from arcadia.db import get_db
from arcadia.arcadiaApp.requiremobile import requiremobile

# from flask import current_app as app

app_bp = Blueprint('app_bp', __name__, template_folder="templates", static_folder="static", static_url_path="/ast")

@app_bp.route('/')
@requiremobile
def home():
    if session.get("userid"):
        return render_template("displayguesses.jinja2")
    else:
        return render_template("displayguesses.jinja2")



@app_bp.route('/register')
@requiremobile
def account():
    if request.method == 'POST':
        username = request.values.get('username')
        password = request.values.get('password')
        hashed_password = argon2.hash(password)

        db, cur = get_db()
        cur.execute("""INSERT INTO 'Users' (UserName, PasswordHash) VALUES (%s,%s);""",
        (username, hashed_password))

    return Response(
        status = 200,
        mimetype='application/json'
    )

@app_bp.route('/login')
@requiremobile
def login():
    if request.method == 'POST':
        username = request.values.get('username')
        password = request.values.get('password')
        hashed_password = argon2.hash(password)
    
        
        
    return Response(
        status = 200,
        mimetype='application/json'
    )