from flask import Blueprint, request
from passlib.hash import argon2
from requests import Response
from db import get_db

account_bp = Blueprint('account_bp', __name__)

@account_bp.route('/create')
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

@account_bp.route('/login')
def login():
    if request.method == 'POST':
        username = request.values.get('username')
        password = request.values.get('password')
        hashed_password = argon2.hash(password)
    
        
        
    return Response(
        status = 200,
        mimetype='application/json'
    )