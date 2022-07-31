from flask import Blueprint, render_template, send_file
# from flask import current_app as app

home_bp = Blueprint('home_bp', __name__, template_folder="templates", static_folder="static", static_url_path="/hst")

@home_bp.route('/')
def home():
    return render_template("home.jinja2")

@home_bp.route('/sw.js')
def sw():
    return send_file('./sw.js', attachment_filename='sw.js')

