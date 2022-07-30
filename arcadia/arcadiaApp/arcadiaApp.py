from flask import Blueprint, render_template
from .requiremobile import requiremobile
# from flask import current_app as app

app_bp = Blueprint('app_bp', __name__, template_folder="templates", static_folder="static", static_url_path="/hst")

@app_bp.route('/')
@requiremobile
def home():
    return render_template("displayguesses.jinja2")

