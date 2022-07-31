import re
from flask import Blueprint, flash, render_template, send_file, session, redirect, url_for
from arcadia.arcadiaApp.requiremobile import requiremobile
from flask import Blueprint, request
from passlib.hash import argon2
from requests import Response
from arcadia.db import get_db

# from flask import current_app as app
app_bp = Blueprint('app_bp', __name__, template_folder="templates",
                   static_folder="static", static_url_path="/ast")


@app_bp.route('/')
@requiremobile
def home():
    if session.get("UserID") is not None:
        return render_template("apphome.jinja2")
    else:
        return redirect(url_for("app_bp.login"))


@app_bp.route('/guesser')
@requiremobile
def guesser():
    print(session.get("success"))
    if session.get("success") == "gamepermitted":
        return render_template("congratulations.jinja2")
    else:
        return render_template("displayguesses.jinja2")

@app_bp.route('/offline')
@requiremobile
def offline():
    return render_template("offline.jinja2")

@app_bp.route('/badges')
@requiremobile
def badges():
    user_id = session.get("UserID")
    db, cur = get_db()
    cur.execute(('SELECT BadgeID FROM "UserBadges" WHERE UserID=%s'), (user_id,))
    response = cur.fetchall()
    resp = []
    for row in response:
        badge_id = row[0]
        cur.execute(('SELECT BadgeName FROM "Badges" WHERE BadgeID=%s'), (badge_id))
        badge_name = cur.fetchone()
        url = "arcadia/arcadiaApp/static/images/" + badge_id + ".jpeg"
        resp.append((url, badge_name))
    return render_template("badgedisplayer.jinja2", response=resp)

@app_bp.route('/register', methods=["GET", "POST"])
@requiremobile
def register():

    if request.method == 'GET':
        if session.get("UserID"):
            redirect(url_for("app_bp.home"))
        return render_template("register.jinja2")

    elif request.method == 'POST':
        if not session.get("UserID"):
            username = request.values.get('username')
            password = request.values.get('password')
            hashed_password = argon2.hash(password)

            db, cur = get_db()
            cur.execute('INSERT INTO "Users" (UserName, PasswordHash) VALUES (%s,%s);',
                        (username, hashed_password))

            cur.execute(
                'SELECT UserID FROM "Users" WHERE UserName=%s;', (username,))
            session['UserID'] = cur.fetchone()
            session['UserName'] = username
            return redirect(url_for("app_bp.home"))
        else:
            return "already logged in, logout before registering"


@app_bp.route('/login', methods=["GET", "POST"])
@requiremobile
def login():

    if request.method == 'GET':
        if session.get("UserID"):
            redirect(url_for("app_bp.home"))
        return render_template("login.jinja2",)
    elif request.method == 'POST':
        if not session.get("UserID"):
            username = request.values.get('username')
            password = request.values.get('password')
            hashed_password = argon2.hash(password)

            db, cur = get_db()
            cur.execute(
                'SELECT PasswordHash FROM "Users" WHERE UserName= %s;', (username,))
            resp = cur.fetchone()
            
            if resp == None: # No user exists
                flash("Incorrect Login details")
                return redirect(url_for("app_bp.login"))

            if not argon2.verify(hashed_password, resp["passwordhash"]): # Bad password for user
                flash("Incorrect Login details")
                return redirect(url_for("app_bp.login"))

            else:
                cur.execute(
                    'SELECT UserID FROM "Users" WHERE UserName=%s;', (username,))
                session['UserID'] = cur.fetchone()
                session['UserName'] = username
                return redirect(url_for("app_bp.home"))
        else:
            return "already logged in, logout before logging in again"


@app_bp.route('/logout')
@requiremobile
def logout():
    if session.get("UserID"):
        session.pop("UserID")
    if session.get("UserName"):
        session.pop("UserName")
    return redirect(url_for("app_bp.home"))



@app_bp.route('/playgame')
@requiremobile
def playgame():
    return render_template("playgame.jinja2")

