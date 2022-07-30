from flask import Blueprint, render_template
# from flask import current_app as app

home_bp = Blueprint('home_bp', __name__, template_folder="templates", static_folder="static", static_url_path="/hst")

@home_bp.route('/')
def home():
    return render_template("home.jinja2")
