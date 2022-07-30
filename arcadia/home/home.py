from flask import Blueprint, render_template, send_from_directory, session
from flask import current_app as app

home_bp = Blueprint('home_bp', __name__,)

@home_bp.route('/', methods = ['GET'])
def home():
    pass