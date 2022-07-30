import re
from flask import Blueprint, render_template, session, redirect, url_for
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
    if session.get("UserID"):
        return render_template("apphome.jinja2")
    else:
        return redirect(url_for("app_bp.login"))


@app_bp.route('/guesser')
@requiremobile
def guesser():
    return render_template("displayguesses.jinja2")

@app_bp.route('/badges')
@requiremobile
def badges():
    user_id = session["UserID"]
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

@app_bp.route('/register')
@requiremobile
def register():

    if request.method == 'GET':
        if session.get("UserID"):
            redirect(url_for("app_bp.apphome"))
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
            redirect(url_for("app_bp.apphome"))
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

            if resp == None:
                return redirect(url_for("account_bp.login"))

            if not argon2.verify(password, resp["PasswordHash"]):
                return redirect(url_for("account_bp.login"))

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

